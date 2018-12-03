import server as topic_server
import configparser
from text_topic_generator import topic_gen_model as model
from text_topic_generator import text_topic_generator

if __name__ == '__main__':
    config = configparser.ConfigParser()
    defaults = config.read('config.ini')['DEFAULT']
    port = int(defaults['port'])

    topic_model = model.TopicModelling()
    handler = text_topic_generator.GrpcTopicHandler(topic_model)

    server = topic_server.GrpcServer(handler=handler, port=port)
    server.run()
