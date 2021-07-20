from Bots.Bot import Bot

class BotSulMatogrossense(Bot):

    __com = {0: "Aôba!",
             1: "Qual é seu nome?",
             2: "Quero um téras",
             3: "Qual seu animal de estimação?",
             4: "Você mora na aldeia?",
             5: "Como é aí no Mato Grosso?",
             6: "Adeus"}

    def __init__(self, nome):
        super().__init__(nome, self.__com)  

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    def apresentacao(self):
        return "TaRrde! Eu sou o(a) {} e vim do interioRr".format(self.__nome)
    
    def executa_comando(self,cmd):
        if cmd == 0: 
            return "Aôooba! :)"
        elif cmd == 1: 
            return "meu nome é Maria, muito prazeRr!"
        elif cmd == 2: 
            return "Cê tá louco, tá frio!"
        elif cmd == 3: 
            return "Uma capivara."
        elif cmd == 4: 
            return "..."
        elif cmd == 5: 
            return "DO SUL."

    def boas_vindas(self):
        pass

    def despedida(self):
        pass