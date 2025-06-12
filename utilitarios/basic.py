import os, time
import json
from datetime import datetime

def limparTela():
    os.system('cls')

def agurdar(segundos):
    time.sleep(segundos)

def abrirBancoDados():
    try:
        banco = open("log.dat", "r")
    except:
        print("Arquivo de log não encontrado. Criando um novo arquivo.")
        banco = open("log.dat", "w")

def escreverDados(nome, pontos):
    banco = open("log.dat", "r")
    dados = banco.read()
    banco.close()
    if dados != "":
        dadosDict = json.loads(dados)
    else:
        dadosDict = {}

    data_br = datetime.now().strftime("%d/%m/%Y %H:%M:%S")
    dadosDict[nome] = (pontos, data_br)

    banco = open("log.dat", "w")
    banco.write(json.dumps(dadosDict))
    banco.close()