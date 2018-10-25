package grpc.document;

import static io.grpc.MethodDescriptor.generateFullMethodName;
import static io.grpc.stub.ClientCalls.asyncBidiStreamingCall;
import static io.grpc.stub.ClientCalls.asyncClientStreamingCall;
import static io.grpc.stub.ClientCalls.asyncServerStreamingCall;
import static io.grpc.stub.ClientCalls.asyncUnaryCall;
import static io.grpc.stub.ClientCalls.blockingServerStreamingCall;
import static io.grpc.stub.ClientCalls.blockingUnaryCall;
import static io.grpc.stub.ClientCalls.futureUnaryCall;
import static io.grpc.stub.ServerCalls.asyncBidiStreamingCall;
import static io.grpc.stub.ServerCalls.asyncClientStreamingCall;
import static io.grpc.stub.ServerCalls.asyncServerStreamingCall;
import static io.grpc.stub.ServerCalls.asyncUnaryCall;
import static io.grpc.stub.ServerCalls.asyncUnimplementedStreamingCall;
import static io.grpc.stub.ServerCalls.asyncUnimplementedUnaryCall;

/**
 * <pre>
 * The Generation service definition.
 * </pre>
 */
@javax.annotation.Generated(
    value = "by gRPC proto compiler (version 1.15.1)",
    comments = "Source: topicgeneration.proto")
public final class TopicGenerationGrpc {

  private TopicGenerationGrpc() {}

  public static final String SERVICE_NAME = "grpc.document.TopicGeneration";

  // Static method descriptors that strictly reflect the proto.
  private static volatile io.grpc.MethodDescriptor<grpc.document.Generation.FileLocation,
      grpc.document.Generation.Topics> getGenerateTopicsDirectMethod;

  @io.grpc.stub.annotations.RpcMethod(
      fullMethodName = SERVICE_NAME + '/' + "GenerateTopicsDirect",
      requestType = grpc.document.Generation.FileLocation.class,
      responseType = grpc.document.Generation.Topics.class,
      methodType = io.grpc.MethodDescriptor.MethodType.UNARY)
  public static io.grpc.MethodDescriptor<grpc.document.Generation.FileLocation,
      grpc.document.Generation.Topics> getGenerateTopicsDirectMethod() {
    io.grpc.MethodDescriptor<grpc.document.Generation.FileLocation, grpc.document.Generation.Topics> getGenerateTopicsDirectMethod;
    if ((getGenerateTopicsDirectMethod = TopicGenerationGrpc.getGenerateTopicsDirectMethod) == null) {
      synchronized (TopicGenerationGrpc.class) {
        if ((getGenerateTopicsDirectMethod = TopicGenerationGrpc.getGenerateTopicsDirectMethod) == null) {
          TopicGenerationGrpc.getGenerateTopicsDirectMethod = getGenerateTopicsDirectMethod = 
              io.grpc.MethodDescriptor.<grpc.document.Generation.FileLocation, grpc.document.Generation.Topics>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
              .setFullMethodName(generateFullMethodName(
                  "grpc.document.TopicGeneration", "GenerateTopicsDirect"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  grpc.document.Generation.FileLocation.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  grpc.document.Generation.Topics.getDefaultInstance()))
                  .setSchemaDescriptor(new TopicGenerationMethodDescriptorSupplier("GenerateTopicsDirect"))
                  .build();
          }
        }
     }
     return getGenerateTopicsDirectMethod;
  }

  private static volatile io.grpc.MethodDescriptor<grpc.document.Generation.FileLocation,
      grpc.document.Generation.FileLocation> getGenerateTopicsIndirectMethod;

  @io.grpc.stub.annotations.RpcMethod(
      fullMethodName = SERVICE_NAME + '/' + "GenerateTopicsIndirect",
      requestType = grpc.document.Generation.FileLocation.class,
      responseType = grpc.document.Generation.FileLocation.class,
      methodType = io.grpc.MethodDescriptor.MethodType.UNARY)
  public static io.grpc.MethodDescriptor<grpc.document.Generation.FileLocation,
      grpc.document.Generation.FileLocation> getGenerateTopicsIndirectMethod() {
    io.grpc.MethodDescriptor<grpc.document.Generation.FileLocation, grpc.document.Generation.FileLocation> getGenerateTopicsIndirectMethod;
    if ((getGenerateTopicsIndirectMethod = TopicGenerationGrpc.getGenerateTopicsIndirectMethod) == null) {
      synchronized (TopicGenerationGrpc.class) {
        if ((getGenerateTopicsIndirectMethod = TopicGenerationGrpc.getGenerateTopicsIndirectMethod) == null) {
          TopicGenerationGrpc.getGenerateTopicsIndirectMethod = getGenerateTopicsIndirectMethod = 
              io.grpc.MethodDescriptor.<grpc.document.Generation.FileLocation, grpc.document.Generation.FileLocation>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
              .setFullMethodName(generateFullMethodName(
                  "grpc.document.TopicGeneration", "GenerateTopicsIndirect"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  grpc.document.Generation.FileLocation.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  grpc.document.Generation.FileLocation.getDefaultInstance()))
                  .setSchemaDescriptor(new TopicGenerationMethodDescriptorSupplier("GenerateTopicsIndirect"))
                  .build();
          }
        }
     }
     return getGenerateTopicsIndirectMethod;
  }

  /**
   * Creates a new async stub that supports all call types for the service
   */
  public static TopicGenerationStub newStub(io.grpc.Channel channel) {
    return new TopicGenerationStub(channel);
  }

  /**
   * Creates a new blocking-style stub that supports unary and streaming output calls on the service
   */
  public static TopicGenerationBlockingStub newBlockingStub(
      io.grpc.Channel channel) {
    return new TopicGenerationBlockingStub(channel);
  }

  /**
   * Creates a new ListenableFuture-style stub that supports unary calls on the service
   */
  public static TopicGenerationFutureStub newFutureStub(
      io.grpc.Channel channel) {
    return new TopicGenerationFutureStub(channel);
  }

  /**
   * <pre>
   * The Generation service definition.
   * </pre>
   */
  public static abstract class TopicGenerationImplBase implements io.grpc.BindableService {

    /**
     * <pre>
     * Sends a request to get topics from a file
     * </pre>
     */
    public void generateTopicsDirect(grpc.document.Generation.FileLocation request,
        io.grpc.stub.StreamObserver<grpc.document.Generation.Topics> responseObserver) {
      asyncUnimplementedUnaryCall(getGenerateTopicsDirectMethod(), responseObserver);
    }

    /**
     */
    public void generateTopicsIndirect(grpc.document.Generation.FileLocation request,
        io.grpc.stub.StreamObserver<grpc.document.Generation.FileLocation> responseObserver) {
      asyncUnimplementedUnaryCall(getGenerateTopicsIndirectMethod(), responseObserver);
    }

    @java.lang.Override public final io.grpc.ServerServiceDefinition bindService() {
      return io.grpc.ServerServiceDefinition.builder(getServiceDescriptor())
          .addMethod(
            getGenerateTopicsDirectMethod(),
            asyncUnaryCall(
              new MethodHandlers<
                grpc.document.Generation.FileLocation,
                grpc.document.Generation.Topics>(
                  this, METHODID_GENERATE_TOPICS_DIRECT)))
          .addMethod(
            getGenerateTopicsIndirectMethod(),
            asyncUnaryCall(
              new MethodHandlers<
                grpc.document.Generation.FileLocation,
                grpc.document.Generation.FileLocation>(
                  this, METHODID_GENERATE_TOPICS_INDIRECT)))
          .build();
    }
  }

  /**
   * <pre>
   * The Generation service definition.
   * </pre>
   */
  public static final class TopicGenerationStub extends io.grpc.stub.AbstractStub<TopicGenerationStub> {
    private TopicGenerationStub(io.grpc.Channel channel) {
      super(channel);
    }

    private TopicGenerationStub(io.grpc.Channel channel,
        io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected TopicGenerationStub build(io.grpc.Channel channel,
        io.grpc.CallOptions callOptions) {
      return new TopicGenerationStub(channel, callOptions);
    }

    /**
     * <pre>
     * Sends a request to get topics from a file
     * </pre>
     */
    public void generateTopicsDirect(grpc.document.Generation.FileLocation request,
        io.grpc.stub.StreamObserver<grpc.document.Generation.Topics> responseObserver) {
      asyncUnaryCall(
          getChannel().newCall(getGenerateTopicsDirectMethod(), getCallOptions()), request, responseObserver);
    }

    /**
     */
    public void generateTopicsIndirect(grpc.document.Generation.FileLocation request,
        io.grpc.stub.StreamObserver<grpc.document.Generation.FileLocation> responseObserver) {
      asyncUnaryCall(
          getChannel().newCall(getGenerateTopicsIndirectMethod(), getCallOptions()), request, responseObserver);
    }
  }

  /**
   * <pre>
   * The Generation service definition.
   * </pre>
   */
  public static final class TopicGenerationBlockingStub extends io.grpc.stub.AbstractStub<TopicGenerationBlockingStub> {
    private TopicGenerationBlockingStub(io.grpc.Channel channel) {
      super(channel);
    }

    private TopicGenerationBlockingStub(io.grpc.Channel channel,
        io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected TopicGenerationBlockingStub build(io.grpc.Channel channel,
        io.grpc.CallOptions callOptions) {
      return new TopicGenerationBlockingStub(channel, callOptions);
    }

    /**
     * <pre>
     * Sends a request to get topics from a file
     * </pre>
     */
    public grpc.document.Generation.Topics generateTopicsDirect(grpc.document.Generation.FileLocation request) {
      return blockingUnaryCall(
          getChannel(), getGenerateTopicsDirectMethod(), getCallOptions(), request);
    }

    /**
     */
    public grpc.document.Generation.FileLocation generateTopicsIndirect(grpc.document.Generation.FileLocation request) {
      return blockingUnaryCall(
          getChannel(), getGenerateTopicsIndirectMethod(), getCallOptions(), request);
    }
  }

  /**
   * <pre>
   * The Generation service definition.
   * </pre>
   */
  public static final class TopicGenerationFutureStub extends io.grpc.stub.AbstractStub<TopicGenerationFutureStub> {
    private TopicGenerationFutureStub(io.grpc.Channel channel) {
      super(channel);
    }

    private TopicGenerationFutureStub(io.grpc.Channel channel,
        io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected TopicGenerationFutureStub build(io.grpc.Channel channel,
        io.grpc.CallOptions callOptions) {
      return new TopicGenerationFutureStub(channel, callOptions);
    }

    /**
     * <pre>
     * Sends a request to get topics from a file
     * </pre>
     */
    public com.google.common.util.concurrent.ListenableFuture<grpc.document.Generation.Topics> generateTopicsDirect(
        grpc.document.Generation.FileLocation request) {
      return futureUnaryCall(
          getChannel().newCall(getGenerateTopicsDirectMethod(), getCallOptions()), request);
    }

    /**
     */
    public com.google.common.util.concurrent.ListenableFuture<grpc.document.Generation.FileLocation> generateTopicsIndirect(
        grpc.document.Generation.FileLocation request) {
      return futureUnaryCall(
          getChannel().newCall(getGenerateTopicsIndirectMethod(), getCallOptions()), request);
    }
  }

  private static final int METHODID_GENERATE_TOPICS_DIRECT = 0;
  private static final int METHODID_GENERATE_TOPICS_INDIRECT = 1;

  private static final class MethodHandlers<Req, Resp> implements
      io.grpc.stub.ServerCalls.UnaryMethod<Req, Resp>,
      io.grpc.stub.ServerCalls.ServerStreamingMethod<Req, Resp>,
      io.grpc.stub.ServerCalls.ClientStreamingMethod<Req, Resp>,
      io.grpc.stub.ServerCalls.BidiStreamingMethod<Req, Resp> {
    private final TopicGenerationImplBase serviceImpl;
    private final int methodId;

    MethodHandlers(TopicGenerationImplBase serviceImpl, int methodId) {
      this.serviceImpl = serviceImpl;
      this.methodId = methodId;
    }

    @java.lang.Override
    @java.lang.SuppressWarnings("unchecked")
    public void invoke(Req request, io.grpc.stub.StreamObserver<Resp> responseObserver) {
      switch (methodId) {
        case METHODID_GENERATE_TOPICS_DIRECT:
          serviceImpl.generateTopicsDirect((grpc.document.Generation.FileLocation) request,
              (io.grpc.stub.StreamObserver<grpc.document.Generation.Topics>) responseObserver);
          break;
        case METHODID_GENERATE_TOPICS_INDIRECT:
          serviceImpl.generateTopicsIndirect((grpc.document.Generation.FileLocation) request,
              (io.grpc.stub.StreamObserver<grpc.document.Generation.FileLocation>) responseObserver);
          break;
        default:
          throw new AssertionError();
      }
    }

    @java.lang.Override
    @java.lang.SuppressWarnings("unchecked")
    public io.grpc.stub.StreamObserver<Req> invoke(
        io.grpc.stub.StreamObserver<Resp> responseObserver) {
      switch (methodId) {
        default:
          throw new AssertionError();
      }
    }
  }

  private static abstract class TopicGenerationBaseDescriptorSupplier
      implements io.grpc.protobuf.ProtoFileDescriptorSupplier, io.grpc.protobuf.ProtoServiceDescriptorSupplier {
    TopicGenerationBaseDescriptorSupplier() {}

    @java.lang.Override
    public com.google.protobuf.Descriptors.FileDescriptor getFileDescriptor() {
      return grpc.document.Generation.getDescriptor();
    }

    @java.lang.Override
    public com.google.protobuf.Descriptors.ServiceDescriptor getServiceDescriptor() {
      return getFileDescriptor().findServiceByName("TopicGeneration");
    }
  }

  private static final class TopicGenerationFileDescriptorSupplier
      extends TopicGenerationBaseDescriptorSupplier {
    TopicGenerationFileDescriptorSupplier() {}
  }

  private static final class TopicGenerationMethodDescriptorSupplier
      extends TopicGenerationBaseDescriptorSupplier
      implements io.grpc.protobuf.ProtoMethodDescriptorSupplier {
    private final String methodName;

    TopicGenerationMethodDescriptorSupplier(String methodName) {
      this.methodName = methodName;
    }

    @java.lang.Override
    public com.google.protobuf.Descriptors.MethodDescriptor getMethodDescriptor() {
      return getServiceDescriptor().findMethodByName(methodName);
    }
  }

  private static volatile io.grpc.ServiceDescriptor serviceDescriptor;

  public static io.grpc.ServiceDescriptor getServiceDescriptor() {
    io.grpc.ServiceDescriptor result = serviceDescriptor;
    if (result == null) {
      synchronized (TopicGenerationGrpc.class) {
        result = serviceDescriptor;
        if (result == null) {
          serviceDescriptor = result = io.grpc.ServiceDescriptor.newBuilder(SERVICE_NAME)
              .setSchemaDescriptor(new TopicGenerationFileDescriptorSupplier())
              .addMethod(getGenerateTopicsDirectMethod())
              .addMethod(getGenerateTopicsIndirectMethod())
              .build();
        }
      }
    }
    return result;
  }
}
