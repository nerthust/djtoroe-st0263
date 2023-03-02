import grpc
import os
from concurrent import futures
import file_service_pb2
import file_service_pb2_grpc

class FileService(file_service_pb2_grpc.FileServiceServicer):
    def ListFiles(self, request, context):
        files = os.listdir('.')
        response = file_service_pb2.FileList()
        response.filenames.extend(files)
        return response

    def ReadFile(self, request, context):
        filename = request.filename
        try:
            with open(filename, 'rb') as f:
                contents = f.read()
                response = file_service_pb2.FileResponse(file_contents=contents)
                return response
        except FileNotFoundError:
            context.abort(grpc.StatusCode.NOT_FOUND, "File not found")

server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
file_service_pb2_grpc.add_FileServiceServicer_to_server(FileService(), server)
server.add_insecure_port('[::]:50051')
server.start()
print("Server listening on port 50051")
server.wait_for_termination()
