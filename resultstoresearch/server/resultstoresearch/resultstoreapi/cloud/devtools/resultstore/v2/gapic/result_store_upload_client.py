# -*- coding: utf-8 -*-
#
# Copyright 2020 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     https://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Accesses the google.devtools.resultstore.v2 ResultStoreUpload API."""

import pkg_resources
import warnings

from google.oauth2 import service_account
import google.api_core.client_options
import google.api_core.gapic_v1.client_info
import google.api_core.gapic_v1.config
import google.api_core.gapic_v1.method
import google.api_core.gapic_v1.routing_header
import google.api_core.grpc_helpers
import grpc

from google.cloud.devtools.resultstore.v2.gapic import enums
from google.cloud.devtools.resultstore.v2.gapic import result_store_upload_client_config
from google.cloud.devtools.resultstore.v2.gapic.transports import result_store_upload_grpc_transport
from google.cloud.devtools.resultstore.v2.proto import action_pb2
from google.cloud.devtools.resultstore.v2.proto import configuration_pb2
from google.cloud.devtools.resultstore.v2.proto import configured_target_pb2
from google.cloud.devtools.resultstore.v2.proto import download_metadata_pb2
from google.cloud.devtools.resultstore.v2.proto import file_set_pb2
from google.cloud.devtools.resultstore.v2.proto import invocation_pb2
from google.cloud.devtools.resultstore.v2.proto import resultstore_download_pb2
from google.cloud.devtools.resultstore.v2.proto import resultstore_download_pb2_grpc
from google.cloud.devtools.resultstore.v2.proto import resultstore_file_download_pb2
from google.cloud.devtools.resultstore.v2.proto import resultstore_file_download_pb2_grpc
from google.cloud.devtools.resultstore.v2.proto import resultstore_upload_pb2
from google.cloud.devtools.resultstore.v2.proto import resultstore_upload_pb2_grpc
from google.cloud.devtools.resultstore.v2.proto import target_pb2
from google.cloud.devtools.resultstore.v2.proto import upload_metadata_pb2
from google.protobuf import empty_pb2
from google.protobuf import field_mask_pb2
from google.protobuf import timestamp_pb2



_GAPIC_LIBRARY_VERSION = pkg_resources.get_distribution(
    'google-cloud-devtools-resultstore',
).version


class ResultStoreUploadClient(object):
    """
    This is the interface used to upload information to the ResultStore database,
    to update that information as necessary, and to make it immutable at the end.

    This interface intentionally does not support user read-modify-write
    operations. They may corrupt data, and are too expensive. For the same
    reason, all upload RPCs will return no resource fields except name and ID. An
    uploader should hold as little state as possible in memory to avoid running
    out of memory.
    """

    SERVICE_ADDRESS = 'resultstore.googleapis.com:443'
    """The default address of the service."""

    # The name of the interface for this client. This is the key used to
    # find the method configuration in the client_config dictionary.
    _INTERFACE_NAME = 'google.devtools.resultstore.v2.ResultStoreUpload'


    @classmethod
    def from_service_account_file(cls, filename, *args, **kwargs):
        """Creates an instance of this client using the provided credentials
        file.

        Args:
            filename (str): The path to the service account private key json
                file.
            args: Additional arguments to pass to the constructor.
            kwargs: Additional arguments to pass to the constructor.

        Returns:
            ResultStoreUploadClient: The constructed client.
        """
        credentials = service_account.Credentials.from_service_account_file(
            filename)
        kwargs['credentials'] = credentials
        return cls(*args, **kwargs)

    from_service_account_json = from_service_account_file

    def __init__(self, transport=None, channel=None, credentials=None,
            client_config=None, client_info=None, client_options=None):
        """Constructor.

        Args:
            transport (Union[~.ResultStoreUploadGrpcTransport,
                    Callable[[~.Credentials, type], ~.ResultStoreUploadGrpcTransport]): A transport
                instance, responsible for actually making the API calls.
                The default transport uses the gRPC protocol.
                This argument may also be a callable which returns a
                transport instance. Callables will be sent the credentials
                as the first argument and the default transport class as
                the second argument.
            channel (grpc.Channel): DEPRECATED. A ``Channel`` instance
                through which to make calls. This argument is mutually exclusive
                with ``credentials``; providing both will raise an exception.
            credentials (google.auth.credentials.Credentials): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
                This argument is mutually exclusive with providing a
                transport instance to ``transport``; doing so will raise
                an exception.
            client_config (dict): DEPRECATED. A dictionary of call options for
                each method. If not specified, the default configuration is used.
            client_info (google.api_core.gapic_v1.client_info.ClientInfo):
                The client info used to send a user-agent string along with
                API requests. If ``None``, then default info will be used.
                Generally, you only need to set this if you're developing
                your own client library.
            client_options (Union[dict, google.api_core.client_options.ClientOptions]):
                Client options used to set user options on the client. API Endpoint
                should be set through client_options.
        """
        # Raise deprecation warnings for things we want to go away.
        if client_config is not None:
            warnings.warn('The `client_config` argument is deprecated.',
                          PendingDeprecationWarning, stacklevel=2)
        else:
            client_config = result_store_upload_client_config.config

        if channel:
            warnings.warn('The `channel` argument is deprecated; use '
                          '`transport` instead.',
                          PendingDeprecationWarning, stacklevel=2)

        api_endpoint = self.SERVICE_ADDRESS
        if client_options:
            if type(client_options) == dict:
                client_options = google.api_core.client_options.from_dict(client_options)
            if client_options.api_endpoint:
                api_endpoint = client_options.api_endpoint

        # Instantiate the transport.
        # The transport is responsible for handling serialization and
        # deserialization and actually sending data to the service.
        if transport:
            if callable(transport):
                self.transport = transport(
                    credentials=credentials,
                    default_class=result_store_upload_grpc_transport.ResultStoreUploadGrpcTransport,
                    address=api_endpoint,
                )
            else:
                if credentials:
                    raise ValueError(
                        'Received both a transport instance and '
                        'credentials; these are mutually exclusive.'
                    )
                self.transport = transport
        else:
            self.transport = result_store_upload_grpc_transport.ResultStoreUploadGrpcTransport(
                address=api_endpoint,
                channel=channel,
                credentials=credentials,
            )

        if client_info is None:
            client_info = google.api_core.gapic_v1.client_info.ClientInfo(
                gapic_version=_GAPIC_LIBRARY_VERSION,
            )
        else:
            client_info.gapic_version = _GAPIC_LIBRARY_VERSION
        self._client_info = client_info

        # Parse out the default settings for retry and timeout for each RPC
        # from the client configuration.
        # (Ordinarily, these are the defaults specified in the `*_config.py`
        # file next to this one.)
        self._method_configs = google.api_core.gapic_v1.config.parse_method_configs(
            client_config['interfaces'][self._INTERFACE_NAME],
        )

        # Save a dictionary of cached API call functions.
        # These are the actual callables which invoke the proper
        # transport methods, wrapped with `wrap_method` to add retry,
        # timeout, and the like.
        self._inner_api_calls = {}

    # Service calls
    def create_invocation(
            self,
            request_id=None,
            invocation_id=None,
            invocation=None,
            authorization_token=None,
            auto_finalize_time=None,
            initial_resume_token=None,
            uploader_state=None,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Creates the given invocation.

        This is not an implicitly idempotent API, so a request id is required to
        make it idempotent.

        Returns an empty Invocation proto with only the name and ID fields
        populated.

        An error will be reported in the following cases:
        - If an invocation with the same ID already exists.

        Example:
            >>> from google.cloud.devtools.resultstore import v2
            >>>
            >>> client = v2.ResultStoreUploadClient()
            >>>
            >>> response = client.create_invocation()

        Args:
            request_id (str): A unique identifier for this request. Must be set to a different
                value for each request that affects a given resource (eg. a random
                UUID). Required for the operation to be idempotent. This is achieved by
                ignoring this request if the last successful operation on the resource
                had the same request ID. If set, invocation_id must also be provided.
                Restricted to 36 Unicode characters.
            invocation_id (str): The invocation ID. It is optional, but strongly recommended.

                If left empty then a new unique ID will be assigned by the server. If
                populated, a RFC 4122-compliant v4 UUID is preferred, but v3 or v5 UUIDs
                are allowed too.
            invocation (Union[dict, ~google.cloud.devtools.resultstore.v2.types.Invocation]): The invocation to create.  Its name field will be ignored, since the name
                will be derived from the id field above and assigned by the server.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.devtools.resultstore.v2.types.Invocation`
            authorization_token (str): This is a token to authorize upload access to this invocation. It
                must be set to a RFC 4122-compliant v3, v4, or v5 UUID. Once this is set
                in CreateInvocation, all other upload RPCs for that Invocation and any
                of its child resources must also include the exact same token, or they
                will be rejected. The generated token should be unique to this
                invocation, and it should be kept secret.

                The purpose of this field is to prevent other users and tools from
                clobbering your upload intentionally or accidentally. The standard way
                of using this token is to create a second v4 UUID when the invocation_id
                is created, and storing them together during the upload. Essentially,
                this is a "password" to the invocation.
            auto_finalize_time (Union[dict, ~google.cloud.devtools.resultstore.v2.types.Timestamp]): By default, Invocations are auto-finalized if they are not modified for 24
                hours. If you need auto-finalize to happen sooner, set this field to the
                time you'd like auto-finalize to occur.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.devtools.resultstore.v2.types.Timestamp`
            initial_resume_token (str): Client provided unique token for batch upload to ensure data
                integrity and to provide a way to resume batch upload in case of a
                distributed failure on the client side. The standard uploading client is
                presumed to have many machines uploading to ResultStore, and that any
                given machine could process any given Invocation at any time. This field
                is used to coordinate between the client's machines, resolve concurrency
                issues, and enforce "exactly once" semantics on each batch within the
                upload.

                The typical usage of the resume_token is that it should contain a "key"
                indicating to the client where it is in the upload process, so that the
                client can use it to resume the upload by reconstructing the state of
                upload from the point where it was interrupted.

                If this matches the previously uploaded resume_token, then this request
                will silently do nothing, making CreateInvocation idempotent. If this
                token is provided, all further upload RPCs must be done through
                UploadBatch. This token must not be combined with request_id. Must be
                web safe Base64 encoded bytes.
            uploader_state (bytes): Client-specific data used to resume batch upload if an error occurs
                and retry is needed. This serves a role closely related to resume_token,
                as both fields may be used to provide state required to restore a Batch
                Upload, but they differ in two important aspects:

                -  it is not compared to previous values, and as such does not provide
                   concurrency control;
                -  it allows for a larger payload, since the contents are never
                   inspected/compared; The size of the message must be within 1 MiB. Too
                   large requests will be rejected.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.devtools.resultstore.v2.types.Invocation` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'create_invocation' not in self._inner_api_calls:
            self._inner_api_calls['create_invocation'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.create_invocation,
                default_retry=self._method_configs['CreateInvocation'].retry,
                default_timeout=self._method_configs['CreateInvocation'].timeout,
                client_info=self._client_info,
            )

        request = resultstore_upload_pb2.CreateInvocationRequest(
            request_id=request_id,
            invocation_id=invocation_id,
            invocation=invocation,
            authorization_token=authorization_token,
            auto_finalize_time=auto_finalize_time,
            initial_resume_token=initial_resume_token,
            uploader_state=uploader_state,
        )
        return self._inner_api_calls['create_invocation'](request, retry=retry, timeout=timeout, metadata=metadata)

    def update_invocation(
            self,
            invocation=None,
            update_mask=None,
            authorization_token=None,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Applies a standard update to the invocation identified by the given proto's
        name.  For all types of fields (primitive, message, or repeated), replaces
        them with the given proto fields if they are under the given field mask
        paths.  Fields that match the mask but aren't populated in the given
        invocation are cleared. This is an implicitly idempotent API.

        Returns an empty Invocation proto with only the name and ID fields
        populated.

        An error will be reported in the following cases:
        - If the invocation does not exist.
        - If the invocation is finalized.
        - If no field mask was given.

        Example:
            >>> from google.cloud.devtools.resultstore import v2
            >>>
            >>> client = v2.ResultStoreUploadClient()
            >>>
            >>> response = client.update_invocation()

        Args:
            invocation (Union[dict, ~google.cloud.devtools.resultstore.v2.types.Invocation]): Contains the name and the fields of the invocation to be updated.
                The name format must be: invocations/${INVOCATION_ID}

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.devtools.resultstore.v2.types.Invocation`
            update_mask (Union[dict, ~google.cloud.devtools.resultstore.v2.types.FieldMask]): Indicates which fields to update.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.devtools.resultstore.v2.types.FieldMask`
            authorization_token (str): This is a token to authorize access to this invocation. It must be set to
                the same value that was provided in the CreateInvocationRequest.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.devtools.resultstore.v2.types.Invocation` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'update_invocation' not in self._inner_api_calls:
            self._inner_api_calls['update_invocation'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.update_invocation,
                default_retry=self._method_configs['UpdateInvocation'].retry,
                default_timeout=self._method_configs['UpdateInvocation'].timeout,
                client_info=self._client_info,
            )

        request = resultstore_upload_pb2.UpdateInvocationRequest(
            invocation=invocation,
            update_mask=update_mask,
            authorization_token=authorization_token,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [('invocation.name', invocation.name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(routing_header)
            metadata.append(routing_metadata)

        return self._inner_api_calls['update_invocation'](request, retry=retry, timeout=timeout, metadata=metadata)

    def merge_invocation(
            self,
            request_id=None,
            invocation=None,
            update_mask=None,
            authorization_token=None,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Applies a merge update to the invocation identified by the given proto's
        name.  For primitive and message fields, replaces them with the ones in
        the given proto if they are covered under the field mask paths.  For
        repeated fields, merges to them with the given ones if they are covered
        under the field mask paths. This is not an implicitly idempotent API, so a
        request id is required to make it idempotent.

        Returns an empty Invocation proto with only the name and ID fields
        populated.


        An error will be reported in the following cases:
        - If the invocation does not exist.
        - If the invocation is finalized.
        - If no field mask was given.

        Example:
            >>> from google.cloud.devtools.resultstore import v2
            >>>
            >>> client = v2.ResultStoreUploadClient()
            >>>
            >>> response = client.merge_invocation()

        Args:
            request_id (str): A unique identifier for this request. Must be set to a different value for
                each request that affects a given resource (eg. a random UUID). Required
                for the operation to be idempotent. This is achieved by ignoring this
                request if the last successful operation on the resource had the same
                request ID.  Restricted to 36 Unicode characters.
            invocation (Union[dict, ~google.cloud.devtools.resultstore.v2.types.Invocation]): Contains the name and the fields of the invocation to be merged. The
                name format must be: invocations/${INVOCATION_ID}

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.devtools.resultstore.v2.types.Invocation`
            update_mask (Union[dict, ~google.cloud.devtools.resultstore.v2.types.FieldMask]): Indicates which fields to merge.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.devtools.resultstore.v2.types.FieldMask`
            authorization_token (str): This is a token to authorize access to this invocation. It must be set to
                the same value that was provided in the CreateInvocationRequest.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.devtools.resultstore.v2.types.Invocation` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'merge_invocation' not in self._inner_api_calls:
            self._inner_api_calls['merge_invocation'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.merge_invocation,
                default_retry=self._method_configs['MergeInvocation'].retry,
                default_timeout=self._method_configs['MergeInvocation'].timeout,
                client_info=self._client_info,
            )

        request = resultstore_upload_pb2.MergeInvocationRequest(
            request_id=request_id,
            invocation=invocation,
            update_mask=update_mask,
            authorization_token=authorization_token,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [('invocation.name', invocation.name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(routing_header)
            metadata.append(routing_metadata)

        return self._inner_api_calls['merge_invocation'](request, retry=retry, timeout=timeout, metadata=metadata)

    def touch_invocation(
            self,
            name=None,
            authorization_token=None,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Touches the invocation identified by the given proto's name.

        This is useful when you need to notify ResultStore that you haven't
        abandoned the upload, since abandoned uploads will be automatically
        finalized after a set period.

        An error will be reported in the following cases:
        - If the invocation does not exist.
        - If the invocation is finalized.

        Example:
            >>> from google.cloud.devtools.resultstore import v2
            >>>
            >>> client = v2.ResultStoreUploadClient()
            >>>
            >>> response = client.touch_invocation()

        Args:
            name (str): The name of the invocation. Its format must be:
                invocations/${INVOCATION_ID}
            authorization_token (str): This is a token to authorize access to this invocation. It must be set to
                the same value that was provided in the CreateInvocationRequest.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.devtools.resultstore.v2.types.TouchInvocationResponse` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'touch_invocation' not in self._inner_api_calls:
            self._inner_api_calls['touch_invocation'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.touch_invocation,
                default_retry=self._method_configs['TouchInvocation'].retry,
                default_timeout=self._method_configs['TouchInvocation'].timeout,
                client_info=self._client_info,
            )

        request = resultstore_upload_pb2.TouchInvocationRequest(
            name=name,
            authorization_token=authorization_token,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [('name', name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(routing_header)
            metadata.append(routing_metadata)

        return self._inner_api_calls['touch_invocation'](request, retry=retry, timeout=timeout, metadata=metadata)

    def finalize_invocation(
            self,
            name=None,
            authorization_token=None,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Declares the invocation with the given name as finalized and immutable by
        the user. It may still be mutated by post-processing. This is an implicitly
        idempotent API.

        If an Invocation is not updated for 24 hours, some time after that
        this will be called automatically.

        An error will be reported in the following cases:
        - If the invocation does not exist.

        Example:
            >>> from google.cloud.devtools.resultstore import v2
            >>>
            >>> client = v2.ResultStoreUploadClient()
            >>>
            >>> response = client.finalize_invocation()

        Args:
            name (str): The name of the invocation. Its format must be:
                invocations/${INVOCATION_ID}
            authorization_token (str): This is a token to authorize access to this invocation. It must be set to
                the same value that was provided in the CreateInvocationRequest.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.devtools.resultstore.v2.types.FinalizeInvocationResponse` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'finalize_invocation' not in self._inner_api_calls:
            self._inner_api_calls['finalize_invocation'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.finalize_invocation,
                default_retry=self._method_configs['FinalizeInvocation'].retry,
                default_timeout=self._method_configs['FinalizeInvocation'].timeout,
                client_info=self._client_info,
            )

        request = resultstore_upload_pb2.FinalizeInvocationRequest(
            name=name,
            authorization_token=authorization_token,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [('name', name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(routing_header)
            metadata.append(routing_metadata)

        return self._inner_api_calls['finalize_invocation'](request, retry=retry, timeout=timeout, metadata=metadata)

    def delete_invocation(
            self,
            name=None,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Deletes an immutable invocation (permanently)
        Note: this does not delete indirect data, e.g. files stored in other
        services.

        An error will be reported in the following cases:
        - If the invocation does not exist.
        - If the invocation is not finalized.  This can be retried until it is.

        Example:
            >>> from google.cloud.devtools.resultstore import v2
            >>>
            >>> client = v2.ResultStoreUploadClient()
            >>>
            >>> client.delete_invocation()

        Args:
            name (str): The name of the invocation. Its format must be:
                invocations/${INVOCATION_ID}
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'delete_invocation' not in self._inner_api_calls:
            self._inner_api_calls['delete_invocation'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.delete_invocation,
                default_retry=self._method_configs['DeleteInvocation'].retry,
                default_timeout=self._method_configs['DeleteInvocation'].timeout,
                client_info=self._client_info,
            )

        request = resultstore_upload_pb2.DeleteInvocationRequest(
            name=name,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [('name', name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(routing_header)
            metadata.append(routing_metadata)

        self._inner_api_calls['delete_invocation'](request, retry=retry, timeout=timeout, metadata=metadata)

    def create_target(
            self,
            request_id=None,
            parent=None,
            target_id=None,
            target=None,
            authorization_token=None,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Creates the given target under the given parent invocation. The given
        target ID is URL encoded, converted to the full resource name, and assigned
        to the target's name field. This is not an implicitly idempotent API, so a
        request id is required to make it idempotent.

        Returns an empty Target proto with only the name and ID fields populated.

        An error will be reported in the following cases:
        - If no target ID is provided.
        - If the parent invocation does not exist.
        - If the parent invocation is finalized.
        - If a target with the same name already exists.

        Example:
            >>> from google.cloud.devtools.resultstore import v2
            >>>
            >>> client = v2.ResultStoreUploadClient()
            >>>
            >>> response = client.create_target()

        Args:
            request_id (str): A unique identifier for this request. Must be set to a different value for
                each request that affects a given resource (eg. a random UUID). Required
                for the operation to be idempotent. This is achieved by ignoring this
                request if the last successful operation on the resource had the same
                request ID.  Restricted to 36 Unicode characters.
            parent (str): The name of the parent invocation in which the target is created.
                Its format must be invocations/${INVOCATION_ID}
            target_id (str): The target identifier.  It can be any string up to 1024 Unicode characters
                long except for the reserved id '-'.
            target (Union[dict, ~google.cloud.devtools.resultstore.v2.types.Target]): The target to create.  Its name field will be ignored, since the name will
                be derived from the id field above and assigned by the server.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.devtools.resultstore.v2.types.Target`
            authorization_token (str): This is a token to authorize access to this invocation. It must be set to
                the same value that was provided in the CreateInvocationRequest.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.devtools.resultstore.v2.types.Target` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'create_target' not in self._inner_api_calls:
            self._inner_api_calls['create_target'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.create_target,
                default_retry=self._method_configs['CreateTarget'].retry,
                default_timeout=self._method_configs['CreateTarget'].timeout,
                client_info=self._client_info,
            )

        request = resultstore_upload_pb2.CreateTargetRequest(
            request_id=request_id,
            parent=parent,
            target_id=target_id,
            target=target,
            authorization_token=authorization_token,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [('parent', parent)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(routing_header)
            metadata.append(routing_metadata)

        return self._inner_api_calls['create_target'](request, retry=retry, timeout=timeout, metadata=metadata)

    def update_target(
            self,
            target=None,
            update_mask=None,
            authorization_token=None,
            create_if_not_found=None,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Applies a standard update to the target identified by the given proto's
        name. For all types of fields (primitive, message, or repeated), replaces
        them with the given proto fields if they are under the given field mask
        paths. Fields that match the mask but aren't populated in the given
        target are cleared. This is an implicitly idempotent API.

        Returns an empty Target proto with only the name and ID fields populated.

        An error will be reported in the following cases:
        - If the target does not exist.
        - If the target or parent invocation is finalized.
        - If no field mask was given.

        Example:
            >>> from google.cloud.devtools.resultstore import v2
            >>>
            >>> client = v2.ResultStoreUploadClient()
            >>>
            >>> response = client.update_target()

        Args:
            target (Union[dict, ~google.cloud.devtools.resultstore.v2.types.Target]): Contains the name and the fields of the target to be updated. The
                name format must be:
                invocations/${INVOCATION_ID}/targets/${url_encode(TARGET_ID)}

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.devtools.resultstore.v2.types.Target`
            update_mask (Union[dict, ~google.cloud.devtools.resultstore.v2.types.FieldMask]): Indicates which fields to update.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.devtools.resultstore.v2.types.FieldMask`
            authorization_token (str): This is a token to authorize access to this invocation. It must be set to
                the same value that was provided in the CreateInvocationRequest.
            create_if_not_found (bool): If true then the Update operation will become a Create operation if
                the Target is NOT_FOUND.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.devtools.resultstore.v2.types.Target` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'update_target' not in self._inner_api_calls:
            self._inner_api_calls['update_target'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.update_target,
                default_retry=self._method_configs['UpdateTarget'].retry,
                default_timeout=self._method_configs['UpdateTarget'].timeout,
                client_info=self._client_info,
            )

        request = resultstore_upload_pb2.UpdateTargetRequest(
            target=target,
            update_mask=update_mask,
            authorization_token=authorization_token,
            create_if_not_found=create_if_not_found,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [('target.name', target.name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(routing_header)
            metadata.append(routing_metadata)

        return self._inner_api_calls['update_target'](request, retry=retry, timeout=timeout, metadata=metadata)

    def merge_target(
            self,
            request_id=None,
            target=None,
            update_mask=None,
            authorization_token=None,
            create_if_not_found=None,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Applies a merge update to the target identified by the given proto's
        name. For primitive and message fields, replaces them with the ones in the
        given proto if they are covered under the field mask paths.  For repeated
        fields, merges to them with the given ones if they are covered under the
        field mask paths. This is not an implicitly idempotent API, so a request
        id is required to make it idempotent.

        Returns an empty Target proto with only the name and ID fields populated.


        An error will be reported in the following cases:
        - If the target does not exist.
        - If the target or parent invocation is finalized.
        - If no field mask was given.

        Example:
            >>> from google.cloud.devtools.resultstore import v2
            >>>
            >>> client = v2.ResultStoreUploadClient()
            >>>
            >>> response = client.merge_target()

        Args:
            request_id (str): A unique identifier for this request. Must be set to a different value for
                each request that affects a given resource (eg. a random UUID). Required
                for the operation to be idempotent. This is achieved by ignoring this
                request if the last successful operation on the resource had the same
                request ID.  Restricted to 36 Unicode characters.
            target (Union[dict, ~google.cloud.devtools.resultstore.v2.types.Target]): Contains the name and the fields of the target to be merged. The
                name format must be:
                invocations/${INVOCATION_ID}/targets/${url_encode(TARGET_ID)}

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.devtools.resultstore.v2.types.Target`
            update_mask (Union[dict, ~google.cloud.devtools.resultstore.v2.types.FieldMask]): Indicates which fields to merge.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.devtools.resultstore.v2.types.FieldMask`
            authorization_token (str): This is a token to authorize access to this invocation. It must be set to
                the same value that was provided in the CreateInvocationRequest.
            create_if_not_found (bool): If true then the Merge operation will become a Create operation if
                the Target is NOT_FOUND.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.devtools.resultstore.v2.types.Target` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'merge_target' not in self._inner_api_calls:
            self._inner_api_calls['merge_target'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.merge_target,
                default_retry=self._method_configs['MergeTarget'].retry,
                default_timeout=self._method_configs['MergeTarget'].timeout,
                client_info=self._client_info,
            )

        request = resultstore_upload_pb2.MergeTargetRequest(
            request_id=request_id,
            target=target,
            update_mask=update_mask,
            authorization_token=authorization_token,
            create_if_not_found=create_if_not_found,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [('target.name', target.name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(routing_header)
            metadata.append(routing_metadata)

        return self._inner_api_calls['merge_target'](request, retry=retry, timeout=timeout, metadata=metadata)

    def finalize_target(
            self,
            name=None,
            authorization_token=None,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Declares the target with the given name as finalized and immutable by the
        user. It may still be mutated by post-processing. This is an implicitly
        idempotent API.

        An error will be reported in the following cases:
        - If the target does not exist.

        Example:
            >>> from google.cloud.devtools.resultstore import v2
            >>>
            >>> client = v2.ResultStoreUploadClient()
            >>>
            >>> response = client.finalize_target()

        Args:
            name (str): The name of the target. Its format must be:
                invocations/${INVOCATION_ID}/targets/${url_encode(TARGET_ID)}
            authorization_token (str): This is a token to authorize access to this invocation. It must be set to
                the same value that was provided in the CreateInvocationRequest.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.devtools.resultstore.v2.types.FinalizeTargetResponse` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'finalize_target' not in self._inner_api_calls:
            self._inner_api_calls['finalize_target'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.finalize_target,
                default_retry=self._method_configs['FinalizeTarget'].retry,
                default_timeout=self._method_configs['FinalizeTarget'].timeout,
                client_info=self._client_info,
            )

        request = resultstore_upload_pb2.FinalizeTargetRequest(
            name=name,
            authorization_token=authorization_token,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [('name', name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(routing_header)
            metadata.append(routing_metadata)

        return self._inner_api_calls['finalize_target'](request, retry=retry, timeout=timeout, metadata=metadata)

    def create_configured_target(
            self,
            request_id=None,
            parent=None,
            config_id=None,
            configured_target=None,
            authorization_token=None,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Creates the given configured target under the given parent target.
        The given configured target ID is URL encoded, converted to the full
        resource name, and assigned to the configured target's name field.
        This is not an implicitly idempotent API, so a request id is required
        to make it idempotent.

        Returns an empty ConfiguredTarget proto with only the name and ID fields
        populated.

        An error will be reported in the following cases:
        - If no config ID is provided.
        - If a configured target with the same ID already exists.
        - If the parent target does not exist.
        - If the parent target or invocation is finalized.

        Example:
            >>> from google.cloud.devtools.resultstore import v2
            >>>
            >>> client = v2.ResultStoreUploadClient()
            >>>
            >>> response = client.create_configured_target()

        Args:
            request_id (str): A unique identifier for this request. Must be set to a different value for
                each request that affects a given resource (eg. a random UUID). Required
                for the operation to be idempotent. This is achieved by ignoring this
                request if the last successful operation on the resource had the same
                request ID.  Restricted to 36 Unicode characters.
            parent (str): The name of the parent target in which the configured target is
                created. Its format must be:
                invocations/${INVOCATION_ID}/targets/${url_encode(TARGET_ID)}
            config_id (str): The configuration identifier. This must match the ID of an existing
                Configuration under this Invocation. Cannot be the reserved id '-'.
            configured_target (Union[dict, ~google.cloud.devtools.resultstore.v2.types.ConfiguredTarget]): The configured target to create. Its name field will be ignored, since the
                name will be derived from the id field above and assigned by the server.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.devtools.resultstore.v2.types.ConfiguredTarget`
            authorization_token (str): This is a token to authorize access to this invocation. It must be set to
                the same value that was provided in the CreateInvocationRequest.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.devtools.resultstore.v2.types.ConfiguredTarget` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'create_configured_target' not in self._inner_api_calls:
            self._inner_api_calls['create_configured_target'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.create_configured_target,
                default_retry=self._method_configs['CreateConfiguredTarget'].retry,
                default_timeout=self._method_configs['CreateConfiguredTarget'].timeout,
                client_info=self._client_info,
            )

        request = resultstore_upload_pb2.CreateConfiguredTargetRequest(
            request_id=request_id,
            parent=parent,
            config_id=config_id,
            configured_target=configured_target,
            authorization_token=authorization_token,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [('parent', parent)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(routing_header)
            metadata.append(routing_metadata)

        return self._inner_api_calls['create_configured_target'](request, retry=retry, timeout=timeout, metadata=metadata)

    def update_configured_target(
            self,
            configured_target=None,
            update_mask=None,
            authorization_token=None,
            create_if_not_found=None,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Applies a standard update to the configured target identified by the given
        proto's name. For all types of fields (primitive, message, or repeated),
        replaces them with the given proto fields if they are under the given
        field mask paths. Fields that match the mask but aren't populated in the
        given configured target are cleared. This is an implicitly idempotent API.

        Returns an empty ConfiguredTarget proto with only the name and ID fields
        populated.

        An error will be reported in the following cases:
        - If the configured target does not exist.
        - If the parent target or invocation is finalized.
        - If no field mask was given.

        Example:
            >>> from google.cloud.devtools.resultstore import v2
            >>>
            >>> client = v2.ResultStoreUploadClient()
            >>>
            >>> response = client.update_configured_target()

        Args:
            configured_target (Union[dict, ~google.cloud.devtools.resultstore.v2.types.ConfiguredTarget]): Contains the name and the fields of the configured target to be
                updated. The name format must be:
                invocations/${INVOCATION_ID}/targets/${url_encode(TARGET_ID)}/configuredTargets/${url_encode(CONFIG_ID)}

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.devtools.resultstore.v2.types.ConfiguredTarget`
            update_mask (Union[dict, ~google.cloud.devtools.resultstore.v2.types.FieldMask]): Indicates which fields to update.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.devtools.resultstore.v2.types.FieldMask`
            authorization_token (str): This is a token to authorize access to this invocation. It must be set to
                the same value that was provided in the CreateInvocationRequest.
            create_if_not_found (bool): If true then the Update operation will become a Create operation if
                the ConfiguredTarget is NOT_FOUND.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.devtools.resultstore.v2.types.ConfiguredTarget` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'update_configured_target' not in self._inner_api_calls:
            self._inner_api_calls['update_configured_target'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.update_configured_target,
                default_retry=self._method_configs['UpdateConfiguredTarget'].retry,
                default_timeout=self._method_configs['UpdateConfiguredTarget'].timeout,
                client_info=self._client_info,
            )

        request = resultstore_upload_pb2.UpdateConfiguredTargetRequest(
            configured_target=configured_target,
            update_mask=update_mask,
            authorization_token=authorization_token,
            create_if_not_found=create_if_not_found,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [('configured_target.name', configured_target.name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(routing_header)
            metadata.append(routing_metadata)

        return self._inner_api_calls['update_configured_target'](request, retry=retry, timeout=timeout, metadata=metadata)

    def merge_configured_target(
            self,
            request_id=None,
            configured_target=None,
            update_mask=None,
            authorization_token=None,
            create_if_not_found=None,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Applies a merge update to the configured target identified by the given
        proto's name. For primitive and message fields, replaces them with the
        ones in the given proto if they are covered under the field mask paths.
        For repeated fields, merges to them with the given ones if they are
        covered under the field mask paths. This is not an implicitly idempotent
        API, so a request id is required to make it idempotent.

        Returns an empty ConfiguredTarget proto with only the name and ID fields
        populated.


        An error will be reported in the following cases:
        - If the configured target does not exist.
        - If the parent target or invocation is finalized.
        - If no field mask was given.

        Example:
            >>> from google.cloud.devtools.resultstore import v2
            >>>
            >>> client = v2.ResultStoreUploadClient()
            >>>
            >>> response = client.merge_configured_target()

        Args:
            request_id (str): A unique identifier for this request. Must be set to a different value for
                each request that affects a given resource (eg. a random UUID). Required
                for the operation to be idempotent. This is achieved by ignoring this
                request if the last successful operation on the resource had the same
                request ID.  Restricted to 36 Unicode characters.
            configured_target (Union[dict, ~google.cloud.devtools.resultstore.v2.types.ConfiguredTarget]): Contains the name and the fields of the configured target to be
                merged. The name format must be:
                invocations/${INVOCATION_ID}/targets/${url_encode(TARGET_ID)}/configuredTargets/${url_encode(CONFIG_ID)}

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.devtools.resultstore.v2.types.ConfiguredTarget`
            update_mask (Union[dict, ~google.cloud.devtools.resultstore.v2.types.FieldMask]): Indicates which fields to merge.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.devtools.resultstore.v2.types.FieldMask`
            authorization_token (str): This is a token to authorize access to this invocation. It must be set to
                the same value that was provided in the CreateInvocationRequest.
            create_if_not_found (bool): If true then the Merge operation will become a Create operation if
                the ConfiguredTarget is NOT_FOUND.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.devtools.resultstore.v2.types.ConfiguredTarget` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'merge_configured_target' not in self._inner_api_calls:
            self._inner_api_calls['merge_configured_target'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.merge_configured_target,
                default_retry=self._method_configs['MergeConfiguredTarget'].retry,
                default_timeout=self._method_configs['MergeConfiguredTarget'].timeout,
                client_info=self._client_info,
            )

        request = resultstore_upload_pb2.MergeConfiguredTargetRequest(
            request_id=request_id,
            configured_target=configured_target,
            update_mask=update_mask,
            authorization_token=authorization_token,
            create_if_not_found=create_if_not_found,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [('configured_target.name', configured_target.name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(routing_header)
            metadata.append(routing_metadata)

        return self._inner_api_calls['merge_configured_target'](request, retry=retry, timeout=timeout, metadata=metadata)

    def finalize_configured_target(
            self,
            name=None,
            authorization_token=None,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Declares the configured target with the given name as finalized and
        immutable by the user. It may still be mutated by post-processing. This is
        an implicitly idempotent API.

        An error will be reported in the following cases:
        - If the configured target does not exist.

        Example:
            >>> from google.cloud.devtools.resultstore import v2
            >>>
            >>> client = v2.ResultStoreUploadClient()
            >>>
            >>> response = client.finalize_configured_target()

        Args:
            name (str): The name of the configured target. Its format must be:
                invocations/${INVOCATION_ID}/targets/${url_encode(TARGET_ID)}/configuredTargets/${url_encode(CONFIG_ID)}
            authorization_token (str): This is a token to authorize access to this invocation. It must be set to
                the same value that was provided in the CreateInvocationRequest.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.devtools.resultstore.v2.types.FinalizeConfiguredTargetResponse` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'finalize_configured_target' not in self._inner_api_calls:
            self._inner_api_calls['finalize_configured_target'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.finalize_configured_target,
                default_retry=self._method_configs['FinalizeConfiguredTarget'].retry,
                default_timeout=self._method_configs['FinalizeConfiguredTarget'].timeout,
                client_info=self._client_info,
            )

        request = resultstore_upload_pb2.FinalizeConfiguredTargetRequest(
            name=name,
            authorization_token=authorization_token,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [('name', name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(routing_header)
            metadata.append(routing_metadata)

        return self._inner_api_calls['finalize_configured_target'](request, retry=retry, timeout=timeout, metadata=metadata)

    def create_action(
            self,
            request_id=None,
            parent=None,
            action_id=None,
            action=None,
            authorization_token=None,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Creates the given action under the given configured target. The given
        action ID is URL encoded, converted to the full resource name, and
        assigned to the action's name field. This is not an implicitly
        idempotent API, so a request id is required to make it idempotent.

        Returns an empty Action proto with only the name and ID fields populated.

        An error will be reported in the following cases:
        - If no action ID provided.
        - If the parent configured target does not exist.
        - If the parent target or invocation is finalized.
        - If an action  with the same name already exists.

        Example:
            >>> from google.cloud.devtools.resultstore import v2
            >>>
            >>> client = v2.ResultStoreUploadClient()
            >>>
            >>> response = client.create_action()

        Args:
            request_id (str): A unique identifier for this request. Must be set to a different value for
                each request that affects a given resource (eg. a random UUID). Required
                for the operation to be idempotent. This is achieved by ignoring this
                request if the last successful operation on the resource had the same
                request ID.  Restricted to 36 Unicode characters.
            parent (str): The name of the parent configured target in which the action is
                created. Its format must be:
                invocations/${INVOCATION_ID}/targets/${url_encode(TARGET_ID)}/configuredTargets/${url_encode(CONFIG_ID)}
            action_id (str): The action identifier. It can be any string up to 512 Unicode
                characters long, except for the reserved id '-'.

                Recommended IDs for Test Actions: "test": For a single test action.
                "test_shard0_run0_attempt0" ... "test_shard9_run9_attempt9": For tests
                with shard/run/attempts.

                Recommended IDs for Build Actions: "build": If you only have a single
                build action.
            action (Union[dict, ~google.cloud.devtools.resultstore.v2.types.Action]): The action to create.  Its name field will be ignored, since the
                name will be derived from the id field above and assigned by the server.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.devtools.resultstore.v2.types.Action`
            authorization_token (str): This is a token to authorize access to this invocation. It must be set to
                the same value that was provided in the CreateInvocationRequest.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.devtools.resultstore.v2.types.Action` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'create_action' not in self._inner_api_calls:
            self._inner_api_calls['create_action'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.create_action,
                default_retry=self._method_configs['CreateAction'].retry,
                default_timeout=self._method_configs['CreateAction'].timeout,
                client_info=self._client_info,
            )

        request = resultstore_upload_pb2.CreateActionRequest(
            request_id=request_id,
            parent=parent,
            action_id=action_id,
            action=action,
            authorization_token=authorization_token,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [('parent', parent)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(routing_header)
            metadata.append(routing_metadata)

        return self._inner_api_calls['create_action'](request, retry=retry, timeout=timeout, metadata=metadata)

    def update_action(
            self,
            action=None,
            update_mask=None,
            authorization_token=None,
            create_if_not_found=None,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Applies a standard update to the action identified by the given
        proto's name.  For all types of fields (primitive, message, or repeated),
        replaces them with the given proto fields if they are under the given
        field mask paths.  Fields that match the mask but aren't populated in the
        given action are cleared.  This is an implicitly idempotent API.

        Returns an empty Action proto with only the name and ID fields populated.

        An error will be reported in the following cases:
        - If the action does not exist.
        - If the parent target or invocation is finalized.
        - If no field mask was given.

        Example:
            >>> from google.cloud.devtools.resultstore import v2
            >>>
            >>> client = v2.ResultStoreUploadClient()
            >>>
            >>> response = client.update_action()

        Args:
            action (Union[dict, ~google.cloud.devtools.resultstore.v2.types.Action]): Contains the name and the fields of the action to be updated. The
                name format must be:
                invocations/${INVOCATION_ID}/targets/${url_encode(TARGET_ID)}/configuredTargets/${url_encode(CONFIG_ID)}/actions/${url_encode(ACTION_ID)}

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.devtools.resultstore.v2.types.Action`
            update_mask (Union[dict, ~google.cloud.devtools.resultstore.v2.types.FieldMask]): Indicates which fields to update.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.devtools.resultstore.v2.types.FieldMask`
            authorization_token (str): This is a token to authorize access to this invocation. It must be set to
                the same value that was provided in the CreateInvocationRequest.
            create_if_not_found (bool): If true then the Update operation will become a Create operation if
                the Action is NOT_FOUND.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.devtools.resultstore.v2.types.Action` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'update_action' not in self._inner_api_calls:
            self._inner_api_calls['update_action'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.update_action,
                default_retry=self._method_configs['UpdateAction'].retry,
                default_timeout=self._method_configs['UpdateAction'].timeout,
                client_info=self._client_info,
            )

        request = resultstore_upload_pb2.UpdateActionRequest(
            action=action,
            update_mask=update_mask,
            authorization_token=authorization_token,
            create_if_not_found=create_if_not_found,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [('action.name', action.name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(routing_header)
            metadata.append(routing_metadata)

        return self._inner_api_calls['update_action'](request, retry=retry, timeout=timeout, metadata=metadata)

    def merge_action(
            self,
            request_id=None,
            action=None,
            update_mask=None,
            authorization_token=None,
            create_if_not_found=None,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Applies a merge update to the action identified by the given
        proto's name.  For primitive and message fields, replaces them with the
        ones in the given proto if they are covered under the field mask paths.
        For repeated fields, merges to them with the given ones if they are
        covered under the field mask paths. This is not an implicitly idempotent
        API, so a request id is required to make it idempotent.

        Returns an empty Action proto with only the name and ID fields populated.


        An error will be reported in the following cases:
        - If the action does not exist.
        - If the parent target or invocation is finalized.
        - If no field mask was given.

        Example:
            >>> from google.cloud.devtools.resultstore import v2
            >>>
            >>> client = v2.ResultStoreUploadClient()
            >>>
            >>> response = client.merge_action()

        Args:
            request_id (str): A unique identifier for this request. Must be set to a different value for
                each request that affects a given resource (eg. a random UUID). Required
                for the operation to be idempotent. This is achieved by ignoring this
                request if the last successful operation on the resource had the same
                request ID.  Restricted to 36 Unicode characters.
            action (Union[dict, ~google.cloud.devtools.resultstore.v2.types.Action]): Contains the name and the fields of the action to be merged. The
                name format must be:
                invocations/${INVOCATION_ID}/targets/${url_encode(TARGET_ID)}/configuredTargets/${url_encode(CONFIG_ID)}/actions/${url_encode(ACTION_ID)}

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.devtools.resultstore.v2.types.Action`
            update_mask (Union[dict, ~google.cloud.devtools.resultstore.v2.types.FieldMask]): Indicates which fields to merge.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.devtools.resultstore.v2.types.FieldMask`
            authorization_token (str): This is a token to authorize access to this invocation. It must be set to
                the same value that was provided in the CreateInvocationRequest.
            create_if_not_found (bool): If true then the Merge operation will become a Create operation if
                the Action is NOT_FOUND.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.devtools.resultstore.v2.types.Action` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'merge_action' not in self._inner_api_calls:
            self._inner_api_calls['merge_action'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.merge_action,
                default_retry=self._method_configs['MergeAction'].retry,
                default_timeout=self._method_configs['MergeAction'].timeout,
                client_info=self._client_info,
            )

        request = resultstore_upload_pb2.MergeActionRequest(
            request_id=request_id,
            action=action,
            update_mask=update_mask,
            authorization_token=authorization_token,
            create_if_not_found=create_if_not_found,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [('action.name', action.name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(routing_header)
            metadata.append(routing_metadata)

        return self._inner_api_calls['merge_action'](request, retry=retry, timeout=timeout, metadata=metadata)

    def create_configuration(
            self,
            request_id=None,
            parent=None,
            config_id=None,
            configuration=None,
            authorization_token=None,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Creates the given configuration under the given parent invocation. The
        given configuration ID is URL encoded, converted to the full resource name,
        and assigned to the configuration's name field. The configuration ID of
        "default" should be preferred for the default configuration in a
        single-config invocation. This is not an implicitly idempotent API, so a
        request id is required to make it idempotent.

        Returns an empty Configuration proto with only the name and ID fields
        populated.

        An error will be reported in the following cases:
        - If no configuration ID is provided.
        - If the parent invocation does not exist.
        - If the parent invocation is finalized.
        - If a configuration with the same name already exists.

        Example:
            >>> from google.cloud.devtools.resultstore import v2
            >>>
            >>> client = v2.ResultStoreUploadClient()
            >>>
            >>> response = client.create_configuration()

        Args:
            request_id (str): A unique identifier for this request. Must be set to a different value for
                each request that affects a given resource (eg. a random UUID). Required
                for the operation to be idempotent. This is achieved by ignoring this
                request if the last successful operation on the resource had the same
                request ID.  Restricted to 36 Unicode characters.
            parent (str): The name of the parent invocation in which the configuration is
                created. Its format must be invocations/${INVOCATION_ID}
            config_id (str): The configuration identifier. It can be any string up to 256 Unicode
                characters long. The configuration ID of "default" should be preferred for
                the default configuration in a single-config invocation. Cannot be the
                reserved id '-'.
            configuration (Union[dict, ~google.cloud.devtools.resultstore.v2.types.Configuration]): The configuration to create. Its name field will be ignored, since the name
                will be derived from the id field above and assigned by the server.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.devtools.resultstore.v2.types.Configuration`
            authorization_token (str): This is a token to authorize access to this invocation. It must be set to
                the same value that was provided in the CreateInvocationRequest.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.devtools.resultstore.v2.types.Configuration` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'create_configuration' not in self._inner_api_calls:
            self._inner_api_calls['create_configuration'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.create_configuration,
                default_retry=self._method_configs['CreateConfiguration'].retry,
                default_timeout=self._method_configs['CreateConfiguration'].timeout,
                client_info=self._client_info,
            )

        request = resultstore_upload_pb2.CreateConfigurationRequest(
            request_id=request_id,
            parent=parent,
            config_id=config_id,
            configuration=configuration,
            authorization_token=authorization_token,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [('parent', parent)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(routing_header)
            metadata.append(routing_metadata)

        return self._inner_api_calls['create_configuration'](request, retry=retry, timeout=timeout, metadata=metadata)

    def update_configuration(
            self,
            configuration=None,
            update_mask=None,
            authorization_token=None,
            create_if_not_found=None,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Applies a standard update to the configuration identified by the given
        proto's name. For all types of fields (primitive, message, or repeated),
        replaces them with the given proto fields if they are under the given field
        mask paths. Fields that match the mask but aren't populated in the given
        configuration are cleared. This is an implicitly idempotent API.

        Returns an empty Configuration proto with only the name and ID fields
        populated.

        An error will be reported in the following cases:
        - If the configuration does not exist.
        - If the parent invocation is finalized.
        - If no field mask was given.
        - If a given field mask path is not valid.

        Example:
            >>> from google.cloud.devtools.resultstore import v2
            >>>
            >>> client = v2.ResultStoreUploadClient()
            >>>
            >>> response = client.update_configuration()

        Args:
            configuration (Union[dict, ~google.cloud.devtools.resultstore.v2.types.Configuration]): Contains the name and fields of the configuration to be updated. The
                name format must be:
                invocations/${INVOCATION_ID}/configs/${url_encode(CONFIG_ID)}

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.devtools.resultstore.v2.types.Configuration`
            update_mask (Union[dict, ~google.cloud.devtools.resultstore.v2.types.FieldMask]): Indicates which fields to update.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.devtools.resultstore.v2.types.FieldMask`
            authorization_token (str): This is a token to authorize access to this invocation. It must be set to
                the same value that was provided in the CreateInvocationRequest.
            create_if_not_found (bool): If true then the Update operation will become a Create operation if
                the Configuration is NOT_FOUND.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.devtools.resultstore.v2.types.Configuration` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'update_configuration' not in self._inner_api_calls:
            self._inner_api_calls['update_configuration'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.update_configuration,
                default_retry=self._method_configs['UpdateConfiguration'].retry,
                default_timeout=self._method_configs['UpdateConfiguration'].timeout,
                client_info=self._client_info,
            )

        request = resultstore_upload_pb2.UpdateConfigurationRequest(
            configuration=configuration,
            update_mask=update_mask,
            authorization_token=authorization_token,
            create_if_not_found=create_if_not_found,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [('configuration.name', configuration.name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(routing_header)
            metadata.append(routing_metadata)

        return self._inner_api_calls['update_configuration'](request, retry=retry, timeout=timeout, metadata=metadata)

    def create_file_set(
            self,
            request_id=None,
            parent=None,
            file_set_id=None,
            file_set=None,
            authorization_token=None,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Creates the given file set under the given parent invocation. The given
        file set ID is URL encoded, converted to the full resource name, and
        assigned to the file set's name field. This is not an implicitly idempotent
        API, so a request id is required to make it idempotent.

        Returns an empty FileSet proto with only the name and ID fields populated.

        An error will be reported in the following cases:
        - If no file set ID is provided.
        - If a file set with the same name already exists.
        - If the parent invocation does not exist.
        - If the parent invocation is finalized.

        Example:
            >>> from google.cloud.devtools.resultstore import v2
            >>>
            >>> client = v2.ResultStoreUploadClient()
            >>>
            >>> response = client.create_file_set()

        Args:
            request_id (str): A unique identifier for this request. Must be set to a different value for
                each request that affects a given resource (eg. a random UUID). Required
                for the operation to be idempotent. This is achieved by ignoring this
                request if the last successful operation on the resource had the same
                request ID.  Restricted to 36 Unicode characters.
            parent (str): The name of the parent invocation in which the file set is created.
                Its format must be invocations/${INVOCATION_ID}
            file_set_id (str): The file set identifier. It can be any string up to 256 Unicode characters
                long.
            file_set (Union[dict, ~google.cloud.devtools.resultstore.v2.types.FileSet]): The file set to create. Its name field will be ignored, since the name will
                be derived from the id field above and assigned by the server.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.devtools.resultstore.v2.types.FileSet`
            authorization_token (str): This is a token to authorize access to this invocation. It must be set to
                the same value that was provided in the CreateInvocationRequest.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.devtools.resultstore.v2.types.FileSet` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'create_file_set' not in self._inner_api_calls:
            self._inner_api_calls['create_file_set'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.create_file_set,
                default_retry=self._method_configs['CreateFileSet'].retry,
                default_timeout=self._method_configs['CreateFileSet'].timeout,
                client_info=self._client_info,
            )

        request = resultstore_upload_pb2.CreateFileSetRequest(
            request_id=request_id,
            parent=parent,
            file_set_id=file_set_id,
            file_set=file_set,
            authorization_token=authorization_token,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [('parent', parent)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(routing_header)
            metadata.append(routing_metadata)

        return self._inner_api_calls['create_file_set'](request, retry=retry, timeout=timeout, metadata=metadata)

    def update_file_set(
            self,
            file_set=None,
            update_mask=None,
            authorization_token=None,
            create_if_not_found=None,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Applies a standard update to the file set identified by the given proto's
        name. For all types of fields (primitive, message, or repeated), replaces
        them with the given proto fields if they are under the given field mask
        paths. Fields that match the mask but aren't populated in the given
        configuration are cleared. This is an implicitly idempotent API.

        Returns an empty FileSet proto with only the name and ID fields populated.

        An error will be reported in the following cases:
        - If the file set does not exist.
        - If the parent invocation is finalized.
        - If no field mask was given.
        - If a given field mask path is not valid.

        Example:
            >>> from google.cloud.devtools.resultstore import v2
            >>>
            >>> client = v2.ResultStoreUploadClient()
            >>>
            >>> response = client.update_file_set()

        Args:
            file_set (Union[dict, ~google.cloud.devtools.resultstore.v2.types.FileSet]): Contains the name and fields of the file set to be updated. The name
                format must be:
                invocations/${INVOCATION_ID}/fileSets/${url_encode(FILE_SET_ID)}

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.devtools.resultstore.v2.types.FileSet`
            update_mask (Union[dict, ~google.cloud.devtools.resultstore.v2.types.FieldMask]): Indicates which fields to update.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.devtools.resultstore.v2.types.FieldMask`
            authorization_token (str): This is a token to authorize access to this invocation. It must be set to
                the same value that was provided in the CreateInvocationRequest.
            create_if_not_found (bool): If true then the Update operation will become a Create operation if
                the FileSet is NOT_FOUND.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.devtools.resultstore.v2.types.FileSet` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'update_file_set' not in self._inner_api_calls:
            self._inner_api_calls['update_file_set'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.update_file_set,
                default_retry=self._method_configs['UpdateFileSet'].retry,
                default_timeout=self._method_configs['UpdateFileSet'].timeout,
                client_info=self._client_info,
            )

        request = resultstore_upload_pb2.UpdateFileSetRequest(
            file_set=file_set,
            update_mask=update_mask,
            authorization_token=authorization_token,
            create_if_not_found=create_if_not_found,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [('file_set.name', file_set.name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(routing_header)
            metadata.append(routing_metadata)

        return self._inner_api_calls['update_file_set'](request, retry=retry, timeout=timeout, metadata=metadata)

    def merge_file_set(
            self,
            request_id=None,
            file_set=None,
            update_mask=None,
            authorization_token=None,
            create_if_not_found=None,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Applies a merge update to the file set identified by the given proto's
        name. For primitive and message fields, updates them with the ones in the
        given proto if they are covered under the field mask paths. For repeated
        fields, merges to them with the given ones if they are covered under the
        field mask paths. This is not an implicitly idempotent API, so a request
        id is required to make it idempotent.

        Returns an empty FileSet proto with only the name and ID fields populated.


        An error will be reported in the following cases:
        - If the file set does not exist.
        - If the parent invocation is finalized.
        - If a given field mask path is not valid.
        - If no field mask was given.

        Example:
            >>> from google.cloud.devtools.resultstore import v2
            >>>
            >>> client = v2.ResultStoreUploadClient()
            >>>
            >>> response = client.merge_file_set()

        Args:
            request_id (str): A unique identifier for this request. Must be set to a different value for
                each request that affects a given resource (eg. a random UUID). Required
                for the operation to be idempotent. This is achieved by ignoring this
                request if the last successful operation on the resource had the same
                request ID.  Restricted to 36 Unicode characters.
            file_set (Union[dict, ~google.cloud.devtools.resultstore.v2.types.FileSet]): Contains the name and fields of the file set to be merged. The name
                format must be:
                invocations/${INVOCATION_ID}/fileSets/${url_encode(FILE_SET_ID)}

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.devtools.resultstore.v2.types.FileSet`
            update_mask (Union[dict, ~google.cloud.devtools.resultstore.v2.types.FieldMask]): Indicates which fields to merge.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.devtools.resultstore.v2.types.FieldMask`
            authorization_token (str): This is a token to authorize access to this invocation. It must be set to
                the same value that was provided in the CreateInvocationRequest.
            create_if_not_found (bool): If true then the Merge operation will become a Create operation if
                the FileSet is NOT_FOUND.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.devtools.resultstore.v2.types.FileSet` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'merge_file_set' not in self._inner_api_calls:
            self._inner_api_calls['merge_file_set'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.merge_file_set,
                default_retry=self._method_configs['MergeFileSet'].retry,
                default_timeout=self._method_configs['MergeFileSet'].timeout,
                client_info=self._client_info,
            )

        request = resultstore_upload_pb2.MergeFileSetRequest(
            request_id=request_id,
            file_set=file_set,
            update_mask=update_mask,
            authorization_token=authorization_token,
            create_if_not_found=create_if_not_found,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [('file_set.name', file_set.name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(routing_header)
            metadata.append(routing_metadata)

        return self._inner_api_calls['merge_file_set'](request, retry=retry, timeout=timeout, metadata=metadata)

    def upload_batch(
            self,
            parent=None,
            authorization_token=None,
            next_resume_token=None,
            resume_token=None,
            uploader_state=None,
            upload_requests=None,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        This is the RPC used for batch upload. It supports uploading
        multiple resources for an invocation in a transaction safe manner.

        To use this RPC, the CreateInvocationRequest must have been provided a
        resume_token.

        Combining batch upload with normal upload on a single Invocation is not
        supported. If an Invocation is created with a resume_token, all further
        calls must be through UploadBatch. If an Invocation is created without
        resume_token normal upload, all further upload calls must be through
        normal upload RPCs.

        Example:
            >>> from google.cloud.devtools.resultstore import v2
            >>>
            >>> client = v2.ResultStoreUploadClient()
            >>>
            >>> response = client.upload_batch()

        Args:
            parent (str): Required. The name of the invocation being modified. The name format
                must be: invocations/${INVOCATION_ID}
            authorization_token (str): Required. A UUID that must match the value provided in CreateInvocationRequest.
            next_resume_token (str): Required. The token of this batch, that will be committed in this
                UploadBatchRequest. If this matches the previously uploaded
                resume_token, then this request will silently do nothing. See
                CreateInvocationRequest.initial_resume_token for more information. Must
                be web safe Base64 encoded bytes.
            resume_token (str): Required. The token of the previous batch that was committed in a
                UploadBatchRequest. This will be checked after next_resume_token match
                is checked. If this does not match the previously uploaded resume_token,
                a 409 Conflict (HTTPS) or ABORTED (gRPC ) error code indicating a
                concurrency failure will be returned, and that the user should call
                GetInvocationUploadMetadata to fetch the current resume_token to
                reconstruct the state of the upload to resume it. See
                CreateInvocationRequest.initial_resume_token for more information. Must
                be web safe Base64 encoded bytes.
            uploader_state (bytes): Client-specific data used to resume batch upload if an error occurs
                and retry is needed. This serves a role closely related to resume_token,
                as both fields may be used to provide state required to restore a Batch
                Upload, but they differ in two important aspects:

                -  it is not compared to previous values, and as such does not provide
                   concurrency control;
                -  it allows for a larger payload, since the contents are never
                   inspected/compared; The size of the message must be within 1 MiB. Too
                   large requests will be rejected.
            upload_requests (list[Union[dict, ~google.cloud.devtools.resultstore.v2.types.UploadRequest]]): The individual upload requests for this batch.
                The recommend total size for a batch is 10 MiB. Too large requests may be
                rejected.
                This field may be empty, allowing this RPC to be used like TouchInvocation.

                If a dict is provided, it must be of the same form as the protobuf
                message :class:`~google.cloud.devtools.resultstore.v2.types.UploadRequest`
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.devtools.resultstore.v2.types.UploadBatchResponse` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'upload_batch' not in self._inner_api_calls:
            self._inner_api_calls['upload_batch'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.upload_batch,
                default_retry=self._method_configs['UploadBatch'].retry,
                default_timeout=self._method_configs['UploadBatch'].timeout,
                client_info=self._client_info,
            )

        request = resultstore_upload_pb2.UploadBatchRequest(
            parent=parent,
            authorization_token=authorization_token,
            next_resume_token=next_resume_token,
            resume_token=resume_token,
            uploader_state=uploader_state,
            upload_requests=upload_requests,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [('parent', parent)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(routing_header)
            metadata.append(routing_metadata)

        return self._inner_api_calls['upload_batch'](request, retry=retry, timeout=timeout, metadata=metadata)

    def get_invocation_upload_metadata(
            self,
            name=None,
            authorization_token=None,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Provides a way to read the metadata for an invocation.
        The UploadMetadata could still be retrieved by this RPC even the Invocation
        has been finalized.
        This API requires setting a response FieldMask via 'fields' URL query
        parameter or X-Goog-FieldMask HTTP/gRPC header.

        An error will be reported in the following case:
        - If the invocation does not exist.
        - If no field mask was given.

        Example:
            >>> from google.cloud.devtools.resultstore import v2
            >>>
            >>> client = v2.ResultStoreUploadClient()
            >>>
            >>> response = client.get_invocation_upload_metadata()

        Args:
            name (str): Required The name of the UploadMetadata being requested. The name
                format must be: invocations/${INVOCATION_ID}/uploadMetadata
            authorization_token (str): Required. A UUID that must match the value provided in CreateInvocationRequest.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.devtools.resultstore.v2.types.UploadMetadata` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'get_invocation_upload_metadata' not in self._inner_api_calls:
            self._inner_api_calls['get_invocation_upload_metadata'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.get_invocation_upload_metadata,
                default_retry=self._method_configs['GetInvocationUploadMetadata'].retry,
                default_timeout=self._method_configs['GetInvocationUploadMetadata'].timeout,
                client_info=self._client_info,
            )

        request = resultstore_upload_pb2.GetInvocationUploadMetadataRequest(
            name=name,
            authorization_token=authorization_token,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [('name', name)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(routing_header)
            metadata.append(routing_metadata)

        return self._inner_api_calls['get_invocation_upload_metadata'](request, retry=retry, timeout=timeout, metadata=metadata)
