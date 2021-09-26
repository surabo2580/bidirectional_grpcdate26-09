from __future__ import print_function

import grpc
import bidirectional_pb2_grpc as bidirectional_pb2_grpc
import bidirectional_pb2 as bidirectional_pb2
from faker import Faker
fake_data = Faker()


def make_data(fake_data):
    return bidirectional_pb2.Message(
        message=fake_data
    )


def generate_messages():
    for _ in range(0,10):
        
        messages = [
            make_data(fake_data.name()),
            make_data(fake_data.email()),
            
        ]
        for msg in messages:
            print("Hello Server Sending you the %s" % msg.message)
            yield msg


def send_message(stub):
    responses = stub.GetServerResponse(generate_messages())
    for response in responses:
        print("Hello from the server received your %s" % response.message)


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = bidirectional_pb2_grpc.BidirectionalStub(channel)
        send_message(stub)


if __name__ == '__main__':
    run()