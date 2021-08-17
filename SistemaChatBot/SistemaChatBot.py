import sys
from Bots import Bot


class SistemaChatBot:
    def __init__(self, nomeEmpresa, lista_bots: list[Bot, ]):
        self.__empresa = nomeEmpresa
        # verificar se a lista de bots contém apenas bots
        self.__lista_bots = lista_bots
        self.__bot = None

    def boas_vindas(self):
        print('Bem vindo ao sistema de chatos bots da empresa {}'.format(self.__empresa))
        # mostra mensagem de boas vindas do sistema

    def mostra_menu(self):
        print("Os chatbots disponíveis são:")
        for i in range(len(self.__lista_bots)):
            print(i, "- Bot: ",
                  self.__lista_bots[i].nome, "\t-",
                  self.__lista_bots[i].apresentacao())

    def escolhe_bot(self):
        while True:
            self.mostra_menu()  # mostra o menu ao usuário
            escolha = input('Digite o numero do chatbot desejado: ').strip()
            try:
                escolha = int(escolha)
            except ValueError:
                print('\nA entrada precisa ser um dos números abaixo')
                continue

            if escolha < len(self.__lista_bots) and escolha >= 0:
                self.__bot = self.__lista_bots[escolha]
                break
            else:
                print("\nValor inválido")

    def mostra_comandos_bot(self):
        print(self.__bot.mostra_comandos())
        # mostra os comandos disponíveis no bot escolhido

    def le_envia_comando(self):
        while True:
            self.mostra_comandos_bot()
            escolha = input('Digite o comando desejado (ou -1 para fechar o programa):').strip()
            try:
                escolha = int(escolha)
            except ValueError:
                print('\nComando deve ser um numero')
                continue
            break

        if escolha == -1:
            return False

        # faz a entrada de dados do usuário e executa o comando no bot ativo
        try:
            print(self.__bot.nome, ":", self.__bot.executa_comando(escolha))
        except KeyError:
            print("Comando inválido")
        return True

    def inicio(self):
        run = True

        self.boas_vindas()  # mostra mensagem de boas-vindas do sistema
        self.escolhe_bot()  # escolha do bot
        self.__bot.boas_vindas()  # mostra mensagens de boas-vindas do bot escolhido

        while run:
            # entra no loop de mostrar comandos do bot e escolher comando do bot até o usuário definir a saída
            run = self.le_envia_comando()

        print(self.__bot.despedida())

        # ao sair mostrar a mensagem de despedida do bot
