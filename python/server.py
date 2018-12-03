from concurrent import futures
import time
import grpc

from grpc_protos.textmining import textminingservice_pb2_grpc as gen_grpc
from grpc_protos import test_servicer


class GrpcServer:
    def __init__(self, port="50051"):
        self.server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
        self.host = '[::]'
        self.port = port

        gen_grpc.add_TextMiningServicer_to_server(test_servicer.TestServicer(), self.server)

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
    test = GrpcServer()
    test.run()
