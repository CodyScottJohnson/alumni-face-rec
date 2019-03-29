import pandas
import grpc
from concurrent import futures
import time
import os
# import the generated classes
import face_rec_pb2
import face_rec_pb2_grpc
from rec import face_db


# import the original calculator.py

# create a class to define the server functions, derived from
# calculator_pb2_grpc.CalculatorServicer
class FaceRecServicer(face_rec_pb2_grpc.FaceRecServicer):
    def __init__(self):
        self.database = face_db.create_encoding_db()
    
    # calculator.square_root is exposed here
    # the request and response are of the data type
    # calculator_pb2.Number
    def AuthenticateFace(self, request, context):
        face_result = face_db.validate_face(request.face,self.database)
        if face_result['valid']:
            authenticated = face_rec_pb2.AuthenticatedResponse(authenticated=True)
            #response.authenticated.authenticated = True
            user = face_rec_pb2.User(first_name=face_result['user']['first_name'],
                                     last_name=face_result['user']['last_name'],
                                     user_name=face_result['user']['username'],
            )
            response = face_rec_pb2.ValidateResponse(api="v1",authenticated=authenticated,user=user)
            return response
        response.api = face_result["message"]
        return response


# create a gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))

# use the generated function `add_CalculatorServicer_to_server`
# to add the defined class to the server
face_rec_pb2_grpc.add_FaceRecServicer_to_server(
        FaceRecServicer(), server)

# listen on port 50051
print('Starting server. Listening on port 50051.')
server.add_insecure_port('[::]:50051')
server.start()

# since server.start() will not block,
# a sleep-loop is added to keep alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)