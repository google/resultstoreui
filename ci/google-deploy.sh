#!/bin/bash

# Authenticate with the Google Services
# codeship_google authenticate

# switch to the directory containing your app.yml (or similar) configuration file
# note that your repository is mounted as a volume to the /deploy directory
cd ../

# copy the application files
gcloud compute scp [!.]* ${CLOUD_USER}@${INSTANCE_NAME}:./ --quiet --zone ${INSTANCE_ZONE}

# deploy the application
gcloud compute ssh ${CLOUD_USER}@${INSTANCE_NAME} --zone ${INSTANCE_ZONE} --command "sudo docker-compose -f ./ci/docker-compose.prod.yaml up --build"
