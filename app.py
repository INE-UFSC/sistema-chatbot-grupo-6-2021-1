#encoding: utf-8
from Bots.BotSulMatogrossense import BotSulMatogrossense
from Bots.BotZangado import BotZangado
from Bots.BotEsqueleto import BotEsqueleto
from SistemaChatBot import SistemaChatBot as scb

###construa a lista de bots disponíveis aqui
lista_bots = [BotZangado("Yoda"), BotSulMatogrossense("Maria"), BotEsqueleto("Thomas")]
sys = scb.SistemaChatBot("CrazyBots", lista_bots)
sys.inicio()
