import grpc

import Calculator_pb2
import Calculator_pb2_grpc 


def run():
  channel = grpc.insecure_channel('localhost:50051')
  stub = Calculator_pb2_grpc.CalculatorStub(channel)
  response = stub.Execute(Calculator_pb2.CalcRequest(a=-5,b=12))
  print("Client received: " + str(response.result))


if __name__ == '__main__':
  run()
