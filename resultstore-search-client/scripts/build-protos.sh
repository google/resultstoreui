#!/bin/bash

BASEDIR=$(dirname "$0")
cd ${BASEDIR}/../


PROTO_DEST=./src/api

# # JavaScript code generation
# yarn run grpc_tools_node_protoc \
#     --js_out=import_style=commonjs,binary:${PROTO_DEST} \
#     --grpc-web_out=import_style=commonjs,mode=grpcwebtext:${PROTO_DEST} \
#     --plugin=protoc-gen-grpc=./node_modules/.bin/grpc_tools_node_protoc_plugin \
#     -I ../resultstoresearch/v1 \
#     ../resultstoresearch/v1/*.proto

# # TypeScript code generation
# yarn run grpc_tools_node_protoc \
#     --plugin=protoc-gen-ts=./node_modules/.bin/protoc-gen-ts \
#     --ts_out=${PROTO_DEST} \
#     -I ../resultstoresearch/v1 \
#     ../resultstoresearch/v1/*.proto

protoc \
    --plugin=protoc-gen-ts=./node_modules/.bin/protoc-gen-ts \
    --ts_out=service=true:${PROTO_DEST}\
    --js_out=import_style=commonjs,binary:${PROTO_DEST}\
    -I ../resultstoresearch/v1 \
    ../resultstoresearch/v1/*.proto