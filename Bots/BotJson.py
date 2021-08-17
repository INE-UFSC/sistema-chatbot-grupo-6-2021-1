# implemente as seguintes classes

from Bots.Bot import Bot
from Bots.Comando import Comando
import json


class BotJson(Bot):
    def __init__(self, comandos):
        if not (comandos.endswith(".json") or comandos.endswith(".json")):
            comandos += ".json"

        with open(comandos, 'r') as file:
            temp = json.load(file)[0]
            self.__apre = temp["apresentação"]
            self.__vindas = temp["boas vindas"]
            self.__despedida = temp["despedida"]
            comandos = {}
            for com in temp["comandos"]:
                comandos[com["id"]] = Comando(**com)
            self.__n_comandos = len(comandos)

            super().__init__(temp["nome"], comandos)

    def apresentacao(self):
        return self.__apre

    def executa_comando(self, cmd):
        return self.comandos[cmd].getRandomResposta()

    def boas_vindas(self):
        return self.__vindas

    def despedida(self):
        return self.__despedida
