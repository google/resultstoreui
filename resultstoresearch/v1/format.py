import glob
import re

CLIENT_OUTPUT_DIR = '../../resultstore-search-client/src/api/*.js'
SERVER_OUTPUT_DIR = '../../resultstore-search-api/resultstoresearchapi/*.py'

client_search_phrase = 'GENERATED CODE -- DO NOT EDIT!'
client_replace_phrase = 'GENERATED CODE -- DO NOT EDIT!\n/* tslint:disable */\n/* eslint-disable */'

server_search_phrase = '^import .*_pb2 as .*_pb2'
server_replace_phrase = 'import resultstoresearchapi.'

for filepath in glob.iglob(CLIENT_OUTPUT_DIR, recursive=False):
    with open(filepath) as file:
        s = file.read()
    s = s.replace(client_search_phrase, client_replace_phrase)
    with open(filepath, "w") as file:
        file.write(s)

for filepath in glob.iglob(SERVER_OUTPUT_DIR, recursive=False):
    with open(filepath) as file:
        resp = ''
        for line in file:
            exists = re.search('^import .*_pb2 as .*_pb2', line)
            if exists:
                line = 'import resultstoresearchapi.' + line[7:]
            resp += line
    with open(filepath, "w") as file:
        file.write(resp)
