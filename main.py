import pygame, random
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
fonteMenu = pygame.font.SysFont("comicsansms",18)


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
    velocidadeBolaFogo = 5
    pontos = 0
    larguraPlayer = 250
    alturaPlayer = 127
    larguraBolaFogo = 50
    alturaBolaFogo = 250
    dificuldade = 30

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                quit()
            if evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_LEFT:
                    movimentoXPlayer = -5
                elif evento.key == pygame.K_RIGHT:
                    movimentoXPlayer = 5
                elif evento.key == pygame.K_SPACE:
                    posicaoXBolaFogo = posicaoXPlayer + 50
                    posicaoYBolaFogo = posicaoYPlayer - 50
            if evento.type == pygame.KEYUP:
                if evento.key in (pygame.K_LEFT, pygame.K_RIGHT):
                    movimentoXPlayer = 0

        posicaoXPlayer = posicaoXPlayer + movimentoXPlayer

        if posicaoXPlayer < 0:
            posicaoXPlayer = 15
        elif posicaoXPlayer > 800:
            posicaoXPlayer = 790

        tela.fill(branco)
        tela.blit(fundoJogo, (0, 0))
        tela.blit(player, (posicaoXPlayer, posicaoYPlayer))

        posicaoYBolaFogo = posicaoYBolaFogo + velocidadeBolaFogo
        if posicaoYBolaFogo > 600:
            posicaoYBolaFogo = -240
            pontos = pontos + 1
            velocidadeBolaFogo = velocidadeBolaFogo + 1
            posicaoXBolaFogo = random.randint(0, 1000)
            # pygame.mixer.Sound("recursos/bolaFogo.wav")
            posicaoXBolaFogo = random.randint(0, 1000)

        tela.blit( bolaFogo, (posicaoXBolaFogo, posicaoYBolaFogo) )

        textoPontos = fonteMenu.render("Pontos: " + str(pontos), True, branco)
        tela.blit(textoPontos, (15, 15))

        pixelsPlayerX = list(range(posicaoXPlayer, posicaoXPlayer + larguraPlayer))
        pixelsPlayerY = list(range(posicaoYPlayer, posicaoYPlayer + alturaPlayer))
        pixelsBolaFogoX = list(range(posicaoXBolaFogo, posicaoXBolaFogo + larguraBolaFogo))
        pixelsBolaFogoY = list(range(posicaoYBolaFogo, posicaoYBolaFogo + alturaBolaFogo))

        limparTela

        if len( list( set(pixelsBolaFogoY).intersection(set(pixelsPlayerY))) ) > dificuldade:
            if len( list ( set(pixelsBolaFogoX).intersection(set(pixelsPlayerX))  ) ) > 0:
                escreverDados(nome, pontos)
                dead()

        pygame.display.update()
        relogio.tick(60)

def start():
    larguraButtonStart = 150
    alturaButtonStart = 40
    larguraButtonQuit = 150
    alturaButtonQuit = 40


    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                quit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if startButton.collidepoint(evento.pos):
                    larguraButtonStart = 140
                    alturaButtonStart = 35
                if quitButton.collidepoint(evento.pos):
                    larguraButtonQuit = 140
                    alturaButtonQuit = 35

            elif evento.type == pygame.MOUSEBUTTONUP:
                if startButton.collidepoint(evento.pos):
                    larguraButtonStart = 150
                    alturaButtonStart = 40
                    jogar()
                if quitButton.collidepoint(evento.pos):
                    larguraButtonQuit = 150
                    alturaButtonQuit = 40
                    quit()

        tela.fill(branco)
        tela.blit(fundoJogo, (0,0) )

        startButton = pygame.draw.rect(tela, branco, (10,10, larguraButtonStart, alturaButtonStart), border_radius=15)
        startTexto = fonteMenu.render("Iniciar Game", True, preto)
        tela.blit(startTexto, (25,12))

        quitButton =pygame.draw.rect(tela, branco, (10,60, larguraButtonQuit, alturaButtonQuit), border_radius=15)
        quitTexto = fonteMenu.render("Sair do Game", True, preto)
        tela.blit(quitTexto, (25,62))

        pygame.display.update()
        relogio.tick(60)

def dead():
    pygame.mixer.music.stop()
    #pygame.mixer.Sound.play(explosaoSound)
    larguraButtonStart = 150
    alturaButtonStart = 40
    larguraButtonStart = 150
    alturaButtonStart = 40

    root = tk.Tk()
    root.title("Tela de Morte")

    label = tk.Label(root, text="Log das Partidas", font=("Arial", 16))
    label.pack(pady=10)

    listbox = tk.Listbox(root, width=50, height=10, selectmode=tk.SINGLE)
    listbox.pack(pady=20)

    log_partidas = open("base.atitus", "r").read()
    log_partidas = json.loads(log_partidas)
    for chave in log_partidas:
        listbox.insert(tk.END, f"Pontos: {log_partidas[chave][0]} na data: {log_partidas[chave][1]} - Nickname: {chave}")

    root.mainloop()
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                quit()
            elif evento.type == pygame.MOUSEBUTTONDOWN:
                if startButton.collidepoint(evento.pos):
                    larguraButtonStart = 140
                    alturaButtonStart = 35
                if quitButton.collidepoint(evento.pos):
                    larguraButtonQuit = 140
                    alturaButtonQuit = 35
            elif evento.type == pygame.MOUSEBUTTONUP:
                if startButton.collidepoint(evento.pos):
                    larguraButtonStart = 150
                    alturaButtonStart = 40
                    jogar()
                if quitButton.collidepoint(evento.pos):
                    larguraButtonQuit = 150
                    alturaButtonQuit = 40
                    quit()


        tela.fill(branco)
        tela.blit(fundoJogo, (0,0) )

        startButton = pygame.draw.rect(tela, branco, (10,10, larguraButtonStart, alturaButtonStart), border_radius=15)
        startTexto = fonteMenu.render("Iniciar Game", True, preto)
        tela.blit(startTexto, (25,12))

        quitButton = pygame.draw.rect(tela,branco, (10,60, larguraButtonQuit, alturaButtonQuit), border_radius=15)
        quitTexto = fonteMenu.render("Sair do Game", True, preto)
        tela.blit(quitTexto, (25,62))

        pygame.display.update()
        relogio.tick(60)


start()