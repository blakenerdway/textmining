from grpc_protos.textmining import textminingservice_pb2_grpc as grpc_service
from grpc_protos.textmining import topicmining_pb2 as topicmining
from grpc_protos.textmining import textsummary_pb2 as textsummary
from text_summary import summary_gen
import time


class TestServicer(grpc_service.TextMiningServicer):
    def GenerateTopics(self, request_iterator, context):
        topics = [topicmining.TopicDistribution(words=["hello", "test"], coverage=".8"),
                  topicmining.TopicDistribution(words=["another", "topic2!"], coverage=".2")]
        for i in range(1):
            yield topicmining.Topics(topics=topics[i])

    def GenerateTextSummary(self, request_iterator, context):
        for location in request_iterator:
            text = ""
            with open(location.location) as text_file:
                for num, line in enumerate(text_file):
                    text += line.strip()
            yield textsummary.Summary(summary=summary_gen.summarize(text, "nltk"))
