import pygame
import random

pygame.init()
pygame.display.set_caption("Game Snake Python")
largura, altura = 1200, 800

tela = pygame.display.set_mode((largura, altura))
relogio = pygame.time.Clock()

fundo = (112, 128, 144)
cobrinha = (75, 0, 130)
contador = (0, 100, 0)
comidinha = (255, 165, 0)

tamanho_quadrado = 20
velocidade_jogo = 10


def gerar_comida():
    comida_x = round(random.randrange(0, largura - tamanho_quadrado) / 20.0) * 20.0
    comida_y = round(random.randrange(0, altura - tamanho_quadrado) / 20.0) * 20.0
    return comida_x, comida_y


def desenhar_comida(tamanho, comida_x, comida_y):
    pygame.draw.rect(tela, comidinha, [comida_x, comida_y, tamanho, tamanho])


def desenhar_cobra(tamanho, pixels):
    for pixel in pixels:
        pygame.draw.rect(tela, cobrinha, [pixel[0], pixel[1], tamanho, tamanho])


def desenhar_pontuacao(pontuacao):
    fonte = pygame.font.SysFont("Helvetica", 35)
    texto = fonte.render(f"Pontos: {pontuacao}", True, contador)
    tela.blit(texto, [1, 1])


def selecionar_velocidade(tecla):
    if tecla == pygame.K_DOWN:
        velocidade_x = 0
        velocidade_y = tamanho_quadrado
    elif tecla == pygame.K_UP:
        velocidade_x = 0
        velocidade_y = - tamanho_quadrado
    elif tecla == pygame.K_RIGHT:
        velocidade_x = tamanho_quadrado
        velocidade_y = 0
    elif tecla == pygame.K_LEFT:
        velocidade_x = - tamanho_quadrado
        velocidade_y = 0
    return velocidade_x, velocidade_y


def rodar_jogo():
    fim_jogo = False
    
    x = largura / 2
    y = altura / 2
    
    velocidade_x = 0
    velocidade_y = 0
    
    tamanho_cobra = 1
    pixels = []
    
    comida_x, comida_y = gerar_comida()
    
    
    while not fim_jogo:
        tela.fill(fundo)
        
        
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                fim_jogo = True
            elif evento.type == pygame.KEYDOWN:
                velocidade_x, velocidade_y = selecionar_velocidade(evento.key)
        
        
        desenhar_comida(tamanho_quadrado, comida_x, comida_y)
        
        if x < 0 or x >= largura or y < 0 or y >= altura:
            fim_jogo = True
        
        x += velocidade_x
        y += velocidade_y
        
        pixels.append([x, y])
        if len(pixels) > tamanho_cobra:
            del pixels[0]
        
        
        for pixel in pixels[:-1]:
            if pixel == [x, y]:
                fim_jogo = True
        
        
        desenhar_cobra(tamanho_quadrado, pixels)
        
        desenhar_pontuacao(tamanho_cobra - 1)
        
        pygame.display.update()
        
        if x == comida_x and y == comida_y:
            tamanho_cobra +=1
            comida_x, comida_y = gerar_comida()
            
        relogio.tick(velocidade_jogo)


rodar_jogo()