import { ColumnProps } from 'react-virtualized';
import { InvocationTest } from '../../api/invocation_pb';
import { TestCase } from '../../api/test_suite_pb';
import { flakyTestHeaderDate } from '../../utils';
import { DividerRowHeight, RowHeight } from './';

interface ToolTargetMap {
    [key: string]: {
        [key: string]: {
            [key: string]: TableCell;
        };
    };
}

export interface TableCell {
    isDivider: boolean;
    cellData: CellData;
}

interface CellData {
    [key: string]: string | TestResult;
}

export interface TestResult {
    hasTest: boolean;
    testStatus: 'P' | string;
    url: string;
}

export interface AggregateTestData {
    totalTests: number;
    failedTests: number;
    passedTests: number;
}

export const parseFlakyTestTableColumns = (
    invocationsTestList: Array<InvocationTest>
): Array<ColumnProps> => {
    const columns: Array<ColumnProps> = [];
    invocationsTestList.forEach((invocationTest) => {
        const invocation = invocationTest.getInvocation();
        const timing = invocation.getTiming();
        columns.push({
            dataKey: invocation.getName(),
            label: flakyTestHeaderDate(timing),
            width: 50,
        });
    });

    return columns;
};

export const parseFlakyTestTableData = (
    invocationsTestList: Array<InvocationTest>,
    columns: Array<ColumnProps>
): {
    rows: Array<TableCell>;
    rowNames: Array<string>;
    tableSize: number;
    aggregateTestData: AggregateTestData;
} => {
    const aggregateTestData: AggregateTestData = {
        totalTests: 0,
        failedTests: 0,
        passedTests: 0,
    };
    const toolTargetMap: ToolTargetMap = {};
    invocationsTestList.forEach((invocationTest) => {
        const invocation = invocationTest.getInvocation();
        const workspaceInfo = invocation.getWorkspaceInfo();
        const toolTag = workspaceInfo.getToolTag() || '';
        const targetCaseMap = invocationTest.getTargetCaseMap();
        parseTargetData(
            targetCaseMap,
            invocationsTestList,
            toolTargetMap,
            toolTag,
            columns,
            invocationTest,
            aggregateTestData
        );
    });
    return constructRows(toolTargetMap, aggregateTestData);
};

const parseTargetData = (
    targetCaseMap,
    invocationsTestList: Array<InvocationTest>,
    toolTargetMap: ToolTargetMap,
    toolTag: string,
    columns: Array<ColumnProps>,
    invocationTest: InvocationTest,
    aggregateTestData: AggregateTestData
) => {
    if (toolTargetMap[toolTag] === undefined) {
        toolTargetMap[toolTag] = {};
    }
    const targetNamesArr = targetCaseMap.keys().arr_ as [];
    targetNamesArr.forEach((targetName) => {
        if (toolTargetMap[toolTag][targetName] === undefined) {
            toolTargetMap[toolTag][targetName] = {};
            const caseNameMap = targetCaseMap.get(targetName).getCaseNameMap();
            const caseNamesArr = caseNameMap.keys().arr_ as Array<string>;
            caseNamesArr.forEach((caseName) => {
                if (
                    toolTargetMap[toolTag][targetName][caseName] === undefined
                ) {
                    parseCellData(
                        caseName,
                        targetName,
                        invocationsTestList,
                        toolTargetMap,
                        toolTag,
                        columns,
                        invocationTest,
                        aggregateTestData
                    );
                }
            });
        }
    });
};

const parseCellData = (
    caseName: string,
    targetName: string,
    invocationsTestList: Array<InvocationTest>,
    toolTargetMap: ToolTargetMap,
    toolTag: string,
    columns: Array<ColumnProps>,
    invocationTest: InvocationTest,
    aggregateTestData: AggregateTestData
) => {
    let cellData: CellData = {
        testName: caseName,
    };
    const currInvocation = invocationTest.getInvocation();
    const currWorkspaceInfo = currInvocation.getWorkspaceInfo();
    const currToolTag = currWorkspaceInfo.getToolTag() || '';
    for (var i = 0; i < columns.length; i++) {
        try {
            if (currToolTag === toolTag) {
                const currCase = invocationsTestList[i]
                    .getTargetCaseMap()
                    .get(targetName)
                    .getCaseNameMap()
                    .get(caseName) as TestCase;
                console.log(currCase);
                const result = currCase.getResult();
                if (result === TestCase.Result.COMPLETED) {
                    const numFailures = currCase.getFailuresList().length;
                    const numErrors = currCase.getErrorsList().length;
                    aggregateTestData.totalTests += 1;
                    if (numFailures === 0 && numErrors === 0) {
                        cellData[columns[i].dataKey] = {
                            hasTest: true,
                            testStatus: 'P',
                            url: formatTestUrl(
                                invocationsTestList[i]
                                    .getInvocation()
                                    .getName(),
                                targetName,
                                currCase.getClassName(),
                                currCase.getCaseName()
                            ),
                        };
                        aggregateTestData.passedTests += 1;
                    } else {
                        cellData[columns[i].dataKey] = {
                            hasTest: true,
                            testStatus: `F: ${numFailures}, E: ${numErrors}`,
                            url: formatTestUrl(
                                invocationsTestList[i]
                                    .getInvocation()
                                    .getName(),
                                targetName,
                                currCase.getClassName(),
                                currCase.getCaseName()
                            ),
                        };
                        aggregateTestData.failedTests += 1;
                    }
                }
            } else {
                cellData[columns[i].dataKey] = {
                    hasTest: false,
                    testStatus: '',
                    url: '',
                };
            }
        } catch {
            cellData[columns[i].dataKey] = {
                hasTest: false,
                testStatus: '',
                url: '',
            };
        }
    }
    toolTargetMap[toolTag][targetName][caseName] = {
        cellData,
        isDivider: false,
    };
};

const constructRows = (
    toolTargetMap: ToolTargetMap,
    aggregateTestData: AggregateTestData
) => {
    let tableSize = 0;
    const rows = [];
    const rowNames = [];
    for (const toolname in toolTargetMap) {
        const targetCaseMap = toolTargetMap[toolname];
        for (const targetName in targetCaseMap) {
            const caseNameMap = targetCaseMap[targetName];
            const dividerName = `${toolname} (Target: ${targetName})`;
            rowNames.push(dividerName);
            rows.push({
                isDivider: true,
            });
            tableSize += DividerRowHeight;
            for (const caseName in caseNameMap) {
                rowNames.push(caseName);
                rows.push(caseNameMap[caseName]);
                tableSize += RowHeight;
            }
        }
    }
    return { rows, rowNames, tableSize, aggregateTestData };
};

const formatTestUrl = (
    invocationName,
    targetName,
    testSuiteName,
    testSuite
) => {
    return `https://source.cloud.google.com/results/${invocationName}/targets/${encodeURIComponent(
        targetName
    )}/tests;group=${testSuiteName};test=${testSuite}`;
};
