from resultstoresearchapi import (invocation_pb2, common_pb2, timestamp_pb2,
                                  duration_pb2, resultstore_download_pb2)

def mock_search_invocations_response():
    response = resultstore_download_pb2.SearchInvocationsResponse(
        invocations=[mock_invocation()])
    return response


def mock_invocation():
    invocation = invocation_pb2.Invocation(
        name='invocations/51be7217-9798-4448-adf8-1e4428c71e9e',
        status_attributes=mock_status_attributes(),
        timing=mock_timing(),
        invocation_attributes=mock_invocation_attributes())
    return invocation


def mock_status_attributes():
    status_attributes = common_pb2.StatusAttributes(
        status=common_pb2.Status.Value('TESTING'), description='TESTING')
    return status_attributes


def mock_timing():
    timing = common_pb2.Timing(start_time=mock_timestamp(),
                               duration=mock_duration())
    return timing


def mock_timestamp():
    timestamp = timestamp_pb2.Timestamp(seconds=1589929143, nanos=0)
    return timestamp


def mock_duration():
    duration = duration_pb2.Duration(seconds=6, nanos=0)
    return duration


def mock_invocation_attributes():
    invocation_attributes = invocation_pb2.InvocationAttributes(users=(['lewiscraig']),
                                                      labels=(['dank',
                                                               'meme']))
    return invocation_attributes


def mock_workspace_info():
    workspace_info = invocation_pb2.WorkspaceInfo(
        hostname='piestation.mtv.corp.google.com',
        command_lines=mock_command_line())
    return workspace_info


def mock_command_line():
    command_line = invocation_pb2.CommandLine(label='SiVal Test Runner',
                                              tool='ManifestRunner')
    return command_line
