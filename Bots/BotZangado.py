from Bots.Bot import Bot

class BotZangado(Bot):
    __com = {0: "Bom dia",
             1: "Qual é seu nome?",
             2: "Quero um conselho",
             3: "Adeus"}
    
    def __init__(self, nome):
        super().__init__(nome, self.__com)

    def apresentacao(self):
        return "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"
    
    def executa_comando(self, cmd):
        if cmd == 0: #Bom dia
            return "Bom dia AAAAAAAAAa"
        elif cmd == 1: #Qual é seu nome?
            return "Bom dia AAAAAAAAAa"
        elif cmd == 2: #Quero um conselho
            return "Quero um conselho AAAAAAAAAa"
        elif cmd == 3: #Adeus
            return "Adeus AAAAAAAAAa"

    def boas_vindas(self):
        return "Boas vindas AAAAAAAAAAAAaaa"

    def despedida(self):
        return "despeida AAAAAAAAAAAAaaa"