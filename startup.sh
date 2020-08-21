#!/bin/bash
eval $(egrep -v '^#' ./ci/.env | xargs) docker-compose -f ./ci/docker-compose.prod.yaml up --build
