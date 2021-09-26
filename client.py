from __future__ import print_function

import grpc
import bidirectional_pb2_grpc as bidirectional_pb2_grpc
import bidirectional_pb2 as bidirectional_pb2
from faker import Faker
import base64
import numpy as np
import cv2
import Settings
import os
import time
fake_data = Faker()
uuid = "sushant123"

with open("./images/sushant.jpeg", "rb") as f:
    im_b64 = base64.b64encode(f.read())  # Encode the picture into stream data, put it in the memory cache, and then convert it into string format

#p=os.path.join(Settings.BASE_DIRECTORY,Settings.UPLOAD_PATH,'pawan')
#print(p)

def registering_data(uuid):
    return bidirectional_pb2.RegisterMessage(
        message = uuid
    )

def make_data(fake_data):
    return bidirectional_pb2.Message(
        message=fake_data
    )

#print (fake_data.name())
def generate_messages():
    for _ in range(0,10):
        
        messages = [
            make_data(im_b64),
        
            
        ]
        for msg in messages:
            #print("Hello Server Sending you the %s" % msg.message)
            yield msg
            
def register_data():
    for _ in range(0,10):
        
        registering = [
            registering_data(uuid)
        ]
        


def send_message(stub):
    startTime = time.time()
    responses = stub.GetServerResponse(generate_messages())
    for response in responses:
       #print("Hello from the server received your %s" % response.message)
       pass
       
       
    endTime = time.time()
    print(str(endTime - startTime))
    pass
       


def run():
    with grpc.insecure_channel('localhost:50051') as channel:
        stub = bidirectional_pb2_grpc.BidirectionalStub(channel)
        send_message(stub)


if __name__ == '__main__':
    run()