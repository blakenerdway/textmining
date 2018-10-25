import com.google.protobuf.ByteString;
import com.google.protobuf.ProtocolStringList;
import grpc.document.Generation;
import grpc.document.TopicGenerationGrpc;
import io.grpc.ManagedChannel;
import io.grpc.ManagedChannelBuilder;
import io.grpc.StatusRuntimeException;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.TimeUnit;
import java.util.function.Consumer;

/**
 * The topic generation client is used to send GRPC requests to a server on a specific port
 */
public class TopicGenerationClient
{
    public TopicGenerationClient(String host, int port){
        this(ManagedChannelBuilder.forAddress(host, port).usePlaintext().build());
    }

    TopicGenerationClient(ManagedChannel channel){
        _channel = channel;
        _blockingStub = TopicGenerationGrpc.newBlockingStub(_channel);
    }

    public TopicGenerationClient(){
        this("localhost", 50051);
    }

    /**
     * Sends a request to the server to generate topics and store them in a file. The file's location is returned
     */
    public void generateTopicsIndirectFromLoc (String location, Consumer<String> onReturned){
        _logger.info("Attempting to call server to generate topics");
        Generation.FileLocation fileLocationSend = Generation.FileLocation.newBuilder().setLocation(location).build();

        Generation.FileLocation fileLocationRcv;
        try {
            fileLocationRcv = _blockingStub.generateTopicsIndirect(fileLocationSend);
        } catch (StatusRuntimeException e){
            _logger.warn("RPC request failed with status {}", e.getStatus());
            return;
        }

        onReturned.accept(fileLocationRcv.getLocation());
    }

    public void generateTopicsFromLoc (String location, Consumer<List<String>> onReturned){
        _logger.info("Attempting to call server to generate topics");
        Generation.FileLocation fileLocationSend = Generation.FileLocation.newBuilder().setLocation(location).build();

        Generation.Topics returnedTopics;
        try {
            returnedTopics = _blockingStub.generateTopicsDirect(fileLocationSend);
        } catch (StatusRuntimeException e){
            _logger.warn("RPC request failed with status {}", e.getStatus());
            return;
        }

        onReturned.accept(returnedTopics.getTopicsList());
    }

    public void shutdown() throws InterruptedException {
        _channel.shutdown().awaitTermination(5, TimeUnit.SECONDS);
    }

    public static void main (String[] args) throws Exception {
        TopicGenerationClient client = new TopicGenerationClient();

        try {
           client.generateTopicsFromLoc("who cares", strings -> strings.forEach(string -> _logger.info("Topic returned: \"{}\"", string)));

            client.generateTopicsIndirectFromLoc("who cares2", location -> _logger.info("File location returned was: {}", location));
        }
        finally {
            client.shutdown();
        }
    }


    private final ManagedChannel _channel;
    private final TopicGenerationGrpc.TopicGenerationBlockingStub _blockingStub;

    private static final Logger _logger = LoggerFactory.getLogger(TopicGenerationClient.class);
}
