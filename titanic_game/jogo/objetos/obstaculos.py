import pygame
import random

class Obstaculo:
    imagem = pygame.image.load("titanic_game/jogo/imagens/iceberg.png")
    imagem = pygame.transform.scale(imagem, (50, 50))

    def __init__(self, posicao_x, posicao_y, velocidade):
        self.posicao_x = posicao_x
        self.posicao_y = posicao_y
        self.velocidade = velocidade
        self.largura = 50
        self.altura = 50
        self.atingido = False
    
    def mover(self):
        self.posicao_y += self.velocidade
    
    def desenhar(self, tela):
        tela.blit(Obstaculo.imagem, (self.posicao_x, self.posicao_y))
    
    def verificar_colisao(self, area_jogador):
        area_obstaculo = pygame.Rect(self.posicao_x, self.posicao_y, self.largura, self.altura)
        return area_obstaculo.colliderect(area_jogador)

def criar_obstaculo_aleatorio(largura_tela):
    posicao_x = random.randint(0, largura_tela - 50)
    posicao_y = random.randint(-500, -50)
    velocidade = random.uniform(1.0, 3.0)
    return Obstaculo(posicao_x, posicao_y, velocidade)

def criar_lista_obstaculos(largura_tela, quantidade):
    return [criar_obstaculo_aleatorio(largura_tela) for i in range(quantidade)]