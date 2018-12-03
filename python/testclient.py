from __future__ import print_function
import grpc
import grpc_protos.textmining.textminingservice_pb2_grpc as serv_grpc
import grpc_protos.textmining.filelocation_pb2 as file_location


if __name__ == '__main__':
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = serv_grpc.TextMiningStub(channel)
        response = stub.GenerateTopics(file_location.FileLocation(location="hi!"))
        print('Topics:-----------------:')
        print(response.topics)
        print()
        response = stub.GenerateTextSummary(file_location.FileLocation(location="hi!"))
        print('Summary-----------------:')
        print(response.summary)


