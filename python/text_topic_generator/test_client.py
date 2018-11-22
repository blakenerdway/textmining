from __future__ import print_function
import grpc
from grpc_protos.topic_gen import topicgeneration_pb2_grpc as gen_grpc, topicgeneration_pb2 as gen


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = gen_grpc.TopicGenerationStub(channel)
        response = stub.GenerateTopicsDirect(gen.FileLocation(location='~/Desktop'))
        for topic in response.topics:
            print('Client received: ' + topic)

        response = stub.GenerateTopicsIndirect(gen.FileLocation(location='~/Desktop'))
        print('Client received indirect file loc: ' + response.location)


if __name__ == '__main__':
    run()
