# ResultStoreUI
## Usage

This tool can be run using either

```shell
bazel run resultstoreui
```

or

```shell
python3 resultstoreui.py
```

and specifying the following flags

* `--command`: The main command to be run for the current invocation of the cli
    eg.
  * `get-invocation` : Attempts to get the invocation specified with the `--invocation_name` flag.

  ```shell
  bazel run resultstoreui -- --command="get-invocation" --invocation_name="invocations/d9910974-4d59-4fee-8188-a891de97814a"
  ```

  * `create-invocation`: Attempts to create a new invocation using the optionally provided `--authorization_token` or generating one to be associated with requests made with this invocation in the future. Specifying a `--resume_token` will put the invocation into batch mode.

  ```shell
  bazel run resultstoreui -- --command="create-invocation" --authorization_token="77f3d6ca-0577-429f-ba59-02090d27a15b"
  ```

  * `single-upload`: Uploads a single target, config, configured target and files to the specified `--invocation-id`

  ```shell
  bazel run resultstoreui -- --command="single_upload"
  --invocation_id="d9910974-4d59-4fee-8188-a891de97814a"
  --authorization_token="77f3d6ca-0577-429f-ba59-02090d27a15b"
  --files="/path/to/file1, /path/to/file2"
  ```

  * `batch-upload`: Batch uploads targets, configs, configured targets and files to an invocation in batch mode.
  
  ```shell
  bazel run resultstoreui -- --command="batch-upload"
  --invocation_id="d9910974-4d59-4fee-8188-a891de97814a"
  --authorization_token="77f3d6ca-0577-429f-ba59-02090d27a15b"
  --resume_token="current-resume-token"
  --next_resume_token="next-resume-token"
  --files="/path/to/file1, /path/to/file2"
  ```

  * `finalize-batch-upload` : Finalizes an invocation in batch mode

  ```shell
  bazel run resultstoreui -- --command="finalize-batch-upload"
  --invocation_id="d9910974-4d59-4fee-8188-a891de97814a"
  --resume_token="current-resume-token"
  --next_resume_token="next-resume-token"
  --authorization_token="77f3d6ca-0577-429f-ba59-02090d27a15b"
  ```

* `--channel_target`: The host and port of the service that the channel is created to
* `--config_id` : config_id to be used when creating a config
* `--target_name`: target_name to be used when creating a target
* `--invocation_id`: invocation to edit
* `--authorization_token`: authorization token to be used during the current command
* `--action_type`: action_type for the current action to be created
* `--invocation_name`: action to get when using the `get-invocation` command
* `--bigstore_project_name`: bigstore project to upload files to
* `--bucket_name`: Bucket name inside bigstore to upload files to
* `--files`: comma separated list of paths to files to upload for the current target
* `--status`: Current status of the action being uploaded
* `--create_config`: Boolean to specify creatione of a configuration during single-upload or batch-upload
* `--resume_token`: Current resume token for batch uploads
* `--next_resume_token`: Next resume token for batch uploads

## Running Tests

Tests can be run with either

```shell
bazel run test_resultstoreui
```

or

```shell
python3 resultstore_client_test.py
```

## Rebuilding gRPC Client Files

1. Clone https://github.com/googleapis/googleapis

2. Copy the build file from gRPC-build to the `google/devtools/resultstore/v2/` subdirectory

3. `bazel build //...`

4. Navigate to your local bazel cache under `${HOME}/.cache/bazel/_bazel_${USER}/BUILD_ID/execroot/com_google_googleapis`

5. Copy the google subdirectory and replace the current resultstoreapi folder with the newly generated files
