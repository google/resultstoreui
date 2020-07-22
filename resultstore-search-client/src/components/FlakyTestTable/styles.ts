import styled from 'styled-components';
import Paper from '@material-ui/core/Paper';
const TestNameCellWidth = 400;
export const GridContainer = styled.div<{ width: number }>`
    display: flex;
    width: ${({ width }) => width}px;
`;

export const GridBodyContainer = styled.div`
    width: 100%;
`;

export const HeaderContainer = styled.div`
    width: ${TestNameCellWidth}px;
`;

export const NoTestCell = styled.div`
    background-color: grey;
    border: 1px solid black;
`;

export const PassingTestCell = styled.div`
    background-color: #4eb369;
    border: 1px solid black;
    cursor: pointer;
`;

export const FailingTestCell = styled.div`
    background-color: #d73f35;
    border: 1px solid black;
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
    font-size: 14px;
    cursor: pointer;
`;

export const TestNameCell = styled.div`
    width: ${TestNameCellWidth - 10}px !important;
    display: flex;
    align-items: center;
    padding-left: 10px;
    border-bottom: 1px solid black;
    border-right: 1px solid black;
    text-overflow: ellipsis;
    overflow: hidden;
    white-space: nowrap;
`;

export const TestNameDividerCell = styled.div`
    width: ${TestNameCellWidth - 10}px !important;
    display: flex;
    align-items: center;
    padding-left: 10px;
    border-right: 1px solid black;
    background-color: #e0e1dd;
    font-weight: bold;
    text-overflow: ellipsis;
    overflow: hidden;
    white-space: nowrap;
`;

export const DividerCell = styled.div`
    background-color: #e0e1dd;
`;

export const TitleHeaderCell = styled.div`
    display: flex;
    align-items: center;
    border-right: 1px solid black;
`;

export const HeaderCell = styled.div`
    display: flex;
    align-items: center;
    justify-content: center;
    text-align: center;
`;

export const Container = styled(Paper)`
    width: 91.5%;
    height: calc(98vh - 120px);
    margin-left: auto;
    margin-right: auto;
    margin-top: 20px;
    outline: none;
`;
