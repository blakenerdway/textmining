from concurrent import futures
import time
import grpc
import topicgeneration_pb2 as gen
import topicgeneration_pb2_grpc as gen_grpc


class TopicGenerator(gen_grpc.TopicGenerationServicer):
    def GenerateTopicsDirect(self, loc, context):
        return gen.Topics(topics=["hello", "another one"])

    def GenerateTopicsIndirect(self, loc, context):
        return gen.FileLocation(location="~/")

def run():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    gen_grpc.add_TopicGenerationServicer_to_server(TopicGenerator(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(60 * 60 * 24)
    except KeyboardInterrupt:
        server.stop(0)




if __name__ == '__main__':
    run()
