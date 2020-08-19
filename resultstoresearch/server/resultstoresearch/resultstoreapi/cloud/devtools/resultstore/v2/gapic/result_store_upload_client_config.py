config = {
  "interfaces": {
    "google.devtools.resultstore.v2.ResultStoreUpload": {
      "retry_codes": {
        "idempotent": [
          "DEADLINE_EXCEEDED",
          "UNAVAILABLE"
        ],
        "non_idempotent": []
      },
      "retry_params": {
        "default": {
          "initial_retry_delay_millis": 100,
          "retry_delay_multiplier": 1.3,
          "max_retry_delay_millis": 60000,
          "initial_rpc_timeout_millis": 20000,
          "rpc_timeout_multiplier": 1.0,
          "max_rpc_timeout_millis": 20000,
          "total_timeout_millis": 600000
        }
      },
      "methods": {
        "CreateInvocation": {
          "timeout_millis": 60000,
          "retry_codes_name": "non_idempotent",
          "retry_params_name": "default"
        },
        "UpdateInvocation": {
          "timeout_millis": 60000,
          "retry_codes_name": "non_idempotent",
          "retry_params_name": "default"
        },
        "MergeInvocation": {
          "timeout_millis": 60000,
          "retry_codes_name": "non_idempotent",
          "retry_params_name": "default"
        },
        "TouchInvocation": {
          "timeout_millis": 60000,
          "retry_codes_name": "non_idempotent",
          "retry_params_name": "default"
        },
        "FinalizeInvocation": {
          "timeout_millis": 60000,
          "retry_codes_name": "non_idempotent",
          "retry_params_name": "default"
        },
        "DeleteInvocation": {
          "timeout_millis": 60000,
          "retry_codes_name": "non_idempotent",
          "retry_params_name": "default"
        },
        "CreateTarget": {
          "timeout_millis": 60000,
          "retry_codes_name": "non_idempotent",
          "retry_params_name": "default"
        },
        "UpdateTarget": {
          "timeout_millis": 60000,
          "retry_codes_name": "non_idempotent",
          "retry_params_name": "default"
        },
        "MergeTarget": {
          "timeout_millis": 60000,
          "retry_codes_name": "non_idempotent",
          "retry_params_name": "default"
        },
        "FinalizeTarget": {
          "timeout_millis": 60000,
          "retry_codes_name": "non_idempotent",
          "retry_params_name": "default"
        },
        "CreateConfiguredTarget": {
          "timeout_millis": 60000,
          "retry_codes_name": "non_idempotent",
          "retry_params_name": "default"
        },
        "UpdateConfiguredTarget": {
          "timeout_millis": 60000,
          "retry_codes_name": "non_idempotent",
          "retry_params_name": "default"
        },
        "MergeConfiguredTarget": {
          "timeout_millis": 60000,
          "retry_codes_name": "non_idempotent",
          "retry_params_name": "default"
        },
        "FinalizeConfiguredTarget": {
          "timeout_millis": 60000,
          "retry_codes_name": "non_idempotent",
          "retry_params_name": "default"
        },
        "CreateAction": {
          "timeout_millis": 60000,
          "retry_codes_name": "non_idempotent",
          "retry_params_name": "default"
        },
        "UpdateAction": {
          "timeout_millis": 60000,
          "retry_codes_name": "non_idempotent",
          "retry_params_name": "default"
        },
        "MergeAction": {
          "timeout_millis": 60000,
          "retry_codes_name": "non_idempotent",
          "retry_params_name": "default"
        },
        "CreateConfiguration": {
          "timeout_millis": 60000,
          "retry_codes_name": "non_idempotent",
          "retry_params_name": "default"
        },
        "UpdateConfiguration": {
          "timeout_millis": 60000,
          "retry_codes_name": "non_idempotent",
          "retry_params_name": "default"
        },
        "CreateFileSet": {
          "timeout_millis": 60000,
          "retry_codes_name": "non_idempotent",
          "retry_params_name": "default"
        },
        "UpdateFileSet": {
          "timeout_millis": 60000,
          "retry_codes_name": "non_idempotent",
          "retry_params_name": "default"
        },
        "MergeFileSet": {
          "timeout_millis": 60000,
          "retry_codes_name": "non_idempotent",
          "retry_params_name": "default"
        },
        "UploadBatch": {
          "timeout_millis": 60000,
          "retry_codes_name": "non_idempotent",
          "retry_params_name": "default"
        },
        "GetInvocationUploadMetadata": {
          "timeout_millis": 60000,
          "retry_codes_name": "idempotent",
          "retry_params_name": "default"
        }
      }
    }
  }
}
