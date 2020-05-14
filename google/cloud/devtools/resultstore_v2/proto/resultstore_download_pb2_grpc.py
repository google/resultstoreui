# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

from google.cloud.devtools.resultstore_v2.proto import action_pb2 as google_dot_cloud_dot_devtools_dot_resultstore__v2_dot_proto_dot_action__pb2
from google.cloud.devtools.resultstore_v2.proto import configuration_pb2 as google_dot_cloud_dot_devtools_dot_resultstore__v2_dot_proto_dot_configuration__pb2
from google.cloud.devtools.resultstore_v2.proto import configured_target_pb2 as google_dot_cloud_dot_devtools_dot_resultstore__v2_dot_proto_dot_configured__target__pb2
from google.cloud.devtools.resultstore_v2.proto import download_metadata_pb2 as google_dot_cloud_dot_devtools_dot_resultstore__v2_dot_proto_dot_download__metadata__pb2
from google.cloud.devtools.resultstore_v2.proto import file_set_pb2 as google_dot_cloud_dot_devtools_dot_resultstore__v2_dot_proto_dot_file__set__pb2
from google.cloud.devtools.resultstore_v2.proto import invocation_pb2 as google_dot_cloud_dot_devtools_dot_resultstore__v2_dot_proto_dot_invocation__pb2
from google.cloud.devtools.resultstore_v2.proto import resultstore_download_pb2 as google_dot_cloud_dot_devtools_dot_resultstore__v2_dot_proto_dot_resultstore__download__pb2
from google.cloud.devtools.resultstore_v2.proto import target_pb2 as google_dot_cloud_dot_devtools_dot_resultstore__v2_dot_proto_dot_target__pb2


class ResultStoreDownloadStub(object):
  """This is the interface used to download information from the ResultStore
  database.

  Most APIs require setting a response FieldMask via the 'fields' URL query
  parameter or the X-Goog-FieldMask HTTP/gRPC header.
  """

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.GetInvocation = channel.unary_unary(
        '/google.devtools.resultstore.v2.ResultStoreDownload/GetInvocation',
        request_serializer=google_dot_cloud_dot_devtools_dot_resultstore__v2_dot_proto_dot_resultstore__download__pb2.GetInvocationRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_devtools_dot_resultstore__v2_dot_proto_dot_invocation__pb2.Invocation.FromString,
        )
    self.SearchInvocations = channel.unary_unary(
        '/google.devtools.resultstore.v2.ResultStoreDownload/SearchInvocations',
        request_serializer=google_dot_cloud_dot_devtools_dot_resultstore__v2_dot_proto_dot_resultstore__download__pb2.SearchInvocationsRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_devtools_dot_resultstore__v2_dot_proto_dot_resultstore__download__pb2.SearchInvocationsResponse.FromString,
        )
    self.GetInvocationDownloadMetadata = channel.unary_unary(
        '/google.devtools.resultstore.v2.ResultStoreDownload/GetInvocationDownloadMetadata',
        request_serializer=google_dot_cloud_dot_devtools_dot_resultstore__v2_dot_proto_dot_resultstore__download__pb2.GetInvocationDownloadMetadataRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_devtools_dot_resultstore__v2_dot_proto_dot_download__metadata__pb2.DownloadMetadata.FromString,
        )
    self.GetConfiguration = channel.unary_unary(
        '/google.devtools.resultstore.v2.ResultStoreDownload/GetConfiguration',
        request_serializer=google_dot_cloud_dot_devtools_dot_resultstore__v2_dot_proto_dot_resultstore__download__pb2.GetConfigurationRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_devtools_dot_resultstore__v2_dot_proto_dot_configuration__pb2.Configuration.FromString,
        )
    self.ListConfigurations = channel.unary_unary(
        '/google.devtools.resultstore.v2.ResultStoreDownload/ListConfigurations',
        request_serializer=google_dot_cloud_dot_devtools_dot_resultstore__v2_dot_proto_dot_resultstore__download__pb2.ListConfigurationsRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_devtools_dot_resultstore__v2_dot_proto_dot_resultstore__download__pb2.ListConfigurationsResponse.FromString,
        )
    self.GetTarget = channel.unary_unary(
        '/google.devtools.resultstore.v2.ResultStoreDownload/GetTarget',
        request_serializer=google_dot_cloud_dot_devtools_dot_resultstore__v2_dot_proto_dot_resultstore__download__pb2.GetTargetRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_devtools_dot_resultstore__v2_dot_proto_dot_target__pb2.Target.FromString,
        )
    self.ListTargets = channel.unary_unary(
        '/google.devtools.resultstore.v2.ResultStoreDownload/ListTargets',
        request_serializer=google_dot_cloud_dot_devtools_dot_resultstore__v2_dot_proto_dot_resultstore__download__pb2.ListTargetsRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_devtools_dot_resultstore__v2_dot_proto_dot_resultstore__download__pb2.ListTargetsResponse.FromString,
        )
    self.GetConfiguredTarget = channel.unary_unary(
        '/google.devtools.resultstore.v2.ResultStoreDownload/GetConfiguredTarget',
        request_serializer=google_dot_cloud_dot_devtools_dot_resultstore__v2_dot_proto_dot_resultstore__download__pb2.GetConfiguredTargetRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_devtools_dot_resultstore__v2_dot_proto_dot_configured__target__pb2.ConfiguredTarget.FromString,
        )
    self.ListConfiguredTargets = channel.unary_unary(
        '/google.devtools.resultstore.v2.ResultStoreDownload/ListConfiguredTargets',
        request_serializer=google_dot_cloud_dot_devtools_dot_resultstore__v2_dot_proto_dot_resultstore__download__pb2.ListConfiguredTargetsRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_devtools_dot_resultstore__v2_dot_proto_dot_resultstore__download__pb2.ListConfiguredTargetsResponse.FromString,
        )
    self.GetAction = channel.unary_unary(
        '/google.devtools.resultstore.v2.ResultStoreDownload/GetAction',
        request_serializer=google_dot_cloud_dot_devtools_dot_resultstore__v2_dot_proto_dot_resultstore__download__pb2.GetActionRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_devtools_dot_resultstore__v2_dot_proto_dot_action__pb2.Action.FromString,
        )
    self.ListActions = channel.unary_unary(
        '/google.devtools.resultstore.v2.ResultStoreDownload/ListActions',
        request_serializer=google_dot_cloud_dot_devtools_dot_resultstore__v2_dot_proto_dot_resultstore__download__pb2.ListActionsRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_devtools_dot_resultstore__v2_dot_proto_dot_resultstore__download__pb2.ListActionsResponse.FromString,
        )
    self.GetFileSet = channel.unary_unary(
        '/google.devtools.resultstore.v2.ResultStoreDownload/GetFileSet',
        request_serializer=google_dot_cloud_dot_devtools_dot_resultstore__v2_dot_proto_dot_resultstore__download__pb2.GetFileSetRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_devtools_dot_resultstore__v2_dot_proto_dot_file__set__pb2.FileSet.FromString,
        )
    self.ListFileSets = channel.unary_unary(
        '/google.devtools.resultstore.v2.ResultStoreDownload/ListFileSets',
        request_serializer=google_dot_cloud_dot_devtools_dot_resultstore__v2_dot_proto_dot_resultstore__download__pb2.ListFileSetsRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_devtools_dot_resultstore__v2_dot_proto_dot_resultstore__download__pb2.ListFileSetsResponse.FromString,
        )
    self.TraverseFileSets = channel.unary_unary(
        '/google.devtools.resultstore.v2.ResultStoreDownload/TraverseFileSets',
        request_serializer=google_dot_cloud_dot_devtools_dot_resultstore__v2_dot_proto_dot_resultstore__download__pb2.TraverseFileSetsRequest.SerializeToString,
        response_deserializer=google_dot_cloud_dot_devtools_dot_resultstore__v2_dot_proto_dot_resultstore__download__pb2.TraverseFileSetsResponse.FromString,
        )


class ResultStoreDownloadServicer(object):
  """This is the interface used to download information from the ResultStore
  database.

  Most APIs require setting a response FieldMask via the 'fields' URL query
  parameter or the X-Goog-FieldMask HTTP/gRPC header.
  """

  def GetInvocation(self, request, context):
    """Retrieves the invocation with the given name.

    An error will be reported in the following cases:
    - If the invocation is not found.
    - If the given invocation name is badly formatted.
    - If no field mask was given.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def SearchInvocations(self, request, context):
    """Searches for invocations matching the given query parameters. Results will
    be ordered by timing.start_time with most recent first, but total ordering
    of results is not guaranteed when difference in timestamps is very small.
    Results may be stale.


    An error will be reported in the following cases:
    - If a query string is not provided
    - If no field mask was given.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetInvocationDownloadMetadata(self, request, context):
    """Retrieves the metadata for an invocation with the given name.

    An error will be reported in the following cases:
    - If the invocation is not found.
    - If the given invocation name is badly formatted.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetConfiguration(self, request, context):
    """Retrieves the configuration with the given name.

    An error will be reported in the following cases:
    - If the configuration or its parent invocation is not found.
    - If the given configuration name is badly formatted.
    - If no field mask was given.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListConfigurations(self, request, context):
    """Retrieves all configurations for a parent invocation.
    This might be limited by user or server,
    in which case a continuation token is provided.
    The order in which results are returned is undefined, but stable.

    An error will be reported in the following cases:
    - If the parent invocation is not found.
    - If the given parent invocation name is badly formatted.
    - If no field mask was given.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetTarget(self, request, context):
    """Retrieves the target with the given name.

    An error will be reported in the following cases:
    - If the target or its parent invocation is not found.
    - If the given target name is badly formatted.
    - If no field mask was given.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListTargets(self, request, context):
    """Retrieves all targets for a parent invocation.  This might be limited by
    user or server, in which case a continuation token is provided.
    The order in which results are returned is undefined, but stable.

    An error will be reported in the following cases:
    - If the parent is not found.
    - If the given parent name is badly formatted.
    - If no field mask was given.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetConfiguredTarget(self, request, context):
    """Retrieves the configured target with the given name.

    An error will be reported in the following cases:
    - If the configured target is not found.
    - If the given name is badly formatted.
    - If no field mask was given.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListConfiguredTargets(self, request, context):
    """Retrieves all configured targets for a parent invocation/target.
    This might be limited by user or server, in which case a continuation
    token is provided.  Supports '-' for targetId meaning all targets.
    The order in which results are returned is undefined, but stable.

    An error will be reported in the following cases:
    - If the parent is not found.
    - If the given parent name is badly formatted.
    - If no field mask was given.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetAction(self, request, context):
    """Retrieves the action with the given name.

    An error will be reported in the following cases:
    - If the action is not found.
    - If the given name is badly formatted.
    - If no field mask was given.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListActions(self, request, context):
    """Retrieves all actions for a parent invocation/target/configuration.
    This might be limited by user or server, in which case a continuation
    token is provided.  Supports '-' for configurationId to mean all
    actions for all configurations for a target, or '-' for targetId and
    configurationId to mean all actions for all configurations and all targets.
    Does not support targetId '-' with a specified configuration.
    The order in which results are returned is undefined, but stable.

    An error will be reported in the following cases:
    - If the parent is not found.
    - If the given parent name is badly formatted.
    - If no field mask was given.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def GetFileSet(self, request, context):
    """Retrieves the file set with the given name.

    An error will be reported in the following cases:
    - If the file set or its parent invocation is not found.
    - If the given file set name is badly formatted.
    - If no field mask was given.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def ListFileSets(self, request, context):
    """Retrieves all file sets for a parent invocation.
    This might be limited by user or server,
    in which case a continuation token is provided.
    The order in which results are returned is undefined, but stable.

    An error will be reported in the following cases:
    - If the parent invocation is not found.
    - If the given parent invocation name is badly formatted.
    - If no field mask was given.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def TraverseFileSets(self, request, context):
    """Returns the transitive closure of FileSets. This might be limited by user
    or server, in which case a continuation token is provided.
    The order in which results are returned is undefined, and unstable.

    An error will be reported in the following cases:
    - If page_token is too large to continue the calculation.
    - If the resource is not found.
    - If the given resource name is badly formatted.
    - If no field mask was given.
    """
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ResultStoreDownloadServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'GetInvocation': grpc.unary_unary_rpc_method_handler(
          servicer.GetInvocation,
          request_deserializer=google_dot_cloud_dot_devtools_dot_resultstore__v2_dot_proto_dot_resultstore__download__pb2.GetInvocationRequest.FromString,
          response_serializer=google_dot_cloud_dot_devtools_dot_resultstore__v2_dot_proto_dot_invocation__pb2.Invocation.SerializeToString,
      ),
      'SearchInvocations': grpc.unary_unary_rpc_method_handler(
          servicer.SearchInvocations,
          request_deserializer=google_dot_cloud_dot_devtools_dot_resultstore__v2_dot_proto_dot_resultstore__download__pb2.SearchInvocationsRequest.FromString,
          response_serializer=google_dot_cloud_dot_devtools_dot_resultstore__v2_dot_proto_dot_resultstore__download__pb2.SearchInvocationsResponse.SerializeToString,
      ),
      'GetInvocationDownloadMetadata': grpc.unary_unary_rpc_method_handler(
          servicer.GetInvocationDownloadMetadata,
          request_deserializer=google_dot_cloud_dot_devtools_dot_resultstore__v2_dot_proto_dot_resultstore__download__pb2.GetInvocationDownloadMetadataRequest.FromString,
          response_serializer=google_dot_cloud_dot_devtools_dot_resultstore__v2_dot_proto_dot_download__metadata__pb2.DownloadMetadata.SerializeToString,
      ),
      'GetConfiguration': grpc.unary_unary_rpc_method_handler(
          servicer.GetConfiguration,
          request_deserializer=google_dot_cloud_dot_devtools_dot_resultstore__v2_dot_proto_dot_resultstore__download__pb2.GetConfigurationRequest.FromString,
          response_serializer=google_dot_cloud_dot_devtools_dot_resultstore__v2_dot_proto_dot_configuration__pb2.Configuration.SerializeToString,
      ),
      'ListConfigurations': grpc.unary_unary_rpc_method_handler(
          servicer.ListConfigurations,
          request_deserializer=google_dot_cloud_dot_devtools_dot_resultstore__v2_dot_proto_dot_resultstore__download__pb2.ListConfigurationsRequest.FromString,
          response_serializer=google_dot_cloud_dot_devtools_dot_resultstore__v2_dot_proto_dot_resultstore__download__pb2.ListConfigurationsResponse.SerializeToString,
      ),
      'GetTarget': grpc.unary_unary_rpc_method_handler(
          servicer.GetTarget,
          request_deserializer=google_dot_cloud_dot_devtools_dot_resultstore__v2_dot_proto_dot_resultstore__download__pb2.GetTargetRequest.FromString,
          response_serializer=google_dot_cloud_dot_devtools_dot_resultstore__v2_dot_proto_dot_target__pb2.Target.SerializeToString,
      ),
      'ListTargets': grpc.unary_unary_rpc_method_handler(
          servicer.ListTargets,
          request_deserializer=google_dot_cloud_dot_devtools_dot_resultstore__v2_dot_proto_dot_resultstore__download__pb2.ListTargetsRequest.FromString,
          response_serializer=google_dot_cloud_dot_devtools_dot_resultstore__v2_dot_proto_dot_resultstore__download__pb2.ListTargetsResponse.SerializeToString,
      ),
      'GetConfiguredTarget': grpc.unary_unary_rpc_method_handler(
          servicer.GetConfiguredTarget,
          request_deserializer=google_dot_cloud_dot_devtools_dot_resultstore__v2_dot_proto_dot_resultstore__download__pb2.GetConfiguredTargetRequest.FromString,
          response_serializer=google_dot_cloud_dot_devtools_dot_resultstore__v2_dot_proto_dot_configured__target__pb2.ConfiguredTarget.SerializeToString,
      ),
      'ListConfiguredTargets': grpc.unary_unary_rpc_method_handler(
          servicer.ListConfiguredTargets,
          request_deserializer=google_dot_cloud_dot_devtools_dot_resultstore__v2_dot_proto_dot_resultstore__download__pb2.ListConfiguredTargetsRequest.FromString,
          response_serializer=google_dot_cloud_dot_devtools_dot_resultstore__v2_dot_proto_dot_resultstore__download__pb2.ListConfiguredTargetsResponse.SerializeToString,
      ),
      'GetAction': grpc.unary_unary_rpc_method_handler(
          servicer.GetAction,
          request_deserializer=google_dot_cloud_dot_devtools_dot_resultstore__v2_dot_proto_dot_resultstore__download__pb2.GetActionRequest.FromString,
          response_serializer=google_dot_cloud_dot_devtools_dot_resultstore__v2_dot_proto_dot_action__pb2.Action.SerializeToString,
      ),
      'ListActions': grpc.unary_unary_rpc_method_handler(
          servicer.ListActions,
          request_deserializer=google_dot_cloud_dot_devtools_dot_resultstore__v2_dot_proto_dot_resultstore__download__pb2.ListActionsRequest.FromString,
          response_serializer=google_dot_cloud_dot_devtools_dot_resultstore__v2_dot_proto_dot_resultstore__download__pb2.ListActionsResponse.SerializeToString,
      ),
      'GetFileSet': grpc.unary_unary_rpc_method_handler(
          servicer.GetFileSet,
          request_deserializer=google_dot_cloud_dot_devtools_dot_resultstore__v2_dot_proto_dot_resultstore__download__pb2.GetFileSetRequest.FromString,
          response_serializer=google_dot_cloud_dot_devtools_dot_resultstore__v2_dot_proto_dot_file__set__pb2.FileSet.SerializeToString,
      ),
      'ListFileSets': grpc.unary_unary_rpc_method_handler(
          servicer.ListFileSets,
          request_deserializer=google_dot_cloud_dot_devtools_dot_resultstore__v2_dot_proto_dot_resultstore__download__pb2.ListFileSetsRequest.FromString,
          response_serializer=google_dot_cloud_dot_devtools_dot_resultstore__v2_dot_proto_dot_resultstore__download__pb2.ListFileSetsResponse.SerializeToString,
      ),
      'TraverseFileSets': grpc.unary_unary_rpc_method_handler(
          servicer.TraverseFileSets,
          request_deserializer=google_dot_cloud_dot_devtools_dot_resultstore__v2_dot_proto_dot_resultstore__download__pb2.TraverseFileSetsRequest.FromString,
          response_serializer=google_dot_cloud_dot_devtools_dot_resultstore__v2_dot_proto_dot_resultstore__download__pb2.TraverseFileSetsResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'google.devtools.resultstore.v2.ResultStoreDownload', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
