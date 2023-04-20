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
    return 'ok'

@routes.get('/probando')
def getTest():
    print('Hola mundo2')
    return 'ok'