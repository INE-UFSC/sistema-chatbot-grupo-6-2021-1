from Bots import BotJson, BotZangado
from Bots.BotSulMatogrossense import BotSulMatogrossense
from Bots.BotEsqueleto import BotEsqueleto
from SistemaChatBot import SistemaChatBot as scb

lista_bots = [BotSulMatogrossense("Maria"), BotEsqueleto("Thomas")]
lista_bots.append(BotZangado())
sys = scb.SistemaChatBot("CrazyBots", lista_bots)
sys.inicio()
