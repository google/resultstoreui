from base64 import b64encode
from absl import (flags, app)
from resultstore_client import ResultStoreClient
from credentials import Credentials
from resultstoreapi.cloud.devtools.resultstore_v2.proto import common_pb2

FLAGS = flags.FLAGS


def initialize_flags():
    flags.DEFINE_string(
        'command', '',
        'Available commands to execute: get-invocation, create-invocation, single-upload'
    )
    flags.DEFINE_string('config_id', 'default', 'Config Id')
    flags.DEFINE_string('target_name', '', 'Target Name')
    flags.DEFINE_string('invocation_id', '', 'Invocation ID')
    flags.DEFINE_string('authorization_token', '', 'Authorization Token')
    flags.DEFINE_string('action_type', 'TEST', 'Action Type')
    flags.DEFINE_string('invocation_name', '', 'Invocation Name')
    flags.DEFINE_string('bigstore_project_name',
                        'google.com:gchips-productivity',
                        'The project name for the bigstore client')
    flags.DEFINE_enum('status', 'PASSED', common_pb2.Status.keys(),
                      'Status of this action (if command not provided)')
    flags.DEFINE_string('bucket_name', 'sival-logs',
                        'Google Cloud Storage Bucket Name')
    flags.DEFINE_list('files', [], 'files to be uploaded with the action')
    flags.DEFINE_string(
        'channel_target', 'resultstore.googleapis.com',
        'The host and port of the service that the channel is created to')
    flags.DEFINE_bool(
        'create_config', True,
        'Boolean to control creation of configuration during single or batch upload'
    )
    flags.DEFINE_string('resume_token', '',
                        'Current resume token for batch uplaods')
    flags.DEFINE_string('next_resume_token', '',
                        'Next resume token for batch uploads')


def main(argv):
    resultstore_creds = Credentials()
    resultstore_client = ResultStoreClient(resultstore_creds, FLAGS)
    resume_token = b64encode(bytes(FLAGS.resume_token, 'utf-8'))
    next_resume_token = b64encode(bytes(FLAGS.next_resume_token, 'utf-8'))
    with resultstore_creds.create_secure_channel(
            FLAGS.channel_target) as channel:
        if not FLAGS.command:
            raise Exception(
                'No command specified! Please specific a command with --command'
            )
        elif FLAGS.command == 'get-invocation':
            resultstore_client.get_invocation(FLAGS.invocation_name)
        elif FLAGS.command == 'create-invocation':
            resultstore_client.create_invocation()
        elif FLAGS.command == 'single-upload':
            resultstore_client.single_upload()
        elif FLAGS.command == 'batch-upload':
            resultstore_client.batch_upload_wrapper(resume_token,
                                                    next_resume_token)
        elif FLAGS.command == 'finalize-batch-upload':
            resultstore_client.finalize_batch_upload(resume_token,
                                                     next_resume_token,
                                                     FLAGS.invocation_id)
        else:
            raise Exception('Command not found: {}'.format(FLAGS.command))


if __name__ == '__main__':
    initialize_flags()
    app.run(main)
