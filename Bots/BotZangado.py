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
            return "AAAAAAAAAAAAAAAAAAAAAAAA"
        elif cmd == 1: #Qual é seu nome?
            return "Não sabe ler!?!?"
        elif cmd == 2: #Quero um conselho
            return "Use o comando -1"
        elif cmd == 3: #Adeus
            return "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA\nEsse não é o comando -1"

    def boas_vindas(self):
        return "AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA"

    def despedida(self):
        return "Foi tarde"