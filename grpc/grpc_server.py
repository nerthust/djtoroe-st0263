from concurrent import futures
import os
import glob
import pathlib
import grpc
import sys
import json

import file_service_pb2
import file_service_pb2_grpc

class FileService(file_service_pb2_grpc.FileServiceServicer):
    dir_papth = None

    def __init__(self, dir_path):
        self.dir_path = dir_path

    def ListFiles(self, request, Listt):
        limit = request.limit
        file_names = self.list_files(limit=limit)
        response = file_service_pb2.ListFilesResp(file_names=file_names)
        return response

    def SearchFiles(self, request, context):
        query = request.search_query
        limit = request.limit
        file_names = self.list_files(pattern=query, limit=limit)
        response = file_service_pb2.ListFilesResp(file_names=file_names)

        return response

    def list_files(self, pattern="*", limit=None):
        files = list(
            map(lambda p: str(p), pathlib.Path(self.dir_path).glob("**/" + pattern))
        )

        if limit == None or limit < 1:
            return files
        else:
            return files[:limit]

def serve(port, dir_path, workers):
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=workers))
    file_service_pb2_grpc.add_FileServiceServicer_to_server(FileService(dir_path), server)
    server.add_insecure_port(f"[::]:{port}")
    server.start()
    print(f"Server started. Listening on port {port}.")
    server.wait_for_termination()

def main(argv):
    if len(argv) == 2:
        config_path = argv[1]
        config = json.load(open(config_path, 'r'))
        serve(config['port'], config['dir_path'], config['max_workers'])

if __name__ == '__main__':
    main(sys.argv)
