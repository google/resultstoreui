import grpc
import uuid
import logging
import os
import time
from google import auth
from google.protobuf import (duration_pb2)
from resultstoreapi.cloud.devtools.resultstore_v2.proto import (
    resultstore_upload_pb2_grpc, resultstore_upload_pb2,
    resultstore_download_pb2_grpc, resultstore_download_pb2, invocation_pb2,
    invocation_pb2_grpc, action_pb2, common_pb2, configured_target_pb2,
    target_pb2)
from resultstoreui_utils import (get_default_invocation,
                                 get_default_configuration, gen_new_uuid,
                                 get_parent, get_default_target,
                                 get_default_configured_target,
                                 get_default_action, get_name)
from bigstore_client import BigStoreClient
from collections import defaultdict

_LOGGER = logging.getLogger(__name__)
_LOGGER.setLevel(logging.INFO)

_FIELD_MASK_HEADER = 'x-goog-fieldmask'

RESOURCE_TYPES = defaultdict()


class Error(Exception):
    """Generic Exception class for this module."""


class ResultStoreClient(object):
    """Client for ResultStore v2"""
    def __init__(self, credentials, flags):
        """
        Initialize the ResultStore Client
        
        Args:
            credentials (Credentials): Credentials used to make gRPCS calls
            flags (absl.flags): Various flags defined in resultstoreui.py
        """
        self.credentials = credentials
        self.flags = flags
        self.authorization_token = self.get_authorization_token()

    def create_upload_request(self,
                              resources,
                              target_id=None,
                              config_id=None,
                              action_id=None):
        """
        Create upload requests based on resource type
        
        Args:
            resource (One of Target/ConfiguredTarget/Action/Configuration): Resource to be uploaded
            resource_type (str): Type of resource to create an upload request for
            target_id (str): Id of target to be uploaded
            config_id (str): Id of config to be uploaded
            action_id (str): Id of action to be uploaded

        Returns:
            Upload Request
        """
        request = resultstore_upload_pb2.UploadRequest(
            id={
                'target_id': target_id,
                'configuration_id': config_id,
                'action_id': action_id
            },
            target=resources.get('target'),
            action=resources.get('action'),
            configuration=resources.get('configuration'),
            configured_target=resources.get('configured_target'),
            upload_operation=resultstore_upload_pb2.UploadRequest.CREATE)
        return request

    def get_authorization_token(self):
        """
        Generates an authoirzation token if the user does not specify one via
        the --authorization_token flag

        Returns:
            An authorization token
        """
        if not self.flags.authorization_token:
            authorization_token = gen_new_uuid()
            _LOGGER.error('Your auth token is: %s', authorization_token)
            return authorization_token
        return self.flags.authorization_token

    def get_invocation(self, invocation_name, metadata=None):
        """
        Get a resultstore invocation by name

        Args:
            invocation_name (str): The name of the invocation to get
            metadata (Sequence[Tuple[str, str]]): Metadata param for the grpc call
        Returns:
            The response or error from the ResultStore v2 gRPC Stub Call
        """
        stub = resultstore_download_pb2_grpc.ResultStoreDownloadStub(
            self.credentials.get_active_channel())
        if not metadata:
            metadata = [(_FIELD_MASK_HEADER, 'name')]
        request = resultstore_download_pb2.GetInvocationRequest(
            name=invocation_name)
        try:
            response = stub.GetInvocation(request, metadata=metadata)
        except grpc.RpcError as rpc_error:
            _LOGGER.error('Received error: %s', rpc_error)
            return rpc_error
        else:
            _LOGGER.info('Received message: %s', response)
            return response

    def create_invocation(self):
        """
        Create a resultstore invocation

        Args:
            resume_token (bytes): Initial resume token to put the invocation into batch mode

        Returns:
            The response or error from the ResultStore v2 gRPC Stub Call
        """
        request_id = gen_new_uuid()
        invocation = get_default_invocation()
        stub = resultstore_upload_pb2_grpc.ResultStoreUploadStub(
            self.credentials.get_active_channel())
        request = resultstore_upload_pb2.CreateInvocationRequest(
            request_id=request_id,
            authorization_token=self.authorization_token,
            invocation=invocation,
            )
        request.invocation.CopyFrom(invocation)
        request.invocation_id = invocation.id.invocation_id
        try:
            response = stub.CreateInvocation(request)
        except grpc.RpcError as rpc_error:
            _LOGGER.error('Received error: %s', rpc_error)
            return rpc_error
        else:
            _LOGGER.info('Received message: %s', response)
            return response

    def create_configuration(self, config):
        """
        Create a resultstore invocation configuration

        Args:
            config (google.devtools.resultstore.v2.Configuration): The configuration to create

        Returns:
            The response or error from the ResultStore v2 gRPC Stub Call
        """
        stub = resultstore_upload_pb2_grpc.ResultStoreUploadStub(
            self.credentials.get_active_channel())
        request = resultstore_upload_pb2.CreateConfigurationRequest(
            request_id=gen_new_uuid(),
            authorization_token=self.authorization_token,
            parent=get_parent(config),
            config_id=config.id.configuration_id)
        request.configuration.CopyFrom(config)
        try:
            response = stub.CreateConfiguration(request)
        except grpc.RpcError as rpc_error:
            _LOGGER.error('Received error: %s', rpc_error)
            return rpc_error
        else:
            _LOGGER.info('Received message: %s', response)
            return response

    def create_target(self, target):
        """
        Create a resultstore invocation target

        Args:
            target (google.devtools.resultstore.v2.Target): The target to create

        Returns:
            The response or error from the ResultStore v2 gRPC Stub Call
        """
        stub = resultstore_upload_pb2_grpc.ResultStoreUploadStub(
            self.credentials.get_active_channel())
        request = resultstore_upload_pb2.CreateTargetRequest(
            request_id=gen_new_uuid(),
            authorization_token=self.authorization_token,
            parent=get_parent(target),
            target_id=target.id.target_id)
        request.target.CopyFrom(target)
        try:
            response = stub.CreateTarget(request)
        except grpc.RpcError as rpc_error:
            _LOGGER.error('Received error: %s', rpc_error)
            return rpc_error
        else:
            _LOGGER.info('Received message: %s', response)
            return response

    def create_configured_target(self, config_target, parent=None):
        """
        Create a resultstore invocation target

        Args:
            config_target (google.devtools.resultstore.v2.Target): The ConfiguredTarget to create
            parent (str): The name of the parent resource of the ConfiguredTarget to create

        Returns:
            The response or error from the ResultStore v2 gRPC Stub Call
        """
        stub = resultstore_upload_pb2_grpc.ResultStoreUploadStub(
            self.credentials.get_active_channel())
        request = resultstore_upload_pb2.CreateConfiguredTargetRequest(
            request_id=gen_new_uuid(),
            authorization_token=self.authorization_token,
            config_id=config_target.id.configuration_id)
        request.configured_target.CopyFrom(config_target)
        if parent is not None:
            request.parent = parent
            request.configured_target.ClearField('id')
        else:
            request.parent = get_parent(config_target)
        try:
            response = stub.CreateConfiguredTarget(request)
        except grpc.RpcError as rpc_error:
            _LOGGER.error('Received error: %s', rpc_error)
            return rpc_error
        else:
            _LOGGER.info('Received message: %s', response)
            return response

    def create_action(self, action, parent=None):
        """
        Create a resultstore invocation configured target action

        Args:
            action (google.devtools.resultstore.v2.Action): The Action to create
            parent (str): The name of the parent resource of the Action to create

        Returns:
            The response or error from the ResultStore v2 gRPC Stub Call
        """
        stub = resultstore_upload_pb2_grpc.ResultStoreUploadStub(
            self.credentials.get_active_channel())
        request = resultstore_upload_pb2.CreateActionRequest(
            request_id=gen_new_uuid(),
            authorization_token=self.authorization_token,
            action_id=action.id.action_id,
        )
        request.action.CopyFrom(action)
        if parent is not None:
            request.parent = parent
            request.action.ClearField('id')
        else:
            request.parent = get_parent(action)
        try:
            response = stub.CreateAction(request)
        except grpc.RpcError as rpc_error:
            _LOGGER.error('Received error: %s', rpc_error)
            return rpc_error
        else:
            _LOGGER.info('Received message: %s', response)
            return response

    def update_action(self, action, update_fields):
        """
        Update a resultstore invocation configured target action

        Args:
            action (google.devtools.resultstore.v2.Action): The Action to update
            update_fields (Sequence[str]): The list of paths specifying which fields to update

        Returns:
            The response or error from the ResultStore v2 gRPC Stub Call
        """
        if not update_fields:
            raise Error('At least one update field must be provided.')
        stub = resultstore_upload_pb2_grpc.ResultStoreUploadStub(
            self.credentials.get_active_channel())
        request = resultstore_upload_pb2.UpdateActionRequest(
            authorization_token=self.authorization_token)
        request.action.CopyFrom(action)
        request.update_mask.paths.extend(update_fields)
        try:
            response = stub.UpdateAction(request)
        except grpc.RpcError as rpc_error:
            _LOGGER.error('Received error: %s', rpc_error)
            return rpc_error
        else:
            _LOGGER.info('Received message: %s', response)
            return response

    def update_configured_target(self, config_target, update_fields):
        """
        Update a resultstore invocation configured target

        Args:
            config_target (google.devtools.resultstore.v2.ConfiguredTarget): The ConfiguredTarget
                to update
            update_fields (Sequence[str]): The list of paths specifying which fields to update

        Returns:
            The response or error from the ResultStore v2 gRPC Stub Call
        """
        if not update_fields:
            raise Error('At least one update field must be provided.')
        stub = resultstore_upload_pb2_grpc.ResultStoreUploadStub(
            self.credentials.get_active_channel())
        request = resultstore_upload_pb2.UpdateConfiguredTargetRequest(
            authorization_token=self.authorization_token)
        request.configured_target.CopyFrom(config_target)
        request.update_mask.paths.extend(update_fields)
        try:
            response = stub.UpdateConfiguredTarget(request)
        except grpc.RpcError as rpc_error:
            _LOGGER.error('Received error: %s', rpc_error)
            return rpc_error
        else:
            _LOGGER.info('Received message: %s', response)
            return response

    def update_target(self, target, update_fields):
        """
        Update a resultstore invocation target

        Args:
            target (google.devtools.resultstore.v2.Target): The Target
                to update
            update_fields (Sequence[str]): The list of paths specifying which fields to update

        Returns:
            The response or error from the ResultStore v2 gRPC Stub Call

        Raises:
            Error: If no update fields are provided
        """
        if not update_fields:
            raise Error('At least one update field must be provided.')
        stub = resultstore_upload_pb2_grpc.ResultStoreUploadStub(
            self.credentials.get_active_channel())
        request = resultstore_upload_pb2.UpdateTargetRequest(
            authorization_token=self.authorization_token)
        request.target.CopyFrom(target)
        request.update_mask.paths.extend(update_fields)
        try:
            response = stub.UpdateTarget(request)
        except grpc.RpcError as rpc_error:
            _LOGGER.error('Received error: %s', rpc_error)
            return rpc_error
        else:
            _LOGGER.info('Received message: %s', response)
            return response

    def finalize_configured_target(self, invocation_id, target_id, config_id):
        """
        Finalize a resultstore invocation configured target

        Args:
            invocation_id (str): The invocation id for the configured target to finalize
            target_id (str): The target id for the configured target to finalize
            config_id (str): The confugration id for the configured target to finalize

        Returns:
            The response or error from the ResultStore v2 gRPC Stub Call
        """
        stub = resultstore_upload_pb2_grpc.ResultStoreUploadStub(
            self.credentials.get_active_channel())
        request = resultstore_upload_pb2.FinalizeConfiguredTargetRequest(
            authorization_token=self.authorization_token,
            name=get_name(invocation_id, target_id, config_id))
        try:
            response = stub.FinalizeConfiguredTarget(request)
        except grpc.RpcError as rpc_error:
            _LOGGER.error('Received error: %s', rpc_error)
            return rpc_error
        else:
            _LOGGER.info('Received message: %s', response)
            return response

    def finalize_target(self, invocation_id, target_id):
        """
        Finalize a resultstore invocation target

        Args:
            invocation_id (str): The invocation id for the target to finalize
            target_id (str): The id of the target to finalize

        Returns:
            The response or error from the ResultStore v2 gRPC Stub Call
        """
        stub = resultstore_upload_pb2_grpc.ResultStoreUploadStub(
            self.credentials.get_active_channel())
        request = resultstore_upload_pb2.FinalizeTargetRequest(
            authorization_token=self.authorization_token,
            name=get_name(invocation_id, target_id))
        try:
            response = stub.FinalizeTarget(request)
        except grpc.RpcError as rpc_error:
            _LOGGER.error('Received error: %s', rpc_error)
            return rpc_error
        else:
            _LOGGER.info('Received message: %s', response)
            return response

    def create_resource_requests(self, invocation_id, config_id):
        """
        Create upload requests to be batch uploaded

        Args:
            invocation_id (str): Invocation to upload to
            config_id (str): Invocation configuration id to use or create
        
        Returns:
            A list of upload requests
        """
        requests = []
        if self.flags.create_config:
            config = get_default_configuration(invocation_id)
            config_request = self.create_upload_request(
                defaultdict(None, {'configuration': config}),
                config_id=config.id.configuration_id)
            requests.append(config_request)
        target = get_default_target(invocation_id)
        target_id = target.id.target_id
        target_request = self.create_upload_request(
            defaultdict(None, {'target': target}), target_id)
        files = None
        if self.flags.files:
            files = self._upload_files(target_id)
        requests.append(target_request)
        config_target = get_default_configured_target(invocation_id, target_id,
                                                      config_id)
        config_target_request = self.create_upload_request(
            defaultdict(None, {'configured_target': config_target}), target_id,
            config_id)
        requests.append(config_target_request)
        action = get_default_action(invocation_id,
                                    target_id,
                                    config_id,
                                    files=files)
        action_id = action.id.action_id
        action_request = self.create_upload_request(
            defaultdict(None, {'action': action}), target_id, config_id,
            action_id)
        requests.append(action_request)
        return requests

    def finalize_batch_upload(self, resume_token, next_resume_token,
                              invocation_id):
        """
        Finalize an invocation that was in batch mode

        Args:
            resume_token (bytes): Current resume token
            next_resume_token (bytes): Next resume token
            invocation_id (str): Invocation ID to be finalized
        """
        invocation = get_default_invocation(invocation_id)
        finalize_invocation_request = resultstore_upload_pb2.UploadRequest(
            invocation=invocation,
            upload_operation=(resultstore_upload_pb2.UploadRequest.FINALIZE))
        self.batch_upload(resume_token, next_resume_token, invocation_id,
                          [finalize_invocation_request])

    def batch_upload(self, resume_token, next_resume_token, invocation_id,
                     upload_requests):
        """
        Batch upload the provided upload_requests to the invocation

        Args:
            resume_token (bytes): Current resume token
            next_resume_token (bytes): Next resume token
            invocation_id (str): Invocation ID to upload to
            upload_requests (Sequence[UploadRequest]): List of UploadRequests to be uploaded

        Returns:
            The response or error from the ResultStore v2 gRPC Stub Call
        """
        invocation_name = 'invocations/' + invocation_id
        stub = resultstore_upload_pb2_grpc.ResultStoreUploadStub(
            self.credentials.get_active_channel())
        request = resultstore_upload_pb2.UploadBatchRequest(
            parent=invocation_name,
            resume_token=resume_token,
            next_resume_token=next_resume_token,
            authorization_token=self.authorization_token)
        request.upload_requests.extend(upload_requests)

        try:
            response = stub.UploadBatch(request)
        except grpc.RpcError as rpc_error:
            _LOGGER.error('Received error: %s', rpc_error)
            return rpc_error
        else:
            _LOGGER.info('Received message: %s', response)
            return response

    def batch_upload_wrapper(self, resume_token, next_resume_token):
        """
        Batch upload to a given invocation

        Args:
            resume_token (bytes): Current resume token
            next_resume_token (bytes): Next resume token
        """
        batched_requests = self.create_resource_requests(
            self.flags.invocation_id, self.flags.config_id)
        self.batch_upload(resume_token, next_resume_token,
                          self.flags.invocation_id, batched_requests)

    def single_upload(self):
        """
        Uploads a single invocation to resultstore
        """

        config_id = self.flags.config_id
        config = get_default_configuration(self.flags.invocation_id, config_id)
        self.create_configuration(config)
        config_id = config.id.configuration_id
        target = get_default_target(self.flags.invocation_id,
                                    self.flags.target_name)
        self.create_target(target)
        target_id = target.id.target_id
        config_target = get_default_configured_target(self.flags.invocation_id,
                                                      target_id, config_id)
        self.create_configured_target(config_target)
        action = get_default_action(self.flags.invocation_id, target_id,
                                    config_id)
        if self.flags.action_type == 'Test':
            test_action = action_pb2.TestAction()
            action.test_action.CopyFrom(test_action)
        else:
            build_action = action_pb2.BuildAction()
            action.build_action.CopyFrom(build_action)
        self.create_action(action)
        self._file_upload_helper(target_id, action.id.action_id, config_id)
        self.finalize_configured_target(self.flags.invocation_id, target_id,
                                        config_id)
        self.finalize_target(self.flags.invocation_id, target_id)

    def _file_upload_helper(self, target_id, action_id, config_id):
        """
        Uploads files specified by the --files flag to the given target

        Args:
            target_id (str): Id of the target to update
            action_id (str): Id of the action to update
            config_id (str): Id of the config to be updated
        """
        result_status = common_pb2.Status.Value(self.flags.status)
        start_time = time.time()
        additional_files = self._upload_files(target_id)
        end_time = time.time()
        duration_seconds = int(end_time - start_time)
        duration = duration_pb2.Duration(seconds=duration_seconds)
        new_action = action_pb2.Action(
            name=get_name(self.flags.invocation_id, target_id, config_id,
                          action_id),
            timing=common_pb2.Timing(duration=duration),
            status_attributes=common_pb2.StatusAttributes(
                status=result_status),
            files=additional_files)
        self.update_action(new_action,
                           ['timing.duration', 'status_attributes', 'files'])
        new_config_target = configured_target_pb2.ConfiguredTarget(
            name=get_name(self.flags.invocation_id, target_id, config_id),
            timing=common_pb2.Timing(duration=duration))
        self.update_configured_target(new_config_target,
                                      ['timing.duration', 'status_attributes'])
        new_target = target_pb2.Target(
            name=get_name(self.flags.invocation_id, target_id),
            timing=common_pb2.Timing(duration=duration))
        self.update_target(new_target,
                           ['timing.duration', 'status_attributes'])

    def _upload_files(self, target_id):
        """
        Uploads files to bigstore at the given target_id

        Args:
            target_id (str): Target for files to be associated with

        Returns:
            uploaded_files: A list of file_pb2.File() objects
        """
        storage_dir = '{}/{}/'.format(self.flags.invocation_id, target_id)
        bigstore_client = BigStoreClient(self.credentials,
                                         self.flags.bigstore_project_name,
                                         storage_dir, self.flags.bucket_name)
        additional_files = bigstore_client.upload_files_to_bigstore(
            self.flags.files)
        return additional_files
