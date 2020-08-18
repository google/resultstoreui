# Resultstore Search

Service to search through invocation in resultstore.

## Prerequisites

1. Docker and docker-compose installed [here](https://www.docker.com/)
2. Generate [service account](https://cloud.google.com/iam/docs/creating-managing-service-account-keys)
3. Enable the following permissions on the service account

```
Cloud Source Tools Core - Developer
Cloud Datastore User
Storage Object Viewer
Viewer
```

4. Generate a [client id](https://developers.google.com/identity/sign-in/web/sign-in#create_authorization_credentials)
5. Configure .env file in ./ci following example.env
6. Add eligible users to the cloudsourcetoolscore.developer role in your GCP project

## Usage

Locally:

```shell
docker-compose -f ./ci/docker-compose.prod.yaml up --build
```

Navigate to [localhost](http://localhost/)
