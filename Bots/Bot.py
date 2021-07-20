##implemente as seguintes classes

from abc import ABC, abstractmethod

class Bot(ABC):

    def __init__(self, nome, comandos):
        self.nome = nome
        self.__comandos = {}
        
        txt = []
        for cmd, desc in self.comandos.items():
            txt.append(str(cmd) + "/t - " + desc)
        self.__comandos_str = "/n".join(txt)

    @property
    def nome(self):
        return self.nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property()
    def comandos(self):
        return self.__comandos

    @abstractmethod
    def apresentacao(self):
        pass
    
    def mostra_comandos(self):
        return self.__comandos_str
    
    @abstractmethod
    def executa_comando(self, cmd):
        pass

    @abstractmethod
    def boas_vindas(self):
        pass
    
    @abstractmethod
    def despedida(self):
        pass