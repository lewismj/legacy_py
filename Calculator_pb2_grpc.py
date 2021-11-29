import grpc

import Calculator_pb2 as Calculator__pb2


class CalculatorStub(object):
  # missing associated documentation comment in .proto file
  pass

  def __init__(self, channel):
    """Constructor.

    Args:
      channel: A grpc.Channel.
    """
    self.Execute = channel.unary_unary(
        '/Calculator/Execute',
        request_serializer=Calculator__pb2.CalcRequest.SerializeToString,
        response_deserializer=Calculator__pb2.CalcResponse.FromString,
        )


class CalculatorServicer(object):

  def Execute(self, request, context):
      response = Calculator__pb2.CalcResponse() 
      response.result = request.a + request.b
      return response 


def add_CalculatorServicer_to_server(servicer, server):
  rpc_method_handlers = {
      'Execute': grpc.unary_unary_rpc_method_handler(
          servicer.Execute,
          request_deserializer=Calculator__pb2.CalcRequest.FromString,
          response_serializer=Calculator__pb2.CalcResponse.SerializeToString,
      ),
  }
  generic_handler = grpc.method_handlers_generic_handler(
      'Calculator', rpc_method_handlers)
  server.add_generic_rpc_handlers((generic_handler,))
