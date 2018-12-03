from grpc.textmining import textminingservice_pb2_grpc as grpc_service


class Servicer(grpc_service.TextMiningServicer):
    def GenerateTopics(self, loc, context):
        print("Generating topics directly")

    def GenerateTextSummary(self, request, context):
        print("Generating summary")
