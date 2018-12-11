import server as topic_server
import _thread

if __name__ == '__main__':
    server = topic_server.GrpcServer(port="50051")
    _thread.start_new_thread(function=server.run(), args=[])
