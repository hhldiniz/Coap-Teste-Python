# -*-coding:utf-8-*-
from pickle import GET

from aiocoap import *
from tkinter import *


class Coap:
    def __init__(self, master=None):
        self.frame1 = Frame(master)
        self.frame1.pack()
        self.label_frame1 = Label(self.frame1, text="Bem-vindo ao teste Coap com Python")
        self.label_frame1.pack()
        self.frame2 = Frame(master)
        self.frame2.pack()
        self.btn_get_luz = Button(self.frame2)
        self.btn_get_luz["text"] = "Sensor de Luz"
        self.btn_get_luz["width"] = 8
        self.btn_get_luz["command"] = self.__get_valor_luz
        self.btn_get_luz.pack()
        self.luz_valor = Label(self.frame2, text="Valor")
        self.luz_valor.pack(side=LEFT)
        self.btn_get_temp = Button(self.frame1)
        self.btn_get_temp["text"] = "Sensor de Temperatura"
        self.btn_get_temp["width"] = 16
        self.btn_get_temp["command"] = self.__get_valor_temperature
        self.btn_get_temp.pack()

    @staticmethod
    def __get_valor_luz():
        url = "coap:///light"
        print("luz")

    @staticmethod
    def __get_valor_temperature():
        url = "coap:///temperature"
        print("temperatura")


root = Tk()
Coap(root)
root.mainloop()

# while True:
#     server = "coap://"
#     print("1 - Valor do sensor de luz\n")
#     print("2 - Valor da temperatura\n")
#     op = int(input("Digite uma opção\n"))
#     if op == 1:
#         url = server + "/light"
#     elif op == 2:
#         url = server + "/temperature"
#     msg = Message(code=GET, uri=server)
#     print(msg)
