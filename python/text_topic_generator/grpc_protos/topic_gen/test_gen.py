from grpc_protos.topic_gen import topicgeneration_pb2_grpc as gen_grpc, topicgeneration_pb2 as gen


class TestTopicGenerator(gen_grpc.TopicGenerationServicer):
    def GenerateTopicsDirect(self, loc, context):
        print("Generating topics directly")
        return gen.Topics(topics=["hello", "another one"])

    def GenerateTopicsIndirect(self, loc, context):
        print("Generating topics indirectly")
        return gen.FileLocation(location="~/")
