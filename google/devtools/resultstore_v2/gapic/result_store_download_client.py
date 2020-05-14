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

"""Accesses the google.devtools.resultstore.v2 ResultStoreDownload API."""

import pkg_resources
import warnings

from google.oauth2 import service_account
import google.api_core.client_options
import google.api_core.gapic_v1.client_info
import google.api_core.gapic_v1.config
import google.api_core.gapic_v1.method
import google.api_core.gapic_v1.routing_header
import google.api_core.grpc_helpers
import google.api_core.protobuf_helpers
import grpc

from google.devtools.resultstore_v2.gapic import enums
from google.devtools.resultstore_v2.gapic import result_store_download_client_config
from google.devtools.resultstore_v2.gapic.transports import result_store_download_grpc_transport
from google.devtools.resultstore_v2.proto import action_pb2
from google.devtools.resultstore_v2.proto import configuration_pb2
from google.devtools.resultstore_v2.proto import configured_target_pb2
from google.devtools.resultstore_v2.proto import download_metadata_pb2
from google.devtools.resultstore_v2.proto import file_set_pb2
from google.devtools.resultstore_v2.proto import invocation_pb2
from google.devtools.resultstore_v2.proto import resultstore_download_pb2
from google.devtools.resultstore_v2.proto import resultstore_download_pb2_grpc
from google.devtools.resultstore_v2.proto import target_pb2



_GAPIC_LIBRARY_VERSION = pkg_resources.get_distribution(
    'google-cloud-devtools-resultstore',
).version


class ResultStoreDownloadClient(object):
    """
    This is the interface used to download information from the ResultStore
    database.

    Most APIs require setting a response FieldMask via the 'fields' URL query
    parameter or the X-Goog-FieldMask HTTP/gRPC header.
    """

    SERVICE_ADDRESS = 'resultstore.googleapis.com:443'
    """The default address of the service."""

    # The name of the interface for this client. This is the key used to
    # find the method configuration in the client_config dictionary.
    _INTERFACE_NAME = 'google.devtools.resultstore.v2.ResultStoreDownload'


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
            ResultStoreDownloadClient: The constructed client.
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
            transport (Union[~.ResultStoreDownloadGrpcTransport,
                    Callable[[~.Credentials, type], ~.ResultStoreDownloadGrpcTransport]): A transport
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
            client_config = result_store_download_client_config.config

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
                    default_class=result_store_download_grpc_transport.ResultStoreDownloadGrpcTransport,
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
            self.transport = result_store_download_grpc_transport.ResultStoreDownloadGrpcTransport(
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
    def get_invocation(
            self,
            name=None,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Retrieves the invocation with the given name.

        An error will be reported in the following cases:
        - If the invocation is not found.
        - If the given invocation name is badly formatted.
        - If no field mask was given.

        Example:
            >>> from google.devtools import resultstore_v2
            >>>
            >>> client = resultstore_v2.ResultStoreDownloadClient()
            >>>
            >>> response = client.get_invocation()

        Args:
            name (str): The name of the invocation to retrieve. It must match this format:
                invocations/${INVOCATION_ID} where INVOCATION_ID must be an RFC
                4122-compliant random UUID.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.devtools.resultstore_v2.types.Invocation` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'get_invocation' not in self._inner_api_calls:
            self._inner_api_calls['get_invocation'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.get_invocation,
                default_retry=self._method_configs['GetInvocation'].retry,
                default_timeout=self._method_configs['GetInvocation'].timeout,
                client_info=self._client_info,
            )

        request = resultstore_download_pb2.GetInvocationRequest(
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

        return self._inner_api_calls['get_invocation'](request, retry=retry, timeout=timeout, metadata=metadata)

    def search_invocations(
            self,
            page_size=None,
            page_token=None,
            offset=None,
            query=None,
            project_id=None,
            exact_match=None,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Searches for invocations matching the given query parameters.
        Results will be ordered by timing.start_time with most recent first, but
        total ordering of results is not guaranteed when difference in
        timestamps is very small. Results may be stale.

        An error will be reported in the following cases:

        -  If a query string is not provided
        -  If no field mask was given.

        Example:
            >>> from google.devtools import resultstore_v2
            >>>
            >>> client = resultstore_v2.ResultStoreDownloadClient()
            >>>
            >>> response = client.search_invocations()

        Args:
            page_size (int): The maximum number of items to return. Zero means all, but may be capped by
                the server.
            page_token (str): The next_page_token value returned from a previous Search request,
                if any.
            offset (long): Absolute number of results to skip. May be rejected if too high.
            query (str): A filtering query string.

                Only a limited number of fields and operators are supported. Not every
                field supports every operator.

                Fields that support equals ("=") restrictions:

                name status_attributes.status workspace_info.hostname

                Fields that support contains (":") restrictions:

                invocation_attributes.users invocation_attributes.labels

                Fields that support comparison ("<", "<=", ">", ">=") restrictions;

                timing.start_time

                Supported custom function global restrictions:

                propertyEquals("key", "value")
            project_id (str): The project id to search under.
            exact_match (bool): If true, all equals or contains restrictions on string fields in query will
                require exact match. Otherwise, a string field restriction may ignore case
                and punctuation.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.devtools.resultstore_v2.types.SearchInvocationsResponse` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'search_invocations' not in self._inner_api_calls:
            self._inner_api_calls['search_invocations'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.search_invocations,
                default_retry=self._method_configs['SearchInvocations'].retry,
                default_timeout=self._method_configs['SearchInvocations'].timeout,
                client_info=self._client_info,
            )

        # Sanity check: We have some fields which are mutually exclusive;
        # raise ValueError if more than one is sent.
        google.api_core.protobuf_helpers.check_oneof(
            page_token=page_token,
            offset=offset,
        )

        request = resultstore_download_pb2.SearchInvocationsRequest(
            page_size=page_size,
            page_token=page_token,
            offset=offset,
            query=query,
            project_id=project_id,
            exact_match=exact_match,
        )
        return self._inner_api_calls['search_invocations'](request, retry=retry, timeout=timeout, metadata=metadata)

    def get_invocation_download_metadata(
            self,
            name=None,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Retrieves the metadata for an invocation with the given name.

        An error will be reported in the following cases:
        - If the invocation is not found.
        - If the given invocation name is badly formatted.

        Example:
            >>> from google.devtools import resultstore_v2
            >>>
            >>> client = resultstore_v2.ResultStoreDownloadClient()
            >>>
            >>> response = client.get_invocation_download_metadata()

        Args:
            name (str): The name of the download metadata to retrieve. It must match this
                format: invocations/${INVOCATION_ID}/downloadMetadata where
                INVOCATION_ID must be an RFC 4122-compliant random UUID.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.devtools.resultstore_v2.types.DownloadMetadata` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'get_invocation_download_metadata' not in self._inner_api_calls:
            self._inner_api_calls['get_invocation_download_metadata'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.get_invocation_download_metadata,
                default_retry=self._method_configs['GetInvocationDownloadMetadata'].retry,
                default_timeout=self._method_configs['GetInvocationDownloadMetadata'].timeout,
                client_info=self._client_info,
            )

        request = resultstore_download_pb2.GetInvocationDownloadMetadataRequest(
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

        return self._inner_api_calls['get_invocation_download_metadata'](request, retry=retry, timeout=timeout, metadata=metadata)

    def get_configuration(
            self,
            name=None,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Retrieves the configuration with the given name.

        An error will be reported in the following cases:
        - If the configuration or its parent invocation is not found.
        - If the given configuration name is badly formatted.
        - If no field mask was given.

        Example:
            >>> from google.devtools import resultstore_v2
            >>>
            >>> client = resultstore_v2.ResultStoreDownloadClient()
            >>>
            >>> response = client.get_configuration()

        Args:
            name (str): The name of the configuration to retrieve. It must match this
                format:
                invocations/${INVOCATION_ID}/configs/${url_encode(CONFIGURATION_ID)}
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.devtools.resultstore_v2.types.Configuration` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'get_configuration' not in self._inner_api_calls:
            self._inner_api_calls['get_configuration'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.get_configuration,
                default_retry=self._method_configs['GetConfiguration'].retry,
                default_timeout=self._method_configs['GetConfiguration'].timeout,
                client_info=self._client_info,
            )

        request = resultstore_download_pb2.GetConfigurationRequest(
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

        return self._inner_api_calls['get_configuration'](request, retry=retry, timeout=timeout, metadata=metadata)

    def list_configurations(
            self,
            parent=None,
            page_size=None,
            page_token=None,
            offset=None,
            filter_=None,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Retrieves all configurations for a parent invocation.
        This might be limited by user or server,
        in which case a continuation token is provided.
        The order in which results are returned is undefined, but stable.

        An error will be reported in the following cases:
        - If the parent invocation is not found.
        - If the given parent invocation name is badly formatted.
        - If no field mask was given.

        Example:
            >>> from google.devtools import resultstore_v2
            >>>
            >>> client = resultstore_v2.ResultStoreDownloadClient()
            >>>
            >>> response = client.list_configurations()

        Args:
            parent (str): The invocation name of the configurations to retrieve. It must match
                this format: invocations/${INVOCATION_ID}
            page_size (int): The maximum number of items to return.
                Zero means all, but may be capped by the server.
            page_token (str): The next_page_token value returned from a previous List request, if
                any.
            offset (long): Absolute number of results to skip.
            filter_ (str): A filter to return only resources that match it. Any fields used in
                the filter must be also specified in the field mask. May cause pages
                with 0 results and a next_page_token to be returned.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.devtools.resultstore_v2.types.ListConfigurationsResponse` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'list_configurations' not in self._inner_api_calls:
            self._inner_api_calls['list_configurations'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.list_configurations,
                default_retry=self._method_configs['ListConfigurations'].retry,
                default_timeout=self._method_configs['ListConfigurations'].timeout,
                client_info=self._client_info,
            )

        # Sanity check: We have some fields which are mutually exclusive;
        # raise ValueError if more than one is sent.
        google.api_core.protobuf_helpers.check_oneof(
            page_token=page_token,
            offset=offset,
        )

        request = resultstore_download_pb2.ListConfigurationsRequest(
            parent=parent,
            page_size=page_size,
            page_token=page_token,
            offset=offset,
            filter=filter_,
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

        return self._inner_api_calls['list_configurations'](request, retry=retry, timeout=timeout, metadata=metadata)

    def get_target(
            self,
            name=None,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Retrieves the target with the given name.

        An error will be reported in the following cases:
        - If the target or its parent invocation is not found.
        - If the given target name is badly formatted.
        - If no field mask was given.

        Example:
            >>> from google.devtools import resultstore_v2
            >>>
            >>> client = resultstore_v2.ResultStoreDownloadClient()
            >>>
            >>> response = client.get_target()

        Args:
            name (str): The name of the target to retrieve. It must match this format:
                invocations/${INVOCATION_ID}/targets/${url_encode(TARGET_ID)}
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.devtools.resultstore_v2.types.Target` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'get_target' not in self._inner_api_calls:
            self._inner_api_calls['get_target'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.get_target,
                default_retry=self._method_configs['GetTarget'].retry,
                default_timeout=self._method_configs['GetTarget'].timeout,
                client_info=self._client_info,
            )

        request = resultstore_download_pb2.GetTargetRequest(
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

        return self._inner_api_calls['get_target'](request, retry=retry, timeout=timeout, metadata=metadata)

    def list_targets(
            self,
            parent=None,
            page_size=None,
            page_token=None,
            offset=None,
            filter_=None,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Retrieves all targets for a parent invocation.  This might be limited by
        user or server, in which case a continuation token is provided.
        The order in which results are returned is undefined, but stable.

        An error will be reported in the following cases:
        - If the parent is not found.
        - If the given parent name is badly formatted.
        - If no field mask was given.

        Example:
            >>> from google.devtools import resultstore_v2
            >>>
            >>> client = resultstore_v2.ResultStoreDownloadClient()
            >>>
            >>> response = client.list_targets()

        Args:
            parent (str): The invocation name of the targets to retrieve. It must match this
                format: invocations/${INVOCATION_ID}
            page_size (int): The maximum number of items to return.
                Zero means all, but may be capped by the server.
            page_token (str): The next_page_token value returned from a previous List request, if
                any.
            offset (long): Absolute number of results to skip.
            filter_ (str): A filter to return only resources that match it. Any fields used in
                the filter must be also specified in the field mask. May cause pages
                with 0 results and a next_page_token to be returned.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.devtools.resultstore_v2.types.ListTargetsResponse` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'list_targets' not in self._inner_api_calls:
            self._inner_api_calls['list_targets'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.list_targets,
                default_retry=self._method_configs['ListTargets'].retry,
                default_timeout=self._method_configs['ListTargets'].timeout,
                client_info=self._client_info,
            )

        # Sanity check: We have some fields which are mutually exclusive;
        # raise ValueError if more than one is sent.
        google.api_core.protobuf_helpers.check_oneof(
            page_token=page_token,
            offset=offset,
        )

        request = resultstore_download_pb2.ListTargetsRequest(
            parent=parent,
            page_size=page_size,
            page_token=page_token,
            offset=offset,
            filter=filter_,
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

        return self._inner_api_calls['list_targets'](request, retry=retry, timeout=timeout, metadata=metadata)

    def get_configured_target(
            self,
            name=None,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Retrieves the configured target with the given name.

        An error will be reported in the following cases:
        - If the configured target is not found.
        - If the given name is badly formatted.
        - If no field mask was given.

        Example:
            >>> from google.devtools import resultstore_v2
            >>>
            >>> client = resultstore_v2.ResultStoreDownloadClient()
            >>>
            >>> response = client.get_configured_target()

        Args:
            name (str): The name of the configured target to retrieve. It must match this
                format:
                invocations/${INVOCATION_ID}/targets/${url_encode(TARGET_ID)}/configuredTargets/${url_encode(CONFIGURATION_ID)}
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.devtools.resultstore_v2.types.ConfiguredTarget` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'get_configured_target' not in self._inner_api_calls:
            self._inner_api_calls['get_configured_target'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.get_configured_target,
                default_retry=self._method_configs['GetConfiguredTarget'].retry,
                default_timeout=self._method_configs['GetConfiguredTarget'].timeout,
                client_info=self._client_info,
            )

        request = resultstore_download_pb2.GetConfiguredTargetRequest(
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

        return self._inner_api_calls['get_configured_target'](request, retry=retry, timeout=timeout, metadata=metadata)

    def list_configured_targets(
            self,
            parent=None,
            page_size=None,
            page_token=None,
            offset=None,
            filter_=None,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Retrieves all configured targets for a parent invocation/target.
        This might be limited by user or server, in which case a continuation
        token is provided.  Supports '-' for targetId meaning all targets.
        The order in which results are returned is undefined, but stable.

        An error will be reported in the following cases:
        - If the parent is not found.
        - If the given parent name is badly formatted.
        - If no field mask was given.

        Example:
            >>> from google.devtools import resultstore_v2
            >>>
            >>> client = resultstore_v2.ResultStoreDownloadClient()
            >>>
            >>> response = client.list_configured_targets()

        Args:
            parent (str): The invocation and target name of the configured targets to
                retrieve. It must match this format:
                invocations/${INVOCATION_ID}/targets/${url_encode(TARGET_ID)} Supports
                '-' for ${TARGET_ID} meaning all targets.
            page_size (int): The maximum number of items to return.
                Zero means all, but may be capped by the server.
            page_token (str): The next_page_token value returned from a previous List request, if
                any.
            offset (long): Absolute number of results to skip.
            filter_ (str): A filter to return only resources that match it. Any fields used in
                the filter must be also specified in the field mask. May cause pages
                with 0 results and a next_page_token to be returned.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.devtools.resultstore_v2.types.ListConfiguredTargetsResponse` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'list_configured_targets' not in self._inner_api_calls:
            self._inner_api_calls['list_configured_targets'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.list_configured_targets,
                default_retry=self._method_configs['ListConfiguredTargets'].retry,
                default_timeout=self._method_configs['ListConfiguredTargets'].timeout,
                client_info=self._client_info,
            )

        # Sanity check: We have some fields which are mutually exclusive;
        # raise ValueError if more than one is sent.
        google.api_core.protobuf_helpers.check_oneof(
            page_token=page_token,
            offset=offset,
        )

        request = resultstore_download_pb2.ListConfiguredTargetsRequest(
            parent=parent,
            page_size=page_size,
            page_token=page_token,
            offset=offset,
            filter=filter_,
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

        return self._inner_api_calls['list_configured_targets'](request, retry=retry, timeout=timeout, metadata=metadata)

    def get_action(
            self,
            name=None,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Retrieves the action with the given name.

        An error will be reported in the following cases:
        - If the action is not found.
        - If the given name is badly formatted.
        - If no field mask was given.

        Example:
            >>> from google.devtools import resultstore_v2
            >>>
            >>> client = resultstore_v2.ResultStoreDownloadClient()
            >>>
            >>> response = client.get_action()

        Args:
            name (str): The name of the action to retrieve. It must match this format:
                invocations/${INVOCATION_ID}/targets/${url_encode(TARGET_ID)}/configuredTargets/${url_encode(CONFIGURATION_ID)}/actions/${url_encode(ACTION_ID)}
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.devtools.resultstore_v2.types.Action` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'get_action' not in self._inner_api_calls:
            self._inner_api_calls['get_action'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.get_action,
                default_retry=self._method_configs['GetAction'].retry,
                default_timeout=self._method_configs['GetAction'].timeout,
                client_info=self._client_info,
            )

        request = resultstore_download_pb2.GetActionRequest(
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

        return self._inner_api_calls['get_action'](request, retry=retry, timeout=timeout, metadata=metadata)

    def list_actions(
            self,
            parent=None,
            page_size=None,
            page_token=None,
            offset=None,
            filter_=None,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Retrieves all actions for a parent invocation/target/configuration.
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

        Example:
            >>> from google.devtools import resultstore_v2
            >>>
            >>> client = resultstore_v2.ResultStoreDownloadClient()
            >>>
            >>> response = client.list_actions()

        Args:
            parent (str): The invocation, target, and configuration name of the action to
                retrieve. It must match this format:
                invocations/${INVOCATION_ID}/targets/${url_encode(TARGET_ID)}/configuredTargets/${url_encode(CONFIGURATION_ID)}
                Supports '-' for ${CONFIGURATION_ID} to mean all Actions for all
                Configurations for a Target, or '-' for ${TARGET_ID} and
                ${CONFIGURATION_ID} to mean all Actions for all Configurations and all
                Targets. Does not support ${TARGET_ID} '-' with a specified
                configuration.
            page_size (int): The maximum number of items to return.
                Zero means all, but may be capped by the server.
            page_token (str): The next_page_token value returned from a previous List request, if
                any.
            offset (long): Absolute number of results to skip.
            filter_ (str): A filter to return only resources that match it. Any fields used in
                the filter must be also specified in the field mask. May cause pages
                with 0 results and a next_page_token to be returned.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.devtools.resultstore_v2.types.ListActionsResponse` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'list_actions' not in self._inner_api_calls:
            self._inner_api_calls['list_actions'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.list_actions,
                default_retry=self._method_configs['ListActions'].retry,
                default_timeout=self._method_configs['ListActions'].timeout,
                client_info=self._client_info,
            )

        # Sanity check: We have some fields which are mutually exclusive;
        # raise ValueError if more than one is sent.
        google.api_core.protobuf_helpers.check_oneof(
            page_token=page_token,
            offset=offset,
        )

        request = resultstore_download_pb2.ListActionsRequest(
            parent=parent,
            page_size=page_size,
            page_token=page_token,
            offset=offset,
            filter=filter_,
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

        return self._inner_api_calls['list_actions'](request, retry=retry, timeout=timeout, metadata=metadata)

    def get_file_set(
            self,
            name=None,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Retrieves the file set with the given name.

        An error will be reported in the following cases:
        - If the file set or its parent invocation is not found.
        - If the given file set name is badly formatted.
        - If no field mask was given.

        Example:
            >>> from google.devtools import resultstore_v2
            >>>
            >>> client = resultstore_v2.ResultStoreDownloadClient()
            >>>
            >>> response = client.get_file_set()

        Args:
            name (str): The name of the file set to retrieve. It must match this format:
                invocations/${INVOCATION_ID}/fileSets/${url_encode(FILE_SET_ID)}
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.devtools.resultstore_v2.types.FileSet` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'get_file_set' not in self._inner_api_calls:
            self._inner_api_calls['get_file_set'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.get_file_set,
                default_retry=self._method_configs['GetFileSet'].retry,
                default_timeout=self._method_configs['GetFileSet'].timeout,
                client_info=self._client_info,
            )

        request = resultstore_download_pb2.GetFileSetRequest(
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

        return self._inner_api_calls['get_file_set'](request, retry=retry, timeout=timeout, metadata=metadata)

    def list_file_sets(
            self,
            parent=None,
            page_size=None,
            page_token=None,
            offset=None,
            filter_=None,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Retrieves all file sets for a parent invocation.
        This might be limited by user or server,
        in which case a continuation token is provided.
        The order in which results are returned is undefined, but stable.

        An error will be reported in the following cases:
        - If the parent invocation is not found.
        - If the given parent invocation name is badly formatted.
        - If no field mask was given.

        Example:
            >>> from google.devtools import resultstore_v2
            >>>
            >>> client = resultstore_v2.ResultStoreDownloadClient()
            >>>
            >>> response = client.list_file_sets()

        Args:
            parent (str): The invocation name of the file sets to retrieve. It must match this
                format: invocations/${INVOCATION_ID}
            page_size (int): The maximum number of items to return.
                Zero means all, but may be capped by the server.
            page_token (str): The next_page_token value returned from a previous List request, if
                any.
            offset (long): Absolute number of results to skip.
            filter_ (str): A filter to return only resources that match it. Any fields used in
                the filter must be also specified in the field mask. May cause pages
                with 0 results and a next_page_token to be returned.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.devtools.resultstore_v2.types.ListFileSetsResponse` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'list_file_sets' not in self._inner_api_calls:
            self._inner_api_calls['list_file_sets'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.list_file_sets,
                default_retry=self._method_configs['ListFileSets'].retry,
                default_timeout=self._method_configs['ListFileSets'].timeout,
                client_info=self._client_info,
            )

        # Sanity check: We have some fields which are mutually exclusive;
        # raise ValueError if more than one is sent.
        google.api_core.protobuf_helpers.check_oneof(
            page_token=page_token,
            offset=offset,
        )

        request = resultstore_download_pb2.ListFileSetsRequest(
            parent=parent,
            page_size=page_size,
            page_token=page_token,
            offset=offset,
            filter=filter_,
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

        return self._inner_api_calls['list_file_sets'](request, retry=retry, timeout=timeout, metadata=metadata)

    def traverse_file_sets(
            self,
            name=None,
            page_size=None,
            page_token=None,
            offset=None,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Returns the transitive closure of FileSets. This might be limited by
        user or server, in which case a continuation token is provided. The
        order in which results are returned is undefined, and unstable.

        An error will be reported in the following cases:

        -  If page_token is too large to continue the calculation.
        -  If the resource is not found.
        -  If the given resource name is badly formatted.
        -  If no field mask was given.

        Example:
            >>> from google.devtools import resultstore_v2
            >>>
            >>> client = resultstore_v2.ResultStoreDownloadClient()
            >>>
            >>> response = client.traverse_file_sets()

        Args:
            name (str): The name of the resource to traverse. It must match one of the
                following formats:

                invocations/${INVOCATION_ID}/fileSets/${url_encode(FILE_SET_ID)} This
                returns the transitive closure of FileSets referenced by the given
                FileSet, including itself.

                invocations/${INVOCATION_ID}/targets/${url_encode(TARGET_ID)}/configuredTargets/${url_encode(CONFIGURATION_ID)}/actions/${url_encode(ACTION_ID)}
                This returns the transitive closure of FileSets referenced by the given
                Action. If ${ACTION_ID} is "-", this returns the transitive closure of
                FileSets referenced by all Actions under the given ConfiguredTarget.
            page_size (int): The maximum number of items to return.
                Zero means all, but may be capped by the server.
            page_token (str): The next_page_token value returned from a previous List request, if
                any. Page tokens will become larger with every page returned, and if a
                page token becomes too large, it will no longer be possible to continue
                to calculate the transitive dependencies. The API will return a 400 Bad
                request (HTTPS), or a INVALID_ARGUMENT (gRPC ) when this happens.
            offset (long): Absolute number of results to skip.
                Not yet implemented. 0 for default.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.devtools.resultstore_v2.types.TraverseFileSetsResponse` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'traverse_file_sets' not in self._inner_api_calls:
            self._inner_api_calls['traverse_file_sets'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.traverse_file_sets,
                default_retry=self._method_configs['TraverseFileSets'].retry,
                default_timeout=self._method_configs['TraverseFileSets'].timeout,
                client_info=self._client_info,
            )

        # Sanity check: We have some fields which are mutually exclusive;
        # raise ValueError if more than one is sent.
        google.api_core.protobuf_helpers.check_oneof(
            page_token=page_token,
            offset=offset,
        )

        request = resultstore_download_pb2.TraverseFileSetsRequest(
            name=name,
            page_size=page_size,
            page_token=page_token,
            offset=offset,
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

        return self._inner_api_calls['traverse_file_sets'](request, retry=retry, timeout=timeout, metadata=metadata)
