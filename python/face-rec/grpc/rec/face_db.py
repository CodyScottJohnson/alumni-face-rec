import face_recognition
import base64
from io import BytesIO
import os
import json
import pandas as pd
import numpy

def create_encoding_db():
    people_frame = pd.read_csv("face-rec/users.csv")
    known_face_encodings = []
    for index,person in people_frame.iterrows():
        image = base64.b64decode(person["profile_photo"])
        known_image = face_recognition.load_image_file(BytesIO(image))
        Known_encoding = face_recognition.face_encodings(known_image)[0]
        known_face_encodings.append(Known_encoding)
    return {
        "users":people_frame,
        "encodings":known_face_encodings
    }
def validate_face(face_url,encodingdb):
    image = base64.b64decode(face_url)
    login_image = face_recognition.load_image_file(BytesIO(image))
    login_encoding = face_recognition.face_encodings(login_image)
    if not login_encoding:
        return {
            "valid":False,
            "message":"No Faces Found"
        }
    matches = face_recognition.compare_faces(encodingdb["encodings"], login_encoding[0])
    if True in matches:
        first_match_index = matches.index(True)                
        return {
            "valid":True,
            "message":"Valid User",
            "user":encodingdb['users'].iloc[first_match_index].to_dict()
        }
    else:
         return {
            "valid":False,
            "message":"Not a Valid User"
        }