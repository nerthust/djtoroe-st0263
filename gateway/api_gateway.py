from fastapi import FastAPI
from threading import Lock
from rpc_client import mom_service
import json
import grpc

import file_service_pb2
import file_service_pb2_grpc

app = FastAPI()
mutex = Lock()
is_mom = True

@app.get("/")
def index():
    return "Services provided:   /list/ -> Lists all files   /search/{file} -> Searches for specified file"

@app.get("/list/{limit}")
def list(limit):
    return balance({"service": "list", "limit": limit})

@app.get("/search/{file}/{limit}")
def search(file, limit):
    return balance({"service": "search", "file": file, "limit": limit})

def grcp(req):
    req = json.loads(req)
    service = req['service']
    limit = int(req['limit'])

    config = json.load(open("config.json", 'r'))

    host = config['host']
    port = config['port']

    rute = f"{host}:{port}"
    channel = grpc.insecure_channel(rute)
    stub = file_service_pb2_grpc.FileServiceStub(channel)

    response = None

    if service == "list":
        response = stub.ListFiles(file_service_pb2.ListFilesReq(limit=limit))
    else:
        file = req['file']
        response = stub.SearchFiles(file_service_pb2.SearchFilesReq(search_query=file, limit=limit))

    return f"{response}"

def balance(req):
    global is_mom
    mutex.acquire()

    if is_mom == True:
        is_mom = False
        mutex.release()
        return mom_service(json.dumps(req))

    is_mom = True
    mutex.release()
    return grcp(json.dumps(req))
