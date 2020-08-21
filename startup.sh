#!/bin/bash
eval $(egrep -v '^#' ./resultstoresearch/ci/.env | xargs) docker-compose -f ./resultstoresearch/ci/docker-compose.prod.yaml up --build
