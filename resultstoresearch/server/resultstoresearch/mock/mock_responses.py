from resultstoresearch.resultstoresearchapi import (
    invocation_pb2, common_pb2, timestamp_pb2, duration_pb2,
    resultstore_download_pb2, file_pb2, wrappers_pb2, target_pb2)
"""
Used by mock proxy to generate mock responses
"""


def mock_search_invocations_response():
    response = resultstore_download_pb2.SearchInvocationsResponse(
        invocations=[mock_invocation(),
                     mock_invocation('invo1', 'tool1')],
        tools_list=['tool1', 'tool2'])
    return response


def mock_search_invocations_response_with_tools():
    response = resultstore_download_pb2.SearchInvocationsResponse(
        invocations=[mock_invocation('invo1', 'tool1')],
        tools_list=['tool1', 'tool2'])
    return response


def mock_invocation(
        invocation_name='invocations/51be7217-9798-4448-adf8-1e4428c71e9e',
        tool_tag=''):
    invocation = invocation_pb2.Invocation(
        name=invocation_name,
        status_attributes=mock_status_attributes(),
        timing=mock_timing(),
        invocation_attributes=mock_invocation_attributes(),
        workspace_info=mock_workspace_info(tool_tag),
        files=[mock_file()])
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
    invocation_attributes = invocation_pb2.InvocationAttributes(
        users=(['lewiscraig']), labels=(['dank', 'meme']))
    return invocation_attributes


def mock_workspace_info(tool_tag=''):
    workspace_info = invocation_pb2.WorkspaceInfo(
        hostname='piestation.mtv.corp.google.com',
        command_lines=mock_command_lines(),
        tool_tag=tool_tag)
    return workspace_info


def mock_command_lines():
    command_line = invocation_pb2.CommandLine(label='SiVal Test Runner',
                                              tool='ManifestRunner')
    return [command_line]


def mock_target():
    return target_pb2.Target(name='mock-target', files=[mock_file()])


def mock_file():
    return file_pb2.File(uid='test-file',
                         length=mock_int_64_value(),
                         content_type='text/html')


def mock_int_64_value():
    return wrappers_pb2.Int64Value(value=45)
