# implemente as seguintes classes

from Bots.Bot import Bot
from Bots.Comando import Comando
import json


class BotJson(Bot):
    def __init__(self, comandos):
        if not (comandos.endswith(".json") or comandos.endswith(".json")):
            comandos += ".json"

        with open(comandos, 'r') as file:
            temp = json.load(file)
            self.nome = temp["nome"]
            self.__apre = temp["apresentação"]
            self.__vindas = temp["boas vindas"]
            self.__despedida = temp["despedida"]
            self.__comandos = {}
            for com in temp["comandos"]:
                self.comandos[com["id"]] = Comando(**com)
            self.__n_comandos = len(self.__comandos)

        txt = []
        for id, comando in self.__comandos.items():
            txt.append(str(id) + "\t - " + comando.mensagem)
        self.__comandos_str = "\n".join(txt)

    def apresentacao(self):
        return self.__apre

    def executa_comando(self, cmd):
        try:
            self.__comandos[cmd]
        except:
            print("Comando não encontrado")
            raise

    def boas_vindas(self):
        return self.__vindas

    def despedida(self):
        return self.__despedida
