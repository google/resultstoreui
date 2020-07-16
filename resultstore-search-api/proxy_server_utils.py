from resultstoresearchapi import (
    resultstore_download_pb2_grpc as resultstoresearch_download_pb2_grpc,
    resultstore_download_pb2 as resultstoresearch_download_pb2, invocation_pb2
    as resultstoresearch_invocation_pb2, timestamp_pb2 as
    resultstoresearch_timestamp_pb2, duration_pb2 as
    resultstoresearch_duration_pb2, common_pb2 as resultstoresearch_common_pb2,
    wrappers_pb2 as resultoresearch_wrapper_pb2, file_pb2 as
    resultstoresearch_file_pb2, action_pb2 as resultstoresearch_action_pb2,
    test_suite_pb2 as resultoresearch_test_suite_pb2)
from collections import defaultdict
import sys


def configure_grpc_error(context, rpc_error):
    """
    Sets proper error details and code on context

    Args:
        context (grpc.Context)
        rpc_error (grpc.RpcError)
    """
    context.set_details(rpc_error.details())
    context.set_code(rpc_error.code())


def has_tool_tag(invocation):
    """
    Checks if invocation has a tool_tag in workspace info

    Args:
        invocation (Invocation)

    Returns:
        True if tool_tag exists else false
    """
    if (hasattr(invocation, 'workspace_info')
            and hasattr(invocation.workspace_info, 'tool_tag')
            and invocation.workspace_info.tool_tag != ''):
        return True
    return False


def filter_tool(invocations, tool):
    """
    Filters out invocations that do not have a matching tool tag
    from the SearchInvocations request. If no tool is specified
    returns the original invocation list

    Args:
        invocation (Invocation)
        tool (str): tool_tag to filter on

    Returns:
        A list of Invocations after filtering
    """
    filtered_invocations = []
    if not tool:
        for invocation in invocations:
            filtered_invocations.append(convert_invocation(invocation))
        return filtered_invocations

    for invocation in invocations:
        if (has_tool_tag(invocation)
                and invocation.workspace_info.tool_tag == tool):
            filtered_invocations.append(convert_invocation(invocation))
    return filtered_invocations


def update_tools_list(invocations, tools_list, fs):
    """
    Updates tool tag list and firestore with seen tool_tags based on current
    invocations list in firestore queried by SearchInvocations

    Args:
        invocations (Seq[Invocation]): Current list of invocations
        tools_list (Seq[str]): tools list to be updated

    Returns:
        Updated tools list
    """
    for invocation in invocations:
        if (has_tool_tag(invocation)
                and invocation.workspace_info.tool_tag not in tools_list):
            fs.add_tool_tag(invocation.workspace_info.tool_tag)
            tools_list.append(invocation.workspace_info.tool_tag)
    return tools_list


def parse_tests(invocation, actions):
    target_case = {}
    for action in actions:
        if hasattr(action, 'test_action') and hasattr(action.test_action, 'test_suite'):
            target_id = action.id.target_id
            if target_id not in target_case:
                target_case[target_id] = resultstoresearch_invocation_pb2.CaseNameToCaseMap(
                )
            for test in action.test_action.test_suite.tests:
                test_case_name = test.test_case.case_name
                if test_case_name not in target_case[target_id].case_name:
                    target_case[target_id].case_name[test_case_name].CopyFrom(
                        test.test_case)

    return resultstoresearch_invocation_pb2.InvocationTest(
        invocation=invocation,
        target_case=target_case
    )


"""
Helper functions to convert resultstore objects into resultstoresearch objects
"""


def convert_invocations(invocations):
    converted_invocations = []
    for invocation in invocations:
        converted_invocations.append(convert_invocation(invocation))
    return converted_invocations


def convert_invocation(invocation):
    invocation_attributes = convert_invocation_attributes(
        invocation.invocation_attributes) if hasattr(
            invocation, 'invocation_attributes') else None
    timing = convert_timing(invocation.timing) if hasattr(
        invocation, 'timing') else None
    workspace_info = convert_workspace_info(
        invocation.workspace_info) if hasattr(invocation,
                                              'workspace_info') else None
    status_attributes = convert_status_attributes(
        invocation.status_attributes) if hasattr(invocation,
                                                 'status_attributes') else None
    files = convert_files(
        invocation.files if hasattr(invocation, 'files') else None)
    return resultstoresearch_invocation_pb2.Invocation(
        name=invocation.name,
        status_attributes=status_attributes,
        timing=timing,
        invocation_attributes=invocation_attributes,
        workspace_info=workspace_info,
        files=files)


def convert_invocation_attributes(invocation_attributes):
    project_id = invocation_attributes.project_id if hasattr(
        invocation_attributes, 'project_id') else ''
    users = invocation_attributes.users if hasattr(invocation_attributes,
                                                   'users') else []
    labels = invocation_attributes.labels if hasattr(invocation_attributes,
                                                     'labels') else []
    description = invocation_attributes.description if hasattr(
        invocation_attributes, 'description') else ''
    return resultstoresearch_invocation_pb2.InvocationAttributes(
        project_id=project_id,
        users=users,
        labels=labels,
        description=description)


def convert_timing(timing):
    start_time = convert_timestamp(timing.start_time) if hasattr(
        timing, 'start_time') else None
    duration = convert_duration(timing.duration) if hasattr(
        timing, 'duration') else None
    return resultstoresearch_common_pb2.Timing(start_time=start_time,
                                               duration=duration)


def convert_timestamp(timestamp):
    seconds = timestamp.seconds if hasattr(timestamp, 'seconds') else None
    nanos = timestamp.nanos if hasattr(timestamp, 'nanos') else None
    return resultstoresearch_timestamp_pb2.Timestamp(seconds=seconds,
                                                     nanos=nanos)


def convert_duration(duration):
    seconds = duration.seconds if hasattr(duration, 'seconds') else None
    nanos = duration.nanos if hasattr(duration, 'nanos') else None
    return resultstoresearch_duration_pb2.Duration(seconds=seconds,
                                                   nanos=nanos)


def convert_workspace_info(workspace_info):
    hostname = workspace_info.hostname if hasattr(workspace_info,
                                                  'hostname') else ''
    working_directory = workspace_info.working_directory if hasattr(
        workspace_info, 'working_directory') else ''
    tool_tag = workspace_info.tool_tag if hasattr(workspace_info,
                                                  'tool_tag') else ''
    command_lines = convert_command_lines(
        workspace_info.command_lines) if hasattr(workspace_info,
                                                 'command_lines') else []
    return resultstoresearch_invocation_pb2.WorkspaceInfo(
        hostname=hostname,
        working_directory=working_directory,
        tool_tag=tool_tag,
        command_lines=command_lines)


def convert_command_lines(command_lines):
    converted_command_lines = []
    for command_line in command_lines:
        label = command_line.label if hasattr(command_line, 'label') else ''
        tool = command_line.tool if hasattr(command_line, 'tool') else ''
        args = command_line.args if hasattr(command_line, 'args') else []
        command = command_line.command if hasattr(command_line,
                                                  'command') else ''
        converted_command_lines.append(
            resultstoresearch_invocation_pb2.CommandLine(label=label,
                                                         tool=tool,
                                                         args=args,
                                                         command=command))
    return converted_command_lines


def convert_status_attributes(status_attributes):
    status = status_attributes.status if hasattr(status_attributes,
                                                 'status') else None
    description = status_attributes.description if hasattr(
        status_attributes, 'description') else ''
    return resultstoresearch_common_pb2.StatusAttributes(
        status=status, description=description)


def convert_actions(actions):
    converted_actions = []
    for action in actions:
        converted_actions.append(convert_action(action))
    return converted_actions


def convert_action(action):
    converted_action = resultstoresearch_action_pb2.Action(
        name=action.name,
        test_action=convert_test_action(action.test_action) if hasattr(
            action, 'test_action') else None
    )
    return converted_action


def convert_test_action(test_action):
    converted_test_action = resultstoresearch_action_pb2.TestAction(
        test_suite=convert_test_suite(test_action.test_suite) if hasattr(
            test_action, 'test_suite') else None
    )
    return converted_test_action


def convert_test_suite(test_suite):
    converted_test_suite = resultoresearch_test_suite_pb2.TestSuite(
        suite_name=test_suite.suite_name,
        tests=convert_tests(test_suite.tests) if hasattr(
            test_suite, 'tests') else None
    )
    return converted_test_suite


def convert_tests(tests):
    converted_tests = []
    for test in tests:
        converted_tests.append(convert_test(test))
    return converted_tests


def convert_test(test):
    converted_test = resultoresearch_test_suite_pb2.Test(
        test_case=convert_test_case(test.test_case)
    )
    return converted_test


def convert_test_case(test_case):
    converted_test_case = resultoresearch_test_suite_pb2.TestCase(
        case_name=test_case.case_name,
        class_name=test_case.class_name,
        failures=convert_failures(test_case.failures) if hasattr(
            test_case, 'failures') else None,
        errors=convert_errors(test_case.errors) if hasattr(
            test_case, 'errors') else None,
        result=test_case.result,
        timing=convert_timing(test_case.timing) if hasattr(
            test_case, 'timing') else None
    )
    return converted_test_case


def convert_failures(failures):
    converted_failures = []
    for failure in failures:
        converted_failures.append(convert_failure(failure))
    return converted_failures


def convert_failure(failure):
    return resultoresearch_test_suite_pb2.TestFailure(
        failure_message=failure.failure_message,
        exception_type=failure.exception_type,
        stack_trace=failure.stack_trace,
        expected=failure.expected,
        actual=failure.actual
    )


def convert_errors(errors):
    converted_errors = []
    for error in errors:
        converted_errors.append(convert_error(error))
    return converted_errors


def convert_error(error):
    return resultoresearch_test_suite_pb2.TestError(
        error_message=error.error_message,
        exception_type=error.exception_type,
        stack_trace=error.stack_trace
    )


def convert_files(files):
    converted_files = []
    for file in files:
        converted_files.append(convert_file(file))
    return converted_files


def convert_file(file):
    uid = file.uid if hasattr(file, 'uid') else ''
    uri = file.uri if hasattr(file, 'uri') else ''
    length = convert_int_64_value(
        file.length) if hasattr(file, 'length') else None
    content_type = file.content_type if hasattr(file, 'content_type') else ''
    archive_entry = convert_archive_entry(file.archive_entry) if hasattr(
        file, 'archive_entry') else None
    content_viewer = file.content_viewer if hasattr(file,
                                                    'content_viewer') else ''
    hidden = file.hidden if hasattr(file, 'hidden') else False
    description = file.description if hasattr(file, 'description') else ''
    digest = file.digest if hasattr(file, 'digest') else ''
    hash_type = file.hash_type if hasattr(
        file,
        'hash_type') else resultstoresearch_file_pb2.File.HASH_TYPE_UNSPECIFIED

    return resultstoresearch_file_pb2.File(uid=uid,
                                           uri=uri,
                                           length=length,
                                           content_type=content_type,
                                           archive_entry=archive_entry,
                                           content_viewer=content_viewer,
                                           hidden=hidden,
                                           description=description,
                                           digest=digest,
                                           hash_type=hash_type)


def convert_archive_entry(archive_entry):
    path = archive_entry.path if hasattr(archive_entry, 'path') else ''
    length = convert_int_64_value(archive_entry.length) if hasattr(
        archive_entry, 'length') else None
    content_type = archive_entry.content_type if hasattr(
        archive_entry, 'content_type') else ''

    return resultstoresearch_file_pb2.ArchiveEntry(path=path,
                                                   length=length,
                                                   content_type=content_type)


def convert_int_64_value(int_64_value):
    return resultoresearch_wrapper_pb2.Int64Value(value=int_64_value.value)


def print_flush(val):
    print(val, flush=True)
