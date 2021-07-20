##implemente as seguintes classes

from abc import ABC, abstractmethod
import random as r

class Bot(ABC):

    def __init__(self, nome,):
        self.nome = nome
        self.comandos = {}

    @property
    def nome(self):
        return self.nome

    @nome.setter
    def nome(self, nome):
        self.nome = nome

    def mostra_comandos(self):
        pass

    @abstractmethod
    def executa_comando(self,cmd):
        pass

    @abstractmethod
    def boas_vindas():
        pass
    
    @abstractmethod
    def despedida():
        pass