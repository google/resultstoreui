#!/bin/bash

# Authenticate with the Google Services
# codeship_google authenticate

# switch to the directory containing your app.yml (or similar) configuration file
# note that your repository is mounted as a volume to the /deploy directory
cd ../

echo "${CLOUD_USER}@${INSTANCE_NAME}"

# copy the application files
gcloud compute copy-files [!.]* compute copy-files:./ --quiet --zone ${INSTANCE_ZONE}

# deploy the application
gcloud compute ssh ${CLOUD_USER}@${INSTANCE_NAME} --zone ${INSTANCE_ZONE} --command "sudo docker-compose -f ./ci/docker-compose.prod.yaml up --build"
