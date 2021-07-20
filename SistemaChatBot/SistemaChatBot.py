import sys
sys.path.insert(0, '..') # to import modules from parent folder 

from Bots.Bot import Bot


class SistemaChatBot:
    def __init__(self, nomeEmpresa, lista_bots):
        self.__empresa = nomeEmpresa
        # verificar se a lista de bots contém apenas bots
        self.__lista_bots = lista_bots
        self.__bot = None

    def boas_vindas(self):
        print('Bem vindo ao sistema de chatos bots da empresa {}').format(self.__empresa)
        # mostra mensagem de boas vindas do sistema

    def mostra_menu(self):
        print("Os chatbots disponíveis são:")
        for i in range(len(self.__lista_bots)):
            print(i, "- Bot: ",
                  self.__lista_bots[i].nome,
                  self.__lista_bots[i].apresentacao())

    def escolhe_bot(self):
        while True:
            escolha = input('Digite o numero do chatbot desejado: ').strip()
            try:
                escolha = int(escolha)
            except:
                print('entrada invalida')
                continue
            
            if escolha < len(self.__lista_bots) and escolha >= 0:
                self.__bot = self.__lista_bots[escolha]
                break

        # faz a entrada de dados do usuário e atribui o objeto ao atributo __bot

    def mostra_comandos_bot(self):
        print(self.__bot.mostra_comandos())
        # mostra os comandos disponíveis no bot escolhido

    def le_envia_comando(self):
        escolha = int(
            input('Digite o comando desejado (ou -1 para fechar o programa):'))

        if escolha == -1:
            return False

        # faz a entrada de dados do usuário e executa o comando no bot ativo
        print(self.__bot.executa_comando(escolha))
        return True

    def inicio(self):
        run = True

        self.boas_vindas()  # mostra mensagem de boas-vindas do sistema
        self.mostra_menu()  # mostra o menu ao usuário
        self.escolhe_bot()  # escolha do bot
        self.__bot.boas_vindas()  # mostra mensagens de boas-vindas do bot escolhido

        while run:
            # entra no loop de mostrar comandos do bot e escolher comando do bot até o usuário definir a saída
            self.mostra_comandos_bot()
            run = self.le_envia_comando()

        print(self.__bot.despedida())

        # ao sair mostrar a mensagem de despedida do bot
