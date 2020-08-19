config = {
  "interfaces": {
    "google.devtools.resultstore.v2.ResultStoreDownload": {
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
        "GetInvocation": {
          "timeout_millis": 60000,
          "retry_codes_name": "idempotent",
          "retry_params_name": "default"
        },
        "SearchInvocations": {
          "timeout_millis": 60000,
          "retry_codes_name": "idempotent",
          "retry_params_name": "default"
        },
        "GetInvocationDownloadMetadata": {
          "timeout_millis": 60000,
          "retry_codes_name": "idempotent",
          "retry_params_name": "default"
        },
        "GetConfiguration": {
          "timeout_millis": 60000,
          "retry_codes_name": "idempotent",
          "retry_params_name": "default"
        },
        "ListConfigurations": {
          "timeout_millis": 60000,
          "retry_codes_name": "idempotent",
          "retry_params_name": "default"
        },
        "GetTarget": {
          "timeout_millis": 60000,
          "retry_codes_name": "idempotent",
          "retry_params_name": "default"
        },
        "ListTargets": {
          "timeout_millis": 60000,
          "retry_codes_name": "idempotent",
          "retry_params_name": "default"
        },
        "GetConfiguredTarget": {
          "timeout_millis": 60000,
          "retry_codes_name": "idempotent",
          "retry_params_name": "default"
        },
        "ListConfiguredTargets": {
          "timeout_millis": 60000,
          "retry_codes_name": "idempotent",
          "retry_params_name": "default"
        },
        "GetAction": {
          "timeout_millis": 60000,
          "retry_codes_name": "idempotent",
          "retry_params_name": "default"
        },
        "ListActions": {
          "timeout_millis": 60000,
          "retry_codes_name": "idempotent",
          "retry_params_name": "default"
        },
        "GetFileSet": {
          "timeout_millis": 60000,
          "retry_codes_name": "idempotent",
          "retry_params_name": "default"
        },
        "ListFileSets": {
          "timeout_millis": 60000,
          "retry_codes_name": "idempotent",
          "retry_params_name": "default"
        },
        "TraverseFileSets": {
          "timeout_millis": 60000,
          "retry_codes_name": "idempotent",
          "retry_params_name": "default"
        }
      }
    }
  }
}
