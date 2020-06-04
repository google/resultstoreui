import React from "react";
import { makeStyles, Theme, createStyles } from "@material-ui/core/styles";
import Paper from "@material-ui/core/Paper";
import Table from "@material-ui/core/Table";
import TableBody from "@material-ui/core/TableBody";
import TableCell from "@material-ui/core/TableCell";
import TableContainer from "@material-ui/core/TableContainer";
import TableHead from "@material-ui/core/TableHead";
import TablePagination from "@material-ui/core/TablePagination";
import TableRow from "@material-ui/core/TableRow";
import moment from "moment";
import invocation_pb from "../../api/invocation_pb";

interface Column {
  id: "status" | "name" | "labels" | "date" | "duration" | "user";
  label: string;
  minWidth?: number;
  align?: "right";
}

const columns: Column[] = [
  { id: "status", label: "Status" },
  { id: "name", label: "Name" },
  { id: "labels", label: "Labels" },
  { id: "date", label: "Run Date" },
  { id: "duration", label: "Duration" },
  { id: "user", label: "User" },
];

interface Data {
  status: string;
  name: string;
  labels: string;
  date: string;
  duration: string;
  user: string;
}

function createData(invocation: invocation_pb.Invocation): Data {
  const statusAttributes = invocation.getStatusAttributes();
  const invocationAttributes = invocation.getInvocationAttributes();
  const workspaceInfo = invocation.getWorkspaceInfo();
  const timing = invocation.getTiming();
  const startTime = moment.unix(timing.getStartTime().getSeconds());
  const endTime = startTime.clone();
  endTime.add(timing.getDuration().getSeconds());

  const status = statusAttributes.getDescription();
  const name = invocation.getName();
  const labels = invocationAttributes.getLabelsList().join(",");
  const date = startTime.format("YYYY-MM-DD, hh:mm A");
  const duration = moment
    .utc(
      moment.duration(timing.getDuration().getSeconds(), "s").asMilliseconds()
    )
    .format("mm:ss");
  const user = `${
    invocationAttributes.getUsersList()[0]
  }@${workspaceInfo.getHostname()}`;
  return { status, name, labels, date, duration, user };
}

const useStyles = makeStyles((theme: Theme) =>
  createStyles({
    margin: {
      margin: theme.spacing(2),
    },
    container: {
      display: "flex",
      flexWrap: "wrap",
    },
  })
);

export interface InvocationTableProps {
  invocations: Array<invocation_pb.Invocation>;
}

const InvocationTable: React.FC<InvocationTableProps> = ({ invocations }) => {
  const classes = useStyles();
  const [page, setPage] = React.useState(0);
  const [rowsPerPage, setRowsPerPage] = React.useState(10);
  const rows = invocations.map((invocation) => createData(invocation));

  return (
    // <Paper className={classes.root}>
      <TableContainer className={classes.container}>
        <Table stickyHeader aria-label="sticky table" className={classes.margin}>
          <TableHead>
            <TableRow>
              {columns.map((column) => (
                <TableCell
                  key={column.id}
                  align={column.align}
                  style={{ minWidth: column.minWidth }}
                >
                  {column.label}
                </TableCell>
              ))}
            </TableRow>
          </TableHead>
          <TableBody>
            {rows.map((row) => {
              return (
                <TableRow hover role="checkbox" tabIndex={-1} key={row.name}>
                  {columns.map((column) => {
                    return (
                      <TableCell key={column.id} align={column.align}>
                        {row[column.id]}
                      </TableCell>
                    );
                  })}
                </TableRow>
              );
            })}
          </TableBody>
        </Table>
      </TableContainer>
  );
};

export default InvocationTable;
