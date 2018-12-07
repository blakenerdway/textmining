import server as topic_server


if __name__ == '__main__':
    server = topic_server.GrpcServer(port="50051")
    server.run()
