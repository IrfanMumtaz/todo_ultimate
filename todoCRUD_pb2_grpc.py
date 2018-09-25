# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
import grpc

import todoCRUD_pb2 as todoCRUD__pb2


class ToDoCRUDStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.tasks = channel.unary_stream(
        '/todoCRUD.ToDoCRUD/tasks',
        request_serializer=todoCRUD__pb2.AllRequest.SerializeToString,
        response_deserializer=todoCRUD__pb2.SingleResponse.FromString,
        )
    self.taskSingle = channel.unary_unary(
        '/todoCRUD.ToDoCRUD/taskSingle',
        request_serializer=todoCRUD__pb2.SingleRequest.SerializeToString,
        response_deserializer=todoCRUD__pb2.SingleResponse.FromString,
        )
    self.taskCreate = channel.unary_unary(
        '/todoCRUD.ToDoCRUD/taskCreate',
        request_serializer=todoCRUD__pb2.CreateRequest.SerializeToString,
        response_deserializer=todoCRUD__pb2.SingleResponse.FromString,
        )
    self.taskUpdate = channel.unary_unary(
        '/todoCRUD.ToDoCRUD/taskUpdate',
        request_serializer=todoCRUD__pb2.UpdateRequest.SerializeToString,
        response_deserializer=todoCRUD__pb2.SingleResponse.FromString,
        )
    self.taskDelete = channel.unary_unary(
        '/todoCRUD.ToDoCRUD/taskDelete',
        request_serializer=todoCRUD__pb2.SingleRequest.SerializeToString,
        response_deserializer=todoCRUD__pb2.DeleteResponse.FromString,
        )


class ToDoCRUDServicer(object):
  # missing associated documentation comment in .proto file
  pass

  def tasks(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def taskSingle(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def taskCreate(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def taskUpdate(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')

  def taskDelete(self, request, context):
    # missing associated documentation comment in .proto file
    pass
    context.set_code(grpc.StatusCode.UNIMPLEMENTED)
    context.set_details('Method not implemented!')
    raise NotImplementedError('Method not implemented!')


def add_ToDoCRUDServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'tasks': grpc.unary_stream_rpc_method_handler(
          servicer.tasks,
          request_deserializer=todoCRUD__pb2.AllRequest.FromString,
          response_serializer=todoCRUD__pb2.SingleResponse.SerializeToString,
      ),
      'taskSingle': grpc.unary_unary_rpc_method_handler(
          servicer.taskSingle,
          request_deserializer=todoCRUD__pb2.SingleRequest.FromString,
          response_serializer=todoCRUD__pb2.SingleResponse.SerializeToString,
      ),
      'taskCreate': grpc.unary_unary_rpc_method_handler(
          servicer.taskCreate,
          request_deserializer=todoCRUD__pb2.CreateRequest.FromString,
          response_serializer=todoCRUD__pb2.SingleResponse.SerializeToString,
      ),
      'taskUpdate': grpc.unary_unary_rpc_method_handler(
          servicer.taskUpdate,
          request_deserializer=todoCRUD__pb2.UpdateRequest.FromString,
          response_serializer=todoCRUD__pb2.SingleResponse.SerializeToString,
      ),
      'taskDelete': grpc.unary_unary_rpc_method_handler(
          servicer.taskDelete,
          request_deserializer=todoCRUD__pb2.SingleRequest.FromString,
          response_serializer=todoCRUD__pb2.DeleteResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'todoCRUD.ToDoCRUD', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
