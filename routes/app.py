from fastapi import APIRouter
from os import listdir as ld
from bson.objectid import ObjectId
from models.app import testFile
from os import path as pth
from config.db import conn

routes = APIRouter()

@routes.post('/probando')
def postTest(text: testFile):
    filesave = []
    for i in text.id:
        file = conn.local.files.find_one({"_id": ObjectId(i)})
        fname = file["name"]
        filesave.append(fname)
        with open(f'./document/{fname}', 'wb') as f:
            f.write(file["data"])
    print(filesave)
    return 'ok'

@routes.get('/probando')
def getTest():
    print('Hola mundo2')
    return 'ok'