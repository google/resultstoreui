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

"""Accesses the google.devtools.resultstore.v2 ResultStoreFileDownload API."""

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
from google.cloud.devtools.resultstore.v2.gapic import result_store_file_download_client_config
from google.cloud.devtools.resultstore.v2.gapic.transports import result_store_file_download_grpc_transport
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
from google.cloud.devtools.resultstore.v2.proto import target_pb2



_GAPIC_LIBRARY_VERSION = pkg_resources.get_distribution(
    'google-cloud-devtools-resultstore',
).version


class ResultStoreFileDownloadClient(object):
    """
    This API allows download of File messages referenced in
    ResultStore resources.
    """

    SERVICE_ADDRESS = 'resultstore.googleapis.com:443'
    """The default address of the service."""

    # The name of the interface for this client. This is the key used to
    # find the method configuration in the client_config dictionary.
    _INTERFACE_NAME = 'google.devtools.resultstore.v2.ResultStoreFileDownload'


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
            ResultStoreFileDownloadClient: The constructed client.
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
            transport (Union[~.ResultStoreFileDownloadGrpcTransport,
                    Callable[[~.Credentials, type], ~.ResultStoreFileDownloadGrpcTransport]): A transport
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
            client_config = result_store_file_download_client_config.config

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
                    default_class=result_store_file_download_grpc_transport.ResultStoreFileDownloadGrpcTransport,
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
            self.transport = result_store_file_download_grpc_transport.ResultStoreFileDownloadGrpcTransport(
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
    def get_file(
            self,
            uri=None,
            read_offset=None,
            read_limit=None,
            archive_entry=None,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Retrieves the File with the given uri.
        returns a stream of bytes to be stitched together in order.

        An error will be reported in the following cases:
        - If the File is not found.
        - If the given File uri is badly formatted.

        Example:
            >>> from google.cloud.devtools.resultstore import v2
            >>>
            >>> client = v2.ResultStoreFileDownloadClient()
            >>>
            >>> for element in client.get_file():
            ...     # process element
            ...     pass

        Args:
            uri (str): This corresponds to the uri field in the File message.
            read_offset (long): The offset for the first byte to return in the read, relative to the
                start of the resource.

                A ``read_offset`` that is negative or greater than the size of the
                resource will cause an ``OUT_OF_RANGE`` error.
            read_limit (long): The maximum number of ``data`` bytes the server is allowed to return
                in the sum of all ``ReadResponse`` messages. A ``read_limit`` of zero
                indicates that there is no limit, and a negative ``read_limit`` will
                cause an error.

                If the stream returns fewer bytes than allowed by the ``read_limit`` and
                no error occurred, the stream includes all data from the ``read_offset``
                to the end of the resource.
            archive_entry (str): Only applies if the referenced file is a known archive type (ar,
                jar, zip) The above read_offset and read_limit fields are applied to
                this entry. If this file is not an archive, INVALID_ARGUMENT is thrown.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            Iterable[~google.cloud.devtools.resultstore.v2.types.GetFileResponse].

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'get_file' not in self._inner_api_calls:
            self._inner_api_calls['get_file'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.get_file,
                default_retry=self._method_configs['GetFile'].retry,
                default_timeout=self._method_configs['GetFile'].timeout,
                client_info=self._client_info,
            )

        request = resultstore_file_download_pb2.GetFileRequest(
            uri=uri,
            read_offset=read_offset,
            read_limit=read_limit,
            archive_entry=archive_entry,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [('uri', uri)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(routing_header)
            metadata.append(routing_metadata)

        return self._inner_api_calls['get_file'](request, retry=retry, timeout=timeout, metadata=metadata)

    def get_file_tail(
            self,
            uri=None,
            read_offset=None,
            read_limit=None,
            archive_entry=None,
            retry=google.api_core.gapic_v1.method.DEFAULT,
            timeout=google.api_core.gapic_v1.method.DEFAULT,
            metadata=None):
        """
        Retrieves the tail of a File with the given uri.

        An error will be reported in the following cases:
        - If the File is not found.
        - If the given File uri is badly formatted.

        Example:
            >>> from google.cloud.devtools.resultstore import v2
            >>>
            >>> client = v2.ResultStoreFileDownloadClient()
            >>>
            >>> response = client.get_file_tail()

        Args:
            uri (str): This corresponds to the uri field in the File message.
            read_offset (long): The offset for the first byte to return in the read, relative to the
                end of the resource.

                A ``read_offset`` that is negative or greater than the size of the
                resource will cause an ``OUT_OF_RANGE`` error.
            read_limit (long): The maximum number of ``data`` bytes the server is allowed to
                return. The server will return bytes starting from the tail of the file.

                A ``read_limit`` of zero indicates that there is no limit, and a
                negative ``read_limit`` will cause an error.
            archive_entry (str): Only applies if the referenced file is a known archive type (ar,
                jar, zip) The above read_offset and read_limit fields are applied to
                this entry. If this file is not an archive, INVALID_ARGUMENT is thrown.
            retry (Optional[google.api_core.retry.Retry]):  A retry object used
                to retry requests. If ``None`` is specified, requests will
                be retried using a default configuration.
            timeout (Optional[float]): The amount of time, in seconds, to wait
                for the request to complete. Note that if ``retry`` is
                specified, the timeout applies to each individual attempt.
            metadata (Optional[Sequence[Tuple[str, str]]]): Additional metadata
                that is provided to the method.

        Returns:
            A :class:`~google.cloud.devtools.resultstore.v2.types.GetFileTailResponse` instance.

        Raises:
            google.api_core.exceptions.GoogleAPICallError: If the request
                    failed for any reason.
            google.api_core.exceptions.RetryError: If the request failed due
                    to a retryable error and retry attempts failed.
            ValueError: If the parameters are invalid.
        """
        # Wrap the transport method to add retry and timeout logic.
        if 'get_file_tail' not in self._inner_api_calls:
            self._inner_api_calls['get_file_tail'] = google.api_core.gapic_v1.method.wrap_method(
                self.transport.get_file_tail,
                default_retry=self._method_configs['GetFileTail'].retry,
                default_timeout=self._method_configs['GetFileTail'].timeout,
                client_info=self._client_info,
            )

        request = resultstore_file_download_pb2.GetFileTailRequest(
            uri=uri,
            read_offset=read_offset,
            read_limit=read_limit,
            archive_entry=archive_entry,
        )
        if metadata is None:
            metadata = []
        metadata = list(metadata)
        try:
            routing_header = [('uri', uri)]
        except AttributeError:
            pass
        else:
            routing_metadata = google.api_core.gapic_v1.routing_header.to_grpc_metadata(routing_header)
            metadata.append(routing_metadata)

        return self._inner_api_calls['get_file_tail'](request, retry=retry, timeout=timeout, metadata=metadata)
