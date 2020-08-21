#!/bin/bash
INPUT_DIR=./
SERVER_OUTPUT_DIR=../../resultstore-search-api/resultstoresearchapi
CLIENT_OUTPUT_DIR=../../resultstore-search-client/src/api/

protoc -I=$INPUT_DIR *.proto \
  --js_out=import_style=commonjs,binary:$CLIENT_OUTPUT_DIR \
  --grpc-web_out=import_style=typescript,mode=grpcwebtext:$CLIENT_OUTPUT_DIR

python -m grpc_tools.protoc -I=$INPUT_DIR *.proto \
  --python_out=$SERVER_OUTPUT_DIR \
  --grpc_python_out=$SERVER_OUTPUT_DIR

python format.py
