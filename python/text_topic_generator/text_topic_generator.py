from text_topic_generator.grpc_protos import topicgeneration_pb2_grpc as gen_grpc, topicgeneration_pb2 as gen
from . import topic_gen_model as model


class TopicGenerator(gen_grpc.TopicGenerationServicer):
    def __init__(self):
        self.model = model.TopicModelling()

    def GenerateTopicsDirect(self, loc, context):
        topics = self.generate(loc)
        return gen.Topics(topics=topics)

    def GenerateTopicsIndirect(self, loc, context):
        topics = self.generate(loc)

        # Open a file and write the topics there
        topic_loc = loc + '-topics'
        with open(topic_loc, 'w') as document:
            document.write(topics)

        return gen.FileLocation(location=topic_loc)

    def generate(self, loc):
        with open(loc, 'r') as document:
            topics = self.model.generate_topics(document)

        return topics
