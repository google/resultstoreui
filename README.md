# Resultstore Search

Service to search and render invocations and tests in resultstore.

## Client Documentation

Client component documentation can be viewed [here](https://google.github.io/resultstoreui/)

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
5. Configure .env file in ./resultstoresearch/ci following example.env
6. Add eligible users to the cloudsourcetoolscore.developer role in your GCP project

## Usage

Locally:

```shell
./startup
```

Navigate to [localhost](http://localhost/)

## Overview

### Main Page

Page where users can search, filter, and view invocation information

![main-page](https://user-images.githubusercontent.com/22064715/90555764-e0f01b80-e165-11ea-94df-4f6a1f2ec1f9.png)

### Top Bar

![top-bar](https://user-images.githubusercontent.com/22064715/90555769-e188b200-e165-11ea-86bf-535cc8ac4d1b.png)

#### Tool Type Selection

Dropdown thats allows a user to select a tool type to filter search results by.

![tool-type](https://user-images.githubusercontent.com/22064715/90555771-e2214880-e165-11ea-82f6-2a931b1a5948.png)

#### Search Bar

Enter queries to search for invocations. The search bar features an autocomplete typeahead for fields that can be filtered on.

![search-bar](https://user-images.githubusercontent.com/22064715/90549837-15130e80-e15d-11ea-83ae-752e68ed505b.png)

#### Search Button

Initiates a search for invocations based on the query in the search bar

![search-button](https://user-images.githubusercontent.com/22064715/90549687-da10db00-e15c-11ea-9a4c-f93b7b2fd071.png)

#### Flaky Test Button

Initiates the flaky test interface for the current query in the search bar.

![flaky-test](https://user-images.githubusercontent.com/22064715/90549943-3b38ae80-e15d-11ea-9aec-ea3b944fc180.png)

#### Google Login / Logout Button

Google login / logout button for authentication

![google-button](https://user-images.githubusercontent.com/22064715/90550082-720ec480-e15d-11ea-878d-8c5948708fa8.png)

### Invocation Table

Table that lists the result of an invocation search

#### File Modal

Users can view files associated with the current invocation

![file-modal](https://user-images.githubusercontent.com/22064715/90555776-e3527580-e165-11ea-8142-81f83ca25868.png)

## Flaky Test Page

Users can view the results of tests over time with different invocations.

- Grey: No test was run
- Green: Test Success
- Red: Test Failed

![flaky-test](https://user-images.githubusercontent.com/22064715/90555782-e3eb0c00-e165-11ea-932d-010ee4b74dd6.png)
