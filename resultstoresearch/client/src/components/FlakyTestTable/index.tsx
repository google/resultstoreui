// FlakyTestTable Component
/**
 * Component that renders flaky test data
 * @packageDocumentation
 */

import React, { useEffect, useState } from 'react';
import {
    AutoSizer,
    Grid,
    GridCellRenderer,
    ScrollSync,
    Index,
    ColumnProps,
} from 'react-virtualized';
import { makeStyles, createStyles } from '@material-ui/core/styles';
import { InvocationTest } from '../../api/invocation_pb';
import {
    parseFlakyTestTableColumns,
    parseFlakyTestTableData,
    AggregateTestData,
    TableCell,
} from './utils';
import {
    GridContainer,
    GridBodyContainer,
    HeaderContainer,
    NoTestCell,
    PassingTestCell,
    FailingTestCell,
    TestNameCell,
    TestNameDividerCell,
    DividerCell,
    TitleHeaderCell,
    HeaderCell,
    Container,
} from './styles';

export const DividerRowHeight = 25;
export const RowHeight = 35;
const HeaderRowHeight = 50;
const TestNameCellWidth = 400;
const ColumnWidth = 50;

/** FlakyTestTable Props */
interface Props {
    /** List of tests to be rendered in the flaky test ui */
    invocationsTestList: Array<InvocationTest>;
    /** Callback function that will pass the total tests, number of tests passed and number of test failed */
    setAggregateTestData: (aggregateTestData: AggregateTestData) => void;
}

interface State {
    columns: ColumnProps[];
    rows: TableCell[];
    rowNames: string[];
    tableSize: number;
    aggregateTestData: AggregateTestData;
}

const useStyles = makeStyles(() =>
    createStyles({
        bodyGrid: {
            width: '100%',
            border: '1px solid #e0e0e0;',
        },
        gridHeader: {
            overflow: 'hidden !important',
        },
    })
);

/** Function to render TestNameHeaders */
const testNameHeaderCellRenderer: GridCellRenderer = ({ style }) => {
    return <TitleHeaderCell style={style} />;
};

/** FlakyTestTable Component */
export const FlakyTestTable: React.FC<Props> = ({
    invocationsTestList,
    setAggregateTestData,
}) => {
    const classes = useStyles();
    const [state, setState] = useState<State>({
        rows: [],
        rowNames: [],
        tableSize: 0,
        columns: [],
        aggregateTestData: {
            totalTests: 0,
            passedTests: 0,
            failedTests: 0,
        },
    });
    const { rows, rowNames, tableSize, columns } = state;
    useEffect(() => {
        const columns = parseFlakyTestTableColumns(invocationsTestList);
        const {
            rows,
            rowNames,
            tableSize,
            aggregateTestData,
        } = parseFlakyTestTableData(invocationsTestList, columns);
        setState({
            rows,
            rowNames,
            tableSize,
            aggregateTestData,
            columns,
        });
        setAggregateTestData(aggregateTestData);
    }, []);

    const cellRenderer: GridCellRenderer = ({
        columnIndex,
        style,
        rowIndex,
    }) => {
        const columnName = columns[columnIndex].dataKey as string;
        const cell = rows[rowIndex];

        if (cell.isDivider) {
            return <DividerCell style={style} />;
        }

        const cellData = cell.cellData[columnName];

        if (typeof cellData === 'string') {
            return <TestNameCell style={style}>{cell}</TestNameCell>;
        } else {
            const onClick = () => {
                window.open(cellData.url);
            };
            if (!cellData.hasTest) {
                return <NoTestCell style={style}>{}</NoTestCell>;
            } else if (cellData.testStatus === 'P') {
                return (
                    <PassingTestCell
                        style={style}
                        onClick={onClick}
                    ></PassingTestCell>
                );
            } else {
                return (
                    <FailingTestCell style={style} onClick={onClick}>
                        {cellData.testStatus}
                    </FailingTestCell>
                );
            }
        }
    };

    const testNameCellRenderer: GridCellRenderer = ({ style, rowIndex }) => {
        const rowName = rowNames[rowIndex];
        const cell = rows[rowIndex];
        if (cell.isDivider) {
            return (
                <TestNameDividerCell style={style}>
                    {rowName}
                </TestNameDividerCell>
            );
        }
        return <TestNameCell style={style}>{rowName}</TestNameCell>;
    };

    const gridHeaderCellRenderer: GridCellRenderer = ({
        columnIndex,
        style,
    }) => {
        const columnTitle = columns[columnIndex].dataKey;
        const columnName = columns[columnIndex].label;
        return (
            <HeaderCell style={style} title={columnTitle}>
                {columnName}
            </HeaderCell>
        );
    };

    const getRowHeight = ({ index }: Index) => {
        const cell = rows[index];
        if (cell.isDivider) {
            return DividerRowHeight;
        }
        return RowHeight;
    };

    return (
        <Container elevation={3} id={'FlakyTestTable'}>
            <ScrollSync>
                {({ onScroll, scrollLeft, scrollTop }) => (
                    <AutoSizer>
                        {({ height, width }) => (
                            <GridContainer width={width}>
                                <HeaderContainer>
                                    <Grid
                                        cellRenderer={
                                            testNameHeaderCellRenderer
                                        }
                                        width={TestNameCellWidth}
                                        height={HeaderRowHeight}
                                        rowHeight={HeaderRowHeight}
                                        columnWidth={TestNameCellWidth}
                                        rowCount={1}
                                        columnCount={1}
                                    />
                                    <Grid
                                        height={height - HeaderRowHeight}
                                        width={TestNameCellWidth}
                                        columnCount={1}
                                        rowCount={rows.length}
                                        columnWidth={TestNameCellWidth}
                                        rowHeight={getRowHeight}
                                        cellRenderer={testNameCellRenderer}
                                        className={classes.gridHeader}
                                        scrollTop={scrollTop}
                                    />
                                </HeaderContainer>
                                <GridBodyContainer>
                                    <AutoSizer>
                                        {({
                                            height: bodyHeight,
                                            width: bodyWidth,
                                        }) => (
                                            <div>
                                                <Grid
                                                    columnWidth={ColumnWidth}
                                                    columnCount={columns.length}
                                                    height={HeaderRowHeight}
                                                    className={
                                                        classes.gridHeader
                                                    }
                                                    cellRenderer={
                                                        gridHeaderCellRenderer
                                                    }
                                                    rowHeight={HeaderRowHeight}
                                                    rowCount={1}
                                                    scrollLeft={scrollLeft}
                                                    width={bodyWidth}
                                                />

                                                <Grid
                                                    height={
                                                        bodyHeight -
                                                        HeaderRowHeight
                                                    }
                                                    width={bodyWidth}
                                                    columnCount={columns.length}
                                                    rowCount={rows.length}
                                                    columnWidth={({
                                                        index,
                                                    }) => {
                                                        return columns[index]
                                                            .width;
                                                    }}
                                                    estimatedRowSize={tableSize}
                                                    rowHeight={getRowHeight}
                                                    onScroll={onScroll}
                                                    cellRenderer={cellRenderer}
                                                    className={classes.bodyGrid}
                                                    overscanColumnCount={10}
                                                    overscanRowCount={25}
                                                />
                                            </div>
                                        )}
                                    </AutoSizer>
                                </GridBodyContainer>
                            </GridContainer>
                        )}
                    </AutoSizer>
                )}
            </ScrollSync>
        </Container>
    );
};

export default FlakyTestTable;
