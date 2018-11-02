from concurrent import futures
import time
import grpc

from text_topic_generator.grpc_protos.topic_gen import test_gen, topicgeneration_pb2_grpc as gen_grpc


class GrpcServer:
    def __init__(self, handler, port="50051"):
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        self.host = '[::]'
        self.port = port

        gen_grpc.add_TopicGenerationServicer_to_server(handler, self.server)
        self.server.add_insecure_port('[::]:' + port)

    def run(self):
        self.server.start()
        try:
            while True:
                time.sleep(60 * 60 * 24)
        except KeyboardInterrupt:
            self.server.stop(0)


if __name__ == '__main__':
    '''
    Test the server
    '''
    test = GrpcServer(test_gen.TestTopicGenerator())
    test.run()
