#encoding: utf-8
from Bots.BotSulMatogrossense import BotSulMatogrossense
from SistemaChatBot import SistemaChatBot as scb
from Bots.BotZangado import BotZangado

###construa a lista de bots disponíveis aqui
lista_bots = [BotZangado("Yoda")]
lista_bots = [BotSulMatogrossense("Maria")]
sys = scb.SistemaChatBot("CrazyBots",lista_bots)
sys.inicio()
