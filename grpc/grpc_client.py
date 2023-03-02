import grpc
import file_service_pb2
import file_service_pb2_grpc

channel = grpc.insecure_channel('localhost:50051')
stub = file_service_pb2_grpc.FileServiceStub(channel)

response = stub.ListFiles(file_service_pb2.Empty())
print(response.filenames)
