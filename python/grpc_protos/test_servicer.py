from grpc_protos.textmining import textminingservice_pb2_grpc as grpc_service
from grpc_protos.textmining import topicmining_pb2 as topicmining
from grpc_protos.textmining import textsummary_pb2 as textsummary
from text_summary import summary_gen
import time


class TestServicer(grpc_service.TextMiningServicer):
    def GenerateTopics(self, request_iterator, context):
        distributions = [topicmining.TopicDistribution(word_probability=
                                                       [topicmining.WordProbability(word="hello", probability=.5),
                                                        topicmining.WordProbability(word="test", probability=.5)],
                                                       coverage=.8),
                         topicmining.TopicDistribution(word_probability=
                                                       [topicmining.WordProbability(word="another", probability=.3),
                                                        topicmining.WordProbability(word="one", probability=.7)],
                                                       coverage=.2),
                         topicmining.TopicDistribution(word_probability=
                                                       [topicmining.WordProbability(word="sports", probability=.5),
                                                        topicmining.WordProbability(word="game", probability=.5)],
                                                       coverage=.2)
                         ]
        yield topicmining.Topics(topics=[distributions[0], distributions[1]])
        yield topicmining.Topics(topics=[distributions[2]])


    def GenerateTextSummary(self, request_iterator, context):
        for location in request_iterator:
            text = ""
            with open(location.location) as text_file:
                for num, line in enumerate(text_file):
                    text += line.strip()
            yield textsummary.Summary(summary=summary_gen.summarize(text, "nltk"))
