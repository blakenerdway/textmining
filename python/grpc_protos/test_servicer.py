from grpc_protos.textmining import textminingservice_pb2_grpc as grpc_service
from grpc_protos.textmining import topicmining_pb2 as topicmining
from grpc_protos.textmining import textsummary_pb2 as textsummary
from text_summary import summary_gen


class TestServicer(grpc_service.TextMiningServicer):
    def GenerateTopics(self, loc, context):
        print("Generating topics directly")
        return topicmining.Topics(topics=["hello", "another one"])

    def GenerateTextSummary(self, request, context):
        text = ""
        with open(request.location) as text_file:
            for num, line in enumerate(text_file):
                text += line.strip()

        return textsummary.Summary(summary=summary_gen.summarize(text, "nltk"))
