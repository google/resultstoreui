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


import google.api_core.grpc_helpers

from google.cloud.devtools.resultstore.v2.proto import resultstore_download_pb2_grpc


class ResultStoreDownloadGrpcTransport(object):
    """gRPC transport class providing stubs for
    google.devtools.resultstore.v2 ResultStoreDownload API.

    The transport provides access to the raw gRPC stubs,
    which can be used to take advantage of advanced
    features of gRPC.
    """
    # The scopes needed to make gRPC calls to all of the methods defined
    # in this service.
    _OAUTH_SCOPES = (
        'https://www.googleapis.com/auth/cloud-platform',
    )

    def __init__(self, channel=None, credentials=None,
                 address='resultstore.googleapis.com:443'):
        """Instantiate the transport class.

        Args:
            channel (grpc.Channel): A ``Channel`` instance through
                which to make calls. This argument is mutually exclusive
                with ``credentials``; providing both will raise an exception.
            credentials (google.auth.credentials.Credentials): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If none
                are specified, the client will attempt to ascertain the
                credentials from the environment.
            address (str): The address where the service is hosted.
        """
        # If both `channel` and `credentials` are specified, raise an
        # exception (channels come with credentials baked in already).
        if channel is not None and credentials is not None:
            raise ValueError(
                'The `channel` and `credentials` arguments are mutually '
                'exclusive.',
            )

        # Create the channel.
        if channel is None:
            channel = self.create_channel(
                address=address,
                credentials=credentials,
                options={
                    'grpc.max_send_message_length': -1,
                    'grpc.max_receive_message_length': -1,
                }.items(),
            )

        self._channel = channel

        # gRPC uses objects called "stubs" that are bound to the
        # channel and provide a basic method for each RPC.
        self._stubs = {
            'result_store_download_stub': resultstore_download_pb2_grpc.ResultStoreDownloadStub(channel),
        }


    @classmethod
    def create_channel(
                cls,
                address='resultstore.googleapis.com:443',
                credentials=None,
                **kwargs):
        """Create and return a gRPC channel object.

        Args:
            address (str): The host for the channel to use.
            credentials (~.Credentials): The
                authorization credentials to attach to requests. These
                credentials identify this application to the service. If
                none are specified, the client will attempt to ascertain
                the credentials from the environment.
            kwargs (dict): Keyword arguments, which are passed to the
                channel creation.

        Returns:
            grpc.Channel: A gRPC channel object.
        """
        return google.api_core.grpc_helpers.create_channel(
            address,
            credentials=credentials,
            scopes=cls._OAUTH_SCOPES,
            **kwargs
        )

    @property
    def channel(self):
        """The gRPC channel used by the transport.

        Returns:
            grpc.Channel: A gRPC channel object.
        """
        return self._channel

    @property
    def get_invocation(self):
        """Return the gRPC stub for :meth:`ResultStoreDownloadClient.get_invocation`.

        Retrieves the invocation with the given name.

        An error will be reported in the following cases:
        - If the invocation is not found.
        - If the given invocation name is badly formatted.
        - If no field mask was given.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs['result_store_download_stub'].GetInvocation

    @property
    def search_invocations(self):
        """Return the gRPC stub for :meth:`ResultStoreDownloadClient.search_invocations`.

        Searches for invocations matching the given query parameters.
        Results will be ordered by timing.start_time with most recent first, but
        total ordering of results is not guaranteed when difference in
        timestamps is very small. Results may be stale.

        An error will be reported in the following cases:

        -  If a query string is not provided
        -  If no field mask was given.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs['result_store_download_stub'].SearchInvocations

    @property
    def get_invocation_download_metadata(self):
        """Return the gRPC stub for :meth:`ResultStoreDownloadClient.get_invocation_download_metadata`.

        Retrieves the metadata for an invocation with the given name.

        An error will be reported in the following cases:
        - If the invocation is not found.
        - If the given invocation name is badly formatted.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs['result_store_download_stub'].GetInvocationDownloadMetadata

    @property
    def get_configuration(self):
        """Return the gRPC stub for :meth:`ResultStoreDownloadClient.get_configuration`.

        Retrieves the configuration with the given name.

        An error will be reported in the following cases:
        - If the configuration or its parent invocation is not found.
        - If the given configuration name is badly formatted.
        - If no field mask was given.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs['result_store_download_stub'].GetConfiguration

    @property
    def list_configurations(self):
        """Return the gRPC stub for :meth:`ResultStoreDownloadClient.list_configurations`.

        Retrieves all configurations for a parent invocation.
        This might be limited by user or server,
        in which case a continuation token is provided.
        The order in which results are returned is undefined, but stable.

        An error will be reported in the following cases:
        - If the parent invocation is not found.
        - If the given parent invocation name is badly formatted.
        - If no field mask was given.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs['result_store_download_stub'].ListConfigurations

    @property
    def get_target(self):
        """Return the gRPC stub for :meth:`ResultStoreDownloadClient.get_target`.

        Retrieves the target with the given name.

        An error will be reported in the following cases:
        - If the target or its parent invocation is not found.
        - If the given target name is badly formatted.
        - If no field mask was given.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs['result_store_download_stub'].GetTarget

    @property
    def list_targets(self):
        """Return the gRPC stub for :meth:`ResultStoreDownloadClient.list_targets`.

        Retrieves all targets for a parent invocation.  This might be limited by
        user or server, in which case a continuation token is provided.
        The order in which results are returned is undefined, but stable.

        An error will be reported in the following cases:
        - If the parent is not found.
        - If the given parent name is badly formatted.
        - If no field mask was given.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs['result_store_download_stub'].ListTargets

    @property
    def get_configured_target(self):
        """Return the gRPC stub for :meth:`ResultStoreDownloadClient.get_configured_target`.

        Retrieves the configured target with the given name.

        An error will be reported in the following cases:
        - If the configured target is not found.
        - If the given name is badly formatted.
        - If no field mask was given.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs['result_store_download_stub'].GetConfiguredTarget

    @property
    def list_configured_targets(self):
        """Return the gRPC stub for :meth:`ResultStoreDownloadClient.list_configured_targets`.

        Retrieves all configured targets for a parent invocation/target.
        This might be limited by user or server, in which case a continuation
        token is provided.  Supports '-' for targetId meaning all targets.
        The order in which results are returned is undefined, but stable.

        An error will be reported in the following cases:
        - If the parent is not found.
        - If the given parent name is badly formatted.
        - If no field mask was given.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs['result_store_download_stub'].ListConfiguredTargets

    @property
    def get_action(self):
        """Return the gRPC stub for :meth:`ResultStoreDownloadClient.get_action`.

        Retrieves the action with the given name.

        An error will be reported in the following cases:
        - If the action is not found.
        - If the given name is badly formatted.
        - If no field mask was given.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs['result_store_download_stub'].GetAction

    @property
    def list_actions(self):
        """Return the gRPC stub for :meth:`ResultStoreDownloadClient.list_actions`.

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

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs['result_store_download_stub'].ListActions

    @property
    def get_file_set(self):
        """Return the gRPC stub for :meth:`ResultStoreDownloadClient.get_file_set`.

        Retrieves the file set with the given name.

        An error will be reported in the following cases:
        - If the file set or its parent invocation is not found.
        - If the given file set name is badly formatted.
        - If no field mask was given.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs['result_store_download_stub'].GetFileSet

    @property
    def list_file_sets(self):
        """Return the gRPC stub for :meth:`ResultStoreDownloadClient.list_file_sets`.

        Retrieves all file sets for a parent invocation.
        This might be limited by user or server,
        in which case a continuation token is provided.
        The order in which results are returned is undefined, but stable.

        An error will be reported in the following cases:
        - If the parent invocation is not found.
        - If the given parent invocation name is badly formatted.
        - If no field mask was given.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs['result_store_download_stub'].ListFileSets

    @property
    def traverse_file_sets(self):
        """Return the gRPC stub for :meth:`ResultStoreDownloadClient.traverse_file_sets`.

        Returns the transitive closure of FileSets. This might be limited by
        user or server, in which case a continuation token is provided. The
        order in which results are returned is undefined, and unstable.

        An error will be reported in the following cases:

        -  If page_token is too large to continue the calculation.
        -  If the resource is not found.
        -  If the given resource name is badly formatted.
        -  If no field mask was given.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs['result_store_download_stub'].TraverseFileSets