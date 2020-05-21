import socket
import os
import getpass
import uuid
import pathlib
from google.protobuf import timestamp_pb2
from google.cloud import storage
from google import auth
from resultstoreapi.cloud.devtools.resultstore_v2.proto import common_pb2
from resultstoreapi.cloud.devtools.resultstore_v2.proto import (
    invocation_pb2, invocation_pb2_grpc, configuration_pb2, target_pb2,
    configuration_pb2, configured_target_pb2, action_pb2, file_pb2)

_PATH_INVOCATION = 'invocations/%s'
_PATH_TARGET = _PATH_INVOCATION + '/targets/%s'
_PATH_CONFIG_TARGET = _PATH_TARGET + '/configuredTargets/%s'
_PATH_ACTION = _PATH_CONFIG_TARGET + '/actions/%s'


def gen_new_uuid():
    """
    Generates a new uuid

    Returns:
        The generated uuid
    """
    return str(uuid.uuid4())


def set_starting_time_to_now(resource):
    """
    Sets the start time for the resource.

    Args:
        resource (Instance of either Invocation, Target, ConfiguredTarget or Action)
    """
    timestamp = timestamp_pb2.Timestamp()
    timestamp.GetCurrentTime()
    resource.timing.CopyFrom(common_pb2.Timing(start_time=timestamp))


def set_status_to_testing(resource):
    """
    Sets the status of the resource to TESTING

    Args:
        resource (Instance of either Invocation Target, ConfiguredTarget or Action)
    """
    resource.status_attributes.status = common_pb2.Status.Value('TESTING')


def get_name(invocation_id, target_id=None, config_id=None, action_id=None):
    """
    Gets the name given the corresponding ids.

    Args:
        invocation_id (str): The id of the invocation
        target_id (str): The id of the target
        config_id (str): The id of the configuration
        action_id (str): The id of the action

    Returns:
        The name of the resource given the provided ids

    Raises:
        ValueError: If the invocation id is empty
    """
    if not invocation_id:
        raise ValueError('Invocation id cannot be empty')
    if target_id and config_id and action_id:
        return _PATH_ACTION % (invocation_id, target_id, config_id, action_id)
    elif target_id and config_id:
        return _PATH_CONFIG_TARGET % (invocation_id, target_id, config_id)
    elif target_id:
        return _PATH_TARGET % (invocation_id, target_id)
    return _PATH_INVOCATION % invocation_id


def get_parent(resource):
    """
    Gets the parent name given the resource

    Args:
        resource (Instance of either Invocation Target, ConfiguredTarget or Action)

    Returns:
        The name of the parent of the resource

    Raises:
        ValueError: If the resource is empty
        TypeError: If the resource is not an instance of either Invocation Target,
            ConfiguredTarget or Action
    """
    if not resource:
        raise ValueError('Resource cannot be empty')
    if isinstance(resource, target_pb2.Target):
        return _PATH_INVOCATION % resource.id.invocation_id
    elif isinstance(resource, configuration_pb2.Configuration):
        return _PATH_INVOCATION % resource.id.invocation_id
    elif isinstance(resource, configured_target_pb2.ConfiguredTarget):
        return _PATH_TARGET % (resource.id.invocation_id,
                               resource.id.target_id)
    elif isinstance(resource, action_pb2.Action):
        return _PATH_CONFIG_TARGET % (resource.id.invocation_id,
                                      resource.id.target_id,
                                      resource.id.configuration_id)


def get_default_invocation(invocation_id=None, labels=None):
    """
    Returns a new Invocation with fields initialized to defaults

    Args:
        invocation_id (str): The id for the invocation
        labels (Sequence[str]): The labels for the invocation

    Returns:
        A new Invocation object
    """
    if not invocation_id:
        invocation_id = gen_new_uuid()
    if not labels:
        labels = []
    invocation = invocation_pb2.Invocation()
    invocation.id.invocation_id = invocation_id
    set_starting_time_to_now(invocation)
    set_status_to_testing(invocation)
    invocation.invocation_attributes.project_id = 'google.com:gchips-productivity'
    invocation.invocation_attributes.users.append(getpass.getuser())
    for label in labels:
        invocation.invocation_attributes.labels.append(label)
    invocation.workspace_info.hostname = socket.getfqdn()
    invocation.workspace_info.working_directory = os.getcwd()
    return invocation


def get_default_configuration(invocation_id, config_id=None):
    """
    Returns a new Configuration with fields initialized to defaults.

    Args:
        invocation_id (str): The id of the invocation for the configuration.
        config_id (str): The id of the configuration.

    Returns:
        A new Configuration object.
    """
    if not config_id:
        config_id = 'default'

    config = configuration_pb2.Configuration(id={
        'invocation_id': invocation_id,
        'configuration_id': config_id
    })
    return config


def get_default_target(invocation_id, target_id=None):
    """
    Returns a new Target with fields initialized to defaults.

    Args:
        invocation_id (str): The id of the invocation for the target.
        target_id (str): The id for the target.

    Returns:
        A new Target object.
    """
    if not target_id:
        target_id = gen_new_uuid()
    target = target_pb2.Target(
        id={
            'invocation_id': invocation_id,
            'target_id': target_id,
        },
        target_attributes={'type': target_pb2.TargetType.Value('TEST')},
        visible=True)
    set_starting_time_to_now(target)
    set_status_to_testing(target)
    return target


def get_default_configured_target(invocation_id, target_id, config_id):
    """
    Returns a new ConfiguredTarget with fields initialized to defaults.

    Args:
        invocation_id (str): The id of the invocation for the configured target.
        target_id (str): The id of the target for the configured target.
        config_id (str): The id of the configuration for the configured target.

    Returns:
        A new ConfiguredTarget object.
    """
    config_target = configured_target_pb2.ConfiguredTarget(
        id={
            'invocation_id': invocation_id,
            'target_id': target_id,
            'configuration_id': config_id
        })
    set_starting_time_to_now(config_target)
    set_status_to_testing(config_target)
    return config_target


def get_default_action(invocation_id, target_id, config_id, action_id=None):
    """
    Returns a new Action with fields initialized to defaults.
    
    Args:
        invocation_id (str): The id of the invocation for the action.
        target_id (str): The id of the target for the action
        config_id (str): The id of the configuration for the action.
        action_id (str): The id of the action.

    Returns:
        A new Action object.
    """
    if not action_id:
        action_id = 'test'
    action = action_pb2.Action(
        id={
            'invocation_id': invocation_id,
            'target_id': target_id,
            'configuration_id': config_id,
            'action_id': action_id
        })
    set_starting_time_to_now(action)
    set_status_to_testing(action)
    return action
