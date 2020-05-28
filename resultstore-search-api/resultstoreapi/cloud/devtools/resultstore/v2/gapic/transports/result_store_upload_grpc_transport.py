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

from google.cloud.devtools.resultstore.v2.proto import resultstore_upload_pb2_grpc


class ResultStoreUploadGrpcTransport(object):
    """gRPC transport class providing stubs for
    google.devtools.resultstore.v2 ResultStoreUpload API.

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
            'result_store_upload_stub': resultstore_upload_pb2_grpc.ResultStoreUploadStub(channel),
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
    def create_invocation(self):
        """Return the gRPC stub for :meth:`ResultStoreUploadClient.create_invocation`.

        Creates the given invocation.

        This is not an implicitly idempotent API, so a request id is required to
        make it idempotent.

        Returns an empty Invocation proto with only the name and ID fields
        populated.

        An error will be reported in the following cases:
        - If an invocation with the same ID already exists.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs['result_store_upload_stub'].CreateInvocation

    @property
    def update_invocation(self):
        """Return the gRPC stub for :meth:`ResultStoreUploadClient.update_invocation`.

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

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs['result_store_upload_stub'].UpdateInvocation

    @property
    def merge_invocation(self):
        """Return the gRPC stub for :meth:`ResultStoreUploadClient.merge_invocation`.

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

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs['result_store_upload_stub'].MergeInvocation

    @property
    def touch_invocation(self):
        """Return the gRPC stub for :meth:`ResultStoreUploadClient.touch_invocation`.

        Touches the invocation identified by the given proto's name.

        This is useful when you need to notify ResultStore that you haven't
        abandoned the upload, since abandoned uploads will be automatically
        finalized after a set period.

        An error will be reported in the following cases:
        - If the invocation does not exist.
        - If the invocation is finalized.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs['result_store_upload_stub'].TouchInvocation

    @property
    def finalize_invocation(self):
        """Return the gRPC stub for :meth:`ResultStoreUploadClient.finalize_invocation`.

        Declares the invocation with the given name as finalized and immutable by
        the user. It may still be mutated by post-processing. This is an implicitly
        idempotent API.

        If an Invocation is not updated for 24 hours, some time after that
        this will be called automatically.

        An error will be reported in the following cases:
        - If the invocation does not exist.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs['result_store_upload_stub'].FinalizeInvocation

    @property
    def delete_invocation(self):
        """Return the gRPC stub for :meth:`ResultStoreUploadClient.delete_invocation`.

        Deletes an immutable invocation (permanently)
        Note: this does not delete indirect data, e.g. files stored in other
        services.

        An error will be reported in the following cases:
        - If the invocation does not exist.
        - If the invocation is not finalized.  This can be retried until it is.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs['result_store_upload_stub'].DeleteInvocation

    @property
    def create_target(self):
        """Return the gRPC stub for :meth:`ResultStoreUploadClient.create_target`.

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

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs['result_store_upload_stub'].CreateTarget

    @property
    def update_target(self):
        """Return the gRPC stub for :meth:`ResultStoreUploadClient.update_target`.

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

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs['result_store_upload_stub'].UpdateTarget

    @property
    def merge_target(self):
        """Return the gRPC stub for :meth:`ResultStoreUploadClient.merge_target`.

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

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs['result_store_upload_stub'].MergeTarget

    @property
    def finalize_target(self):
        """Return the gRPC stub for :meth:`ResultStoreUploadClient.finalize_target`.

        Declares the target with the given name as finalized and immutable by the
        user. It may still be mutated by post-processing. This is an implicitly
        idempotent API.

        An error will be reported in the following cases:
        - If the target does not exist.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs['result_store_upload_stub'].FinalizeTarget

    @property
    def create_configured_target(self):
        """Return the gRPC stub for :meth:`ResultStoreUploadClient.create_configured_target`.

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

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs['result_store_upload_stub'].CreateConfiguredTarget

    @property
    def update_configured_target(self):
        """Return the gRPC stub for :meth:`ResultStoreUploadClient.update_configured_target`.

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

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs['result_store_upload_stub'].UpdateConfiguredTarget

    @property
    def merge_configured_target(self):
        """Return the gRPC stub for :meth:`ResultStoreUploadClient.merge_configured_target`.

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

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs['result_store_upload_stub'].MergeConfiguredTarget

    @property
    def finalize_configured_target(self):
        """Return the gRPC stub for :meth:`ResultStoreUploadClient.finalize_configured_target`.

        Declares the configured target with the given name as finalized and
        immutable by the user. It may still be mutated by post-processing. This is
        an implicitly idempotent API.

        An error will be reported in the following cases:
        - If the configured target does not exist.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs['result_store_upload_stub'].FinalizeConfiguredTarget

    @property
    def create_action(self):
        """Return the gRPC stub for :meth:`ResultStoreUploadClient.create_action`.

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

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs['result_store_upload_stub'].CreateAction

    @property
    def update_action(self):
        """Return the gRPC stub for :meth:`ResultStoreUploadClient.update_action`.

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

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs['result_store_upload_stub'].UpdateAction

    @property
    def merge_action(self):
        """Return the gRPC stub for :meth:`ResultStoreUploadClient.merge_action`.

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

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs['result_store_upload_stub'].MergeAction

    @property
    def create_configuration(self):
        """Return the gRPC stub for :meth:`ResultStoreUploadClient.create_configuration`.

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

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs['result_store_upload_stub'].CreateConfiguration

    @property
    def update_configuration(self):
        """Return the gRPC stub for :meth:`ResultStoreUploadClient.update_configuration`.

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

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs['result_store_upload_stub'].UpdateConfiguration

    @property
    def create_file_set(self):
        """Return the gRPC stub for :meth:`ResultStoreUploadClient.create_file_set`.

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

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs['result_store_upload_stub'].CreateFileSet

    @property
    def update_file_set(self):
        """Return the gRPC stub for :meth:`ResultStoreUploadClient.update_file_set`.

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

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs['result_store_upload_stub'].UpdateFileSet

    @property
    def merge_file_set(self):
        """Return the gRPC stub for :meth:`ResultStoreUploadClient.merge_file_set`.

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

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs['result_store_upload_stub'].MergeFileSet

    @property
    def upload_batch(self):
        """Return the gRPC stub for :meth:`ResultStoreUploadClient.upload_batch`.

        This is the RPC used for batch upload. It supports uploading
        multiple resources for an invocation in a transaction safe manner.

        To use this RPC, the CreateInvocationRequest must have been provided a
        resume_token.

        Combining batch upload with normal upload on a single Invocation is not
        supported. If an Invocation is created with a resume_token, all further
        calls must be through UploadBatch. If an Invocation is created without
        resume_token normal upload, all further upload calls must be through
        normal upload RPCs.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs['result_store_upload_stub'].UploadBatch

    @property
    def get_invocation_upload_metadata(self):
        """Return the gRPC stub for :meth:`ResultStoreUploadClient.get_invocation_upload_metadata`.

        Provides a way to read the metadata for an invocation.
        The UploadMetadata could still be retrieved by this RPC even the Invocation
        has been finalized.
        This API requires setting a response FieldMask via 'fields' URL query
        parameter or X-Goog-FieldMask HTTP/gRPC header.

        An error will be reported in the following case:
        - If the invocation does not exist.
        - If no field mask was given.

        Returns:
            Callable: A callable which accepts the appropriate
                deserialized request object and returns a
                deserialized response object.
        """
        return self._stubs['result_store_upload_stub'].GetInvocationUploadMetadata