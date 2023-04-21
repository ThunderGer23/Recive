from fastapi import APIRouter
from os import listdir as ld
import ssl
from models.app import testFile
from os import path as pth
from config.db import conn

routes = APIRouter()

@routes.post('/probando')
def postTest(text: testFile):
    print(text.id)
    filesave = []
    file = conn.local.files.find_one({"_id": text.id})
    filename = file["name"]
    filebyte = file["data"]
    filesave.append(filename)
    with open(f'./document/{filename}', 'wb') as f:
            f.write(filebyte)
    return 'ok'

@routes.get('/probando')
def getTest():
    print('Hola mundo2')
    return 'ok'