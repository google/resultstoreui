import unittest
import grpc
from absl import flags
from absl.testing import (absltest, flagsaver)
from unittest.mock import (patch, MagicMock)
from collections import defaultdict
from resultstoreapi.cloud.devtools.resultstore_v2.proto import (
    resultstore_download_pb2_grpc, resultstore_download_pb2, invocation_pb2,
    configuration_pb2)
from resultstore_test_utils import (
    create_return_invocation,
    create_return_configuration,
    create_return_target,
    create_return_configured_target,
    create_return_action,
    create_finalized_configured_target,
    create_finalized_target,
    initialize_client,
)
from resultstoreui_utils import (get_default_configuration, get_default_target,
                                 get_default_configured_target,
                                 get_default_action)
from resultstore_client import Error
from resultstoreui import initialize_flags
from bigstore_client import BigStoreClient

TEST_UUID = 'd9910974-4d59-4fee-8188-a891de97814a'
TEST_INVOCATION_ID = 'test-invocation-id'
TEST_CONFIG_ID = 'test-config-id'
TEST_TARGET_ID = 'test-target-id'
TEST_ACTION_ID = 'test-action-id'
TEST_CURRENT_RESUME_TOKEN = 'current-resume-token'
TEST_NEXT_RESUME_TOKEN = 'next-resume-token'

UPDATE_FIELD_ERROR_MESSAGE = 'At least one update field must be provided.'
DEFAULT_RPC_ERROR = grpc.RpcError('Test gRPC error')

FLAGS = flags.FLAGS


class CreateInvocationTest(absltest.TestCase):
    @patch('resultstoreui_utils.gen_new_uuid', return_value=TEST_UUID)
    @patch(
        'resultstoreapi.cloud.devtools.resultstore_v2.proto.resultstore_upload_pb2_grpc.ResultStoreUploadStub'
    )
    def test_create_invocation_success(self, ResultStoreUploadStubMock,
                                       gen_new_uuid_mock):
        stub = ResultStoreUploadStubMock()
        stub.CreateInvocation = MagicMock(side_effect=create_return_invocation)
        client = initialize_client(FLAGS)
        res = client.create_invocation()
        self.assertEqual(res.id.invocation_id, TEST_UUID)

    @patch('resultstoreui_utils.gen_new_uuid', return_value=TEST_UUID)
    @patch(
        'resultstoreapi.cloud.devtools.resultstore_v2.proto.resultstore_upload_pb2_grpc.ResultStoreUploadStub'
    )
    def test_rpc_error(self, ResultStoreUploadStubMock, gen_new_uuid_mock):
        stub = ResultStoreUploadStubMock()
        stub.CreateInvocation = MagicMock(return_value=DEFAULT_RPC_ERROR)
        client = initialize_client(FLAGS)
        res = client.create_invocation()
        self.assertEqual(res, DEFAULT_RPC_ERROR)


class CreateConfigurationTest(absltest.TestCase):
    @patch('resultstoreui_utils.gen_new_uuid', return_value=TEST_UUID)
    @patch(
        'resultstoreapi.cloud.devtools.resultstore_v2.proto.resultstore_upload_pb2_grpc.ResultStoreUploadStub'
    )
    def test_create_configuration_success(self, ResultStoreUploadStubMock,
                                          gen_new_uuid_mock):
        stub = ResultStoreUploadStubMock()
        stub.CreateConfiguration = MagicMock(
            side_effect=create_return_configuration)
        client = initialize_client(FLAGS)
        config = get_default_configuration(TEST_INVOCATION_ID, TEST_CONFIG_ID)
        res = client.create_configuration(config)
        self.assertEqual(res.id.configuration_id, TEST_CONFIG_ID)
        self.assertEqual(
            res.name,
            "invocations/{}/configs/{}".format(TEST_INVOCATION_ID,
                                               TEST_CONFIG_ID))

    @patch('resultstoreui_utils.gen_new_uuid', return_value=TEST_UUID)
    @patch(
        'resultstoreapi.cloud.devtools.resultstore_v2.proto.resultstore_upload_pb2_grpc.ResultStoreUploadStub'
    )
    def test_rpc_error(self, ResultStoreUploadStubMock, gen_new_uuid_mock):
        stub = ResultStoreUploadStubMock()
        stub.CreateConfiguration = MagicMock(return_value=DEFAULT_RPC_ERROR)
        client = initialize_client(FLAGS)
        config = get_default_configuration(TEST_INVOCATION_ID, TEST_CONFIG_ID)
        res = client.create_configuration(config)
        self.assertEqual(res, DEFAULT_RPC_ERROR)


class CreateTargetTest(absltest.TestCase):
    @patch('resultstoreui_utils.gen_new_uuid', return_value=TEST_UUID)
    @patch(
        'resultstoreapi.cloud.devtools.resultstore_v2.proto.resultstore_upload_pb2_grpc.ResultStoreUploadStub'
    )
    def test_create_target_success(self, ResultStoreUploadStubMock,
                                   gen_new_uuid_mock):
        stub = ResultStoreUploadStubMock()
        stub.CreateTarget = MagicMock(side_effect=create_return_target)
        client = initialize_client(FLAGS)
        target = get_default_target(TEST_INVOCATION_ID, TEST_TARGET_ID)
        res = client.create_target(target)
        self.assertEqual(res.id.target_id, TEST_TARGET_ID)
        self.assertEqual(
            res.name,
            "invocations/{}/targets/{}".format(TEST_INVOCATION_ID,
                                               TEST_TARGET_ID))

    @patch('resultstoreui_utils.gen_new_uuid', return_value=TEST_UUID)
    @patch(
        'resultstoreapi.cloud.devtools.resultstore_v2.proto.resultstore_upload_pb2_grpc.ResultStoreUploadStub'
    )
    def test_rpc_error(self, ResultStoreUploadStubMock, gen_new_uuid_mock):
        stub = ResultStoreUploadStubMock()
        stub.CreateTarget = MagicMock(return_value=DEFAULT_RPC_ERROR)
        client = initialize_client(FLAGS)
        target = get_default_target(TEST_INVOCATION_ID, TEST_TARGET_ID)
        res = client.create_target(target)
        self.assertEqual(res, DEFAULT_RPC_ERROR)


class CreateConfiguredTargetTest(absltest.TestCase):
    @patch('resultstoreui_utils.gen_new_uuid', return_value=TEST_UUID)
    @patch(
        'resultstoreapi.cloud.devtools.resultstore_v2.proto.resultstore_upload_pb2_grpc.ResultStoreUploadStub'
    )
    def test_create_configured_target_success(self, ResultStoreUploadStubMock,
                                              gen_new_uuid_mock):
        stub = ResultStoreUploadStubMock()
        stub.CreateConfiguredTarget = MagicMock(
            side_effect=create_return_configured_target)
        client = initialize_client(FLAGS)
        configured_target = get_default_configured_target(
            TEST_INVOCATION_ID, TEST_TARGET_ID, TEST_CONFIG_ID)
        res = client.create_configured_target(configured_target)
        self.assertEqual(res.id.target_id, TEST_TARGET_ID)
        self.assertEqual(res.id.configuration_id, TEST_CONFIG_ID)
        self.assertEqual(res.id.invocation_id, TEST_INVOCATION_ID)
        self.assertEqual(
            res.name, "invocations/{}/targets/{}/configuredTargets/{}".format(
                TEST_INVOCATION_ID, TEST_TARGET_ID, TEST_CONFIG_ID))

    @patch('resultstoreui_utils.gen_new_uuid', return_value=TEST_UUID)
    @patch(
        'resultstoreapi.cloud.devtools.resultstore_v2.proto.resultstore_upload_pb2_grpc.ResultStoreUploadStub'
    )
    def test_rpc_error(self, ResultStoreUploadStubMock, gen_new_uuid_mock):
        stub = ResultStoreUploadStubMock()
        stub.CreateConfiguredTarget = MagicMock(return_value=DEFAULT_RPC_ERROR)
        client = initialize_client(FLAGS)
        configured_target = get_default_configured_target(
            TEST_INVOCATION_ID, TEST_TARGET_ID, TEST_CONFIG_ID)
        res = client.create_configured_target(configured_target)
        self.assertEqual(res, DEFAULT_RPC_ERROR)


class CreateActionTest(absltest.TestCase):
    @patch('resultstoreui_utils.gen_new_uuid', return_value=TEST_UUID)
    @patch(
        'resultstoreapi.cloud.devtools.resultstore_v2.proto.resultstore_upload_pb2_grpc.ResultStoreUploadStub'
    )
    def test_create_action_success(self, ResultStoreUploadStubMock,
                                   gen_new_uuid_mock):
        stub = ResultStoreUploadStubMock()
        stub.CreateAction = MagicMock(side_effect=create_return_action)
        client = initialize_client(FLAGS)
        action = get_default_action(TEST_INVOCATION_ID, TEST_TARGET_ID,
                                    TEST_CONFIG_ID, TEST_ACTION_ID)
        res = client.create_action(action)
        self.assertEqual(res.id.action_id, TEST_ACTION_ID)
        self.assertEqual(
            res.name,
            "invocations/{}/targets/{}/configuredTargets/{}/actions/{}".format(
                TEST_INVOCATION_ID, TEST_TARGET_ID, TEST_CONFIG_ID,
                TEST_ACTION_ID))

    @patch('resultstoreui_utils.gen_new_uuid', return_value=TEST_UUID)
    @patch(
        'resultstoreapi.cloud.devtools.resultstore_v2.proto.resultstore_upload_pb2_grpc.ResultStoreUploadStub'
    )
    def test_rpc_error(self, ResultStoreUploadStubMock, gen_new_uuid_mock):
        stub = ResultStoreUploadStubMock()
        stub.CreateAction = MagicMock(return_value=DEFAULT_RPC_ERROR)
        client = initialize_client(FLAGS)
        action = get_default_action(TEST_INVOCATION_ID, TEST_TARGET_ID,
                                    TEST_CONFIG_ID, TEST_ACTION_ID)
        res = client.create_action(action)
        self.assertEqual(res, DEFAULT_RPC_ERROR)


class UpdateActionTest(absltest.TestCase):
    @patch('resultstoreui_utils.gen_new_uuid', return_value=TEST_UUID)
    @patch(
        'resultstoreapi.cloud.devtools.resultstore_v2.proto.resultstore_upload_pb2_grpc.ResultStoreUploadStub'
    )
    def test_update_action_success(self, ResultStoreUploadStubMock,
                                   gen_new_uuid_mock):
        stub = ResultStoreUploadStubMock()
        stub.UpdateAction = MagicMock(side_effect=create_return_action)
        client = initialize_client(FLAGS)
        action = get_default_action(TEST_INVOCATION_ID, TEST_TARGET_ID,
                                    TEST_CONFIG_ID, TEST_ACTION_ID)
        res = client.update_action(action,
                                   ['timing.duration', 'status_attributes'])
        self.assertEqual(res.id.action_id, TEST_ACTION_ID)
        self.assertEqual(
            res.name,
            "invocations/{}/targets/{}/configuredTargets/{}/actions/{}".format(
                TEST_INVOCATION_ID, TEST_TARGET_ID, TEST_CONFIG_ID,
                TEST_ACTION_ID))

    @patch('resultstoreui_utils.gen_new_uuid', return_value=TEST_UUID)
    @patch(
        'resultstoreapi.cloud.devtools.resultstore_v2.proto.resultstore_upload_pb2_grpc.ResultStoreUploadStub'
    )
    def test_rpc_error(self, ResultStoreUploadStubMock, gen_new_uuid_mock):
        stub = ResultStoreUploadStubMock()
        stub.UpdateAction = MagicMock(return_value=DEFAULT_RPC_ERROR)
        client = initialize_client(FLAGS)
        action = get_default_action(TEST_INVOCATION_ID, TEST_TARGET_ID,
                                    TEST_CONFIG_ID, TEST_ACTION_ID)
        res = client.update_action(action, ['test'])
        self.assertEqual(res, DEFAULT_RPC_ERROR)

    def test_missing_update_fields(self):
        client = initialize_client(FLAGS)
        try:
            client.update_action(None, None)
            self.fail('update_action passed with empty update fields')
        except Error as error:
            self.assertEqual(error.args[0], UPDATE_FIELD_ERROR_MESSAGE)


class UpdateConfiguredTargetTest(absltest.TestCase):
    def test_missing_update_fields(self):
        client = initialize_client(FLAGS)
        try:
            client.update_configured_target(None, None)
            self.fail(
                'update_configured_target passed with empty update fields')
        except Error as error:
            self.assertEqual(error.args[0], UPDATE_FIELD_ERROR_MESSAGE)

    @patch('resultstoreui_utils.gen_new_uuid', return_value=TEST_UUID)
    @patch(
        'resultstoreapi.cloud.devtools.resultstore_v2.proto.resultstore_upload_pb2_grpc.ResultStoreUploadStub'
    )
    def test_rpc_error(self, ResultStoreUploadStubMock, gen_new_uuid_mock):
        stub = ResultStoreUploadStubMock()
        stub.UpdateConfiguredTarget = MagicMock(return_value=DEFAULT_RPC_ERROR)
        client = initialize_client(FLAGS)
        configured_target = get_default_configured_target(
            TEST_INVOCATION_ID, TEST_TARGET_ID, TEST_CONFIG_ID)
        res = client.update_configured_target(configured_target, ['test'])
        self.assertEqual(res, DEFAULT_RPC_ERROR)

    @patch('resultstoreui_utils.gen_new_uuid', return_value=TEST_UUID)
    @patch(
        'resultstoreapi.cloud.devtools.resultstore_v2.proto.resultstore_upload_pb2_grpc.ResultStoreUploadStub'
    )
    def test_update_configured_target_success(self, ResultStoreUploadStubMock,
                                              gen_new_uuid_mock):
        stub = ResultStoreUploadStubMock()
        stub.UpdateConfiguredTarget = MagicMock(
            side_effect=create_return_configured_target)
        client = initialize_client(FLAGS)
        configured_target = get_default_configured_target(
            TEST_INVOCATION_ID, TEST_TARGET_ID, TEST_CONFIG_ID)
        res = client.update_configured_target(
            configured_target, ['timing.duration', 'status_attributes'])
        self.assertEqual(res.id.target_id, TEST_TARGET_ID)
        self.assertEqual(res.id.configuration_id, TEST_CONFIG_ID)
        self.assertEqual(
            res.name, "invocations/{}/targets/{}/configuredTargets/{}".format(
                TEST_INVOCATION_ID, TEST_TARGET_ID, TEST_CONFIG_ID))


class UpdateTargetTest(absltest.TestCase):
    def test_missing_update_fields(self):
        client = initialize_client(FLAGS)
        try:
            client.update_target(None, None)
            self.fail(
                'update_configured_target passed with empty update fields')
        except Error as error:
            self.assertEqual(error.args[0], UPDATE_FIELD_ERROR_MESSAGE)

    @patch('resultstoreui_utils.gen_new_uuid', return_value=TEST_UUID)
    @patch(
        'resultstoreapi.cloud.devtools.resultstore_v2.proto.resultstore_upload_pb2_grpc.ResultStoreUploadStub'
    )
    def test_rpc_error(self, ResultStoreUploadStubMock, gen_new_uuid_mock):
        stub = ResultStoreUploadStubMock()
        stub.UpdateTarget = MagicMock(return_value=DEFAULT_RPC_ERROR)
        client = initialize_client(FLAGS)
        target = get_default_target(TEST_INVOCATION_ID, TEST_TARGET_ID)
        res = client.update_target(target, ['test'])
        self.assertEqual(res, DEFAULT_RPC_ERROR)

    @patch('resultstoreui_utils.gen_new_uuid', return_value=TEST_UUID)
    @patch(
        'resultstoreapi.cloud.devtools.resultstore_v2.proto.resultstore_upload_pb2_grpc.ResultStoreUploadStub'
    )
    def test_update_target_success(self, ResultStoreUploadStubMock,
                                   gen_new_uuid_mock):
        stub = ResultStoreUploadStubMock()
        stub.UpdateTarget = MagicMock(side_effect=create_return_target)
        client = initialize_client(FLAGS)
        target = get_default_target(TEST_INVOCATION_ID, TEST_TARGET_ID)
        res = client.update_target(target,
                                   ['timing.duration', 'status_attributes'])
        self.assertEqual(res.id.target_id, TEST_TARGET_ID)
        self.assertEqual(
            res.name,
            "invocations/{}/targets/{}".format(TEST_INVOCATION_ID,
                                               TEST_TARGET_ID))


class FinalizeConfiguredTargetTest(absltest.TestCase):
    @patch('resultstoreui_utils.gen_new_uuid', return_value=TEST_UUID)
    @patch(
        'resultstoreapi.cloud.devtools.resultstore_v2.proto.resultstore_upload_pb2_grpc.ResultStoreUploadStub'
    )
    def test_rpc_error(self, ResultStoreUploadStubMock, gen_new_uuid_mock):
        stub = ResultStoreUploadStubMock()
        stub.FinalizeConfiguredTarget = MagicMock(
            return_value=DEFAULT_RPC_ERROR)
        client = initialize_client(FLAGS)
        res = client.finalize_configured_target(TEST_INVOCATION_ID,
                                                TEST_TARGET_ID, TEST_CONFIG_ID)
        self.assertEqual(res, DEFAULT_RPC_ERROR)

    @patch('resultstoreui_utils.gen_new_uuid', return_value=TEST_UUID)
    @patch(
        'resultstoreapi.cloud.devtools.resultstore_v2.proto.resultstore_upload_pb2_grpc.ResultStoreUploadStub'
    )
    def test_finalize_configured_target_success(self,
                                                ResultStoreUploadStubMock,
                                                gen_new_uuid_mock):
        stub = ResultStoreUploadStubMock()
        stub.FinalizeConfiguredTarget = MagicMock(
            side_effect=create_finalized_configured_target)
        client = initialize_client(FLAGS)
        res = client.finalize_configured_target(TEST_INVOCATION_ID,
                                                TEST_TARGET_ID, TEST_CONFIG_ID)
        self.assertEqual(res.id.target_id, TEST_TARGET_ID)
        self.assertEqual(res.id.configuration_id, TEST_CONFIG_ID)
        self.assertEqual(res.id.invocation_id, TEST_INVOCATION_ID)
        self.assertEqual(
            res.name, "invocations/{}/targets/{}/configuredTargets/{}".format(
                TEST_INVOCATION_ID, TEST_TARGET_ID, TEST_CONFIG_ID))


class FinalizeTargetTest(absltest.TestCase):
    @patch('resultstoreui_utils.gen_new_uuid', return_value=TEST_UUID)
    @patch(
        'resultstoreapi.cloud.devtools.resultstore_v2.proto.resultstore_upload_pb2_grpc.ResultStoreUploadStub'
    )
    def test_rpc_error(self, ResultStoreUploadStubMock, gen_new_uuid_mock):
        stub = ResultStoreUploadStubMock()
        stub.FinalizeTarget = MagicMock(return_value=DEFAULT_RPC_ERROR)
        client = initialize_client(FLAGS)
        res = client.finalize_target(TEST_INVOCATION_ID, TEST_TARGET_ID)
        self.assertEqual(res, DEFAULT_RPC_ERROR)

    @patch('resultstoreui_utils.gen_new_uuid', return_value=TEST_UUID)
    @patch(
        'resultstoreapi.cloud.devtools.resultstore_v2.proto.resultstore_upload_pb2_grpc.ResultStoreUploadStub'
    )
    def test_finalize_target_success(self, ResultStoreUploadStubMock,
                                     gen_new_uuid_mock):
        stub = ResultStoreUploadStubMock()
        stub.FinalizeTarget = MagicMock(side_effect=create_finalized_target)
        client = initialize_client(FLAGS)
        res = client.finalize_target(TEST_INVOCATION_ID, TEST_TARGET_ID)
        self.assertEqual(res.id.target_id, TEST_TARGET_ID)
        self.assertEqual(res.id.invocation_id, TEST_INVOCATION_ID)
        self.assertEqual(
            res.name,
            "invocations/{}/targets/{}".format(TEST_INVOCATION_ID,
                                               TEST_TARGET_ID))


class SingleUploadTest(absltest.TestCase):
    @flagsaver.flagsaver
    @patch('resultstoreui_utils.gen_new_uuid', return_value=TEST_UUID)
    @patch(
        'resultstoreapi.cloud.devtools.resultstore_v2.proto.resultstore_upload_pb2_grpc.ResultStoreUploadStub'
    )
    def test_finalize_target_success(self, ResultStoreUploadStubMock,
                                     gen_new_uuid_mock):
        FLAGS.invocation_id = TEST_INVOCATION_ID
        stub = ResultStoreUploadStubMock()
        with patch.object(BigStoreClient, 'upload_files_to_bigstore',
                          lambda self, files: []):
            stub.CreateConfiguration = MagicMock(
                side_effect=create_return_configuration)
            stub.CreateTarget = MagicMock(side_effect=create_return_target)
            stub.CreateConfiguredTarget = MagicMock(
                side_effect=create_return_configured_target)
            stub.CreateAction = MagicMock(side_effect=create_return_action)
            stub.UpdateAction = MagicMock(side_effect=create_return_action)
            stub.UpdateConfiguredTarget = MagicMock(
                side_effect=create_return_configured_target)
            stub.UpdateTarget = MagicMock(side_effect=create_return_target)
            stub.FinalizeConfiguredTarget = MagicMock(
                side_effect=create_finalized_configured_target)
            stub.FinalizeTarget = MagicMock(
                side_effect=create_finalized_target)
            client = initialize_client(FLAGS)
            client.single_upload()
            stub.CreateConfiguration.assert_called_once()
            stub.CreateTarget.assert_called_once()
            stub.CreateConfiguredTarget.assert_called_once()
            stub.CreateAction.assert_called_once()
            stub.UpdateAction.assert_called_once()
            stub.UpdateConfiguredTarget.assert_called_once()
            stub.UpdateTarget.assert_called_once()
            stub.FinalizeConfiguredTarget.assert_called_once()
            stub.FinalizeTarget.assert_called_once()


class BatchUploadTest(absltest.TestCase):
    @patch('resultstoreui_utils.gen_new_uuid', return_value=TEST_UUID)
    @patch(
        'resultstoreapi.cloud.devtools.resultstore_v2.proto.resultstore_upload_pb2_grpc.ResultStoreUploadStub'
    )
    def test_rpc_error(self, ResultStoreUploadStubMock, gen_new_uuid_mock):
        stub = ResultStoreUploadStubMock()
        stub.UploadBatch = MagicMock(return_value=DEFAULT_RPC_ERROR)
        client = initialize_client(FLAGS)
        upload_requests = client.create_resource_requests(
            TEST_INVOCATION_ID, TEST_CONFIG_ID)
        res = client.batch_upload(TEST_CURRENT_RESUME_TOKEN,
                                  TEST_NEXT_RESUME_TOKEN, TEST_INVOCATION_ID,
                                  upload_requests)
        self.assertEqual(res, DEFAULT_RPC_ERROR)

    @patch('resultstoreui_utils.gen_new_uuid', return_value=TEST_UUID)
    @patch(
        'resultstoreapi.cloud.devtools.resultstore_v2.proto.resultstore_upload_pb2_grpc.ResultStoreUploadStub'
    )
    def test_batch_upload_success(self, ResultStoreUploadStubMock,
                                  gen_new_uuid_mock):
        stub = ResultStoreUploadStubMock()
        stub.UploadBatch = MagicMock(return_value=None)
        client = initialize_client(FLAGS)
        upload_requests = client.create_resource_requests(
            TEST_INVOCATION_ID, TEST_CONFIG_ID)
        res = client.batch_upload(TEST_CURRENT_RESUME_TOKEN,
                                  TEST_NEXT_RESUME_TOKEN, TEST_INVOCATION_ID,
                                  upload_requests)
        self.assertEqual(res, None)
        stub.UploadBatch.assert_called_once()


if __name__ == '__main__':
    initialize_flags()
    absltest.main()
