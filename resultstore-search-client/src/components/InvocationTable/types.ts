import invocation_pb from '../../api/invocation_pb';

export interface Data {
    status: string;
    name: string;
    labels: string;
    date: string;
    duration: string;
    user: string;
}

export interface Column {
    id: 'status' | 'name' | 'labels' | 'date' | 'duration' | 'user';
    label: string;
    minWidth?: number;
    align?: 'right';
}

export interface InvocationTableProps {
    invocations: Array<invocation_pb.Invocation>;
}
