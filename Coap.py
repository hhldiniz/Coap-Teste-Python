# -*-coding:utf-8-*-
from pickle import GET

from aiocoap import *

while True:
    server = "coap://"
    print("1 - Valor do sensor de luz\n")
    print("2 - Valor da temperatura\n")
    op = int(input("Digite uma opção\n"))
    if op == 1:
        url = server+"/luz"
    elif op == 2:
        url = server+"giro"
    else:
        url = server+"acel"
    msg = Message(code=GET, uri=server)
    print(msg)