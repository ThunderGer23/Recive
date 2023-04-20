from fastapi import APIRouter
from os import listdir as ld
import ssl
from os import path as pth
from config.db import conn

routes = APIRouter()

@routes.get('/probando/${text}')
def getTest(text: dict):
    print(text["name"])
    return 'ok'

@routes.post('/probando')
def postTest():
    print('Hola mundo2')
    return 'ok'