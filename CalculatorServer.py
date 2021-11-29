from concurrent import futures
import logging
import time

import grpc
import Calculator_pb2
import Calculator_pb2_grpc


_ONE_DAY_IN_SECONDS = 60 * 60 * 24


class Calculator(Calculator_pb2_grpc.CalculatorServicer):
    pass


def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    Calculator_pb2_grpc.add_CalculatorServicer_to_server(Calculator(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    try:
        while True:
            time.sleep(_ONE_DAY_IN_SECONDS)
    except KeyboardInterrupt:
        server.stop(0)



if __name__ == '__main__':
    logging.basicConfig()
    serve()
