import pygame
import tkinter as tk
from tkinter import messagebox
from utilitarios.basic import limparTela, agurdar
from utilitarios.basic import abrirBancoDados, escreverDados
import json

pygame.init()
abrirBancoDados()
tamanho = (1000, 700)
relogio = pygame.time.Clock()
tela = pygame.display.set_mode(tamanho)
pygame.display.set_caption("Projeto Final")
icone = pygame.image.load("recursos/icone.png")
pygame.display.set_icon(icone)
branco = (255, 255, 255)
preto = (0, 0, 0)
player = pygame.image.load("recursos/boneco.png")
fundoJogo = pygame.image.load("recursos/fundoJogo.jpg")
sol = pygame.image.load("recursos/sol.png")
bolaFogo = pygame.image.load("recursos/bolaFogo.png")


def jogar():
    larguraJanela = 300
    alturaJanela = 50
    def obter_nome():
        global nome
        nome = entry_nome.get()
        if not nome:
            messagebox.showerror("Erro", "Por favor, insira um nome.")
        else:
            root.destroy()

    root = tk.Tk()
    larguraTela = root.winfo_screenwidth()
    alturaTela = root.winfo_screenheight()
    pos_x = (larguraTela - larguraJanela) // 2
    pos_y = (alturaTela - alturaJanela) // 2
    root.geometry(f"{larguraJanela}x{alturaJanela}+{pos_x}+{pos_y}")
    root.title("Insira seu nickname")
    root.protocol("WM_DELETE_WINDOW", obter_nome)

    entry_nome = tk.Entry(root)
    entry_nome.pack()

    botao = tk.Button(root, text="Confirmar", command=obter_nome)
    botao.pack()
    root.mainloop()
    posicaoXPlayer = 500
    posicaoYPlayer = 300
    movimentoXPlayer = 0
    posicaoXBolaFogo = 500
    posicaoYBolaFogo = -240
    pontos = 0








