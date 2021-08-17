import random
class Comando:
    # recebe o id (inteiro), a mensagem e as respostas (opcional)
    def __init__(self, id, msg, respostas = []):
        self.__id = id
        self.__msg = msg 
        self.__respostas = respostas

    @property
    def id(self):
        return self.__id

    @property
    def mensagem(self):
        return self.__msg

    # retorna uma resposta aleatória
    def getRandomResposta(self):
        return random.choice(self.__respostas)

    # adiciona resposta
    def addResposta(self, resposta):
        self.__respostas.append(resposta)

    # remove resposta 
    def delResposta(self, resposta):
        self.__respostas.pop(resposta)