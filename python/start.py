import server as topic_server
import configparser


if __name__ == '__main__':
    config = configparser.ConfigParser()
    defaults = config.read('config.ini')['DEFAULT']
    port = int(defaults['port'])

    server = topic_server.GrpcServer(port=port)
    server.run()
