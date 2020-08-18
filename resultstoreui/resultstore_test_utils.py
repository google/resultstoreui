from unittest.mock import MagicMock
from resultstore_client import ResultStoreClient
from resultstoreapi.cloud.devtools.resultstore_v2.proto import (
    resultstore_download_pb2_grpc, resultstore_download_pb2, invocation_pb2,
    configuration_pb2, target_pb2, configured_target_pb2, action_pb2)


def create_return_invocation(request):
    return invocation_pb2.Invocation(
        id={'invocation_id': request.invocation_id})


def create_return_target(request):
    return target_pb2.Target(name="invocations/{}/targets/{}".format(
        request.target.id.invocation_id, request.target.id.target_id),
                             id={'target_id': request.target.id.target_id})


def create_return_configuration(request):
    return configuration_pb2.Configuration(
        name="invocations/{}/configs/{}".format(
            request.configuration.id.invocation_id,
            request.configuration.id.configuration_id),
        id={'configuration_id': request.configuration.id.configuration_id})


def create_return_configured_target(request):
    return configured_target_pb2.ConfiguredTarget(
        name="invocations/{}/targets/{}/configuredTargets/{}".format(
            request.configured_target.id.invocation_id,
            request.configured_target.id.target_id,
            request.configured_target.id.configuration_id),
        id={
            'configuration_id': request.configured_target.id.configuration_id,
            'target_id': request.configured_target.id.target_id,
            'invocation_id': request.configured_target.id.invocation_id
        })


def create_return_action(request):
    return action_pb2.Action(
        name="invocations/{}/targets/{}/configuredTargets/{}/actions/{}".
        format(request.action.id.invocation_id, request.action.id.target_id,
               request.action.id.configuration_id,
               request.action.id.action_id),
        id={
            'configuration_id': request.action.id.configuration_id,
            'target_id': request.action.id.target_id,
            'invocation_id': request.action.id.invocation_id,
            'action_id': request.action.id.action_id
        })


def create_finalized_configured_target(request):
    split_name = request.name.split('/')
    return configured_target_pb2.ConfiguredTarget(name=request.name,
                                                  id={
                                                      "invocation_id":
                                                      split_name[1],
                                                      "target_id":
                                                      split_name[3],
                                                      "configuration_id":
                                                      split_name[5]
                                                  })


def create_finalized_target(request):
    split_name = request.name.split('/')
    return target_pb2.Target(name=request.name,
                             id={
                                 "invocation_id": split_name[1],
                                 "target_id": split_name[3],
                             })


def initialize_client(flags, credentials=MagicMock()):
    flags.authorization_token = ''
    credentials.get_active_channel = MagicMock(return_value=None)
    return ResultStoreClient(credentials, flags)
