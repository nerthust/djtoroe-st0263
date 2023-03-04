import grpc
import file_service_pb2
import file_service_pb2_grpc

with grpc.insecure_channel('localhost:50051') as channel:
    stub = file_service_pb2_grpc.FileServiceStub(channel)
    response = stub.ListFiles(file_service_pb2.ListFilesReq())
    print("ListFiles response: ", response)

    response = stub.SearchFiles(file_service_pb2.SearchFilesReq(search_query='file_service.proto'))
    print("SearchFiles response: ", response)
