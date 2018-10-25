from text_topic_generator.grpc_protos import topicgeneration_pb2_grpc as gen_grpc, topicgeneration_pb2 as gen
from . import topic_gen_model as model


class TopicGenerator(gen_grpc.TopicGenerationServicer):
    def __init__(self):
        self.model = model.TopicModelling()
        pass

    def GenerateTopicsDirect(self, loc, context):
        with open(loc, 'r') as document:
            topics = self.model.generate_topics(document)

        return gen.Topics(topics=topics)

    def GenerateTopicsIndirect(self, loc, context):
        return gen.FileLocation(location="~/")

