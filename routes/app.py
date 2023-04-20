from fastapi import APIRouter
from os import listdir as ld
import ssl
from os import path as pth
from config.db import conn

routes = APIRouter()

@routes.get('/probando')
def getTest():
    print('Hola mundo')
    return 'ok'

@routes.post('/probando')
def postTest():
    print('Hola mundo2')
    return 'ok'