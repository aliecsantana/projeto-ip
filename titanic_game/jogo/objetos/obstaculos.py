import pygame
import random

class Obstaculo:
    def __init__(self, posicao_x, posicao_y, velocidade):
        self.posicao_x = posicao_x
        self.posicao_y = posicao_y
        self.velocidade = velocidade
        self.largura = random.randint(30, 50)
        self.altura = random.randint(30, 50)
        self.cor = (200, 230, 255)
        self.atingido = False
    
    def mover(self):
        self.posicao_y += self.velocidade
    
    def desenhar(self, tela):
        pygame.draw.rect(tela, self.cor, (self.posicao_x, self.posicao_y, self.largura, self.altura))
        pygame.draw.rect(tela, (255, 255, 255), (self.posicao_x + 5, self.posicao_y + 5, 10, 10))
    
    def verificar_colisao(self, area_jogador):
        area_obstaculo = pygame.Rect(self.posicao_x, self.posicao_y, self.largura, self.altura)
        return area_obstaculo.colliderect(area_jogador)

def criar_obstaculo_aleatorio(largura_tela):
    posicao_x = random.randint(0, largura_tela - 60)
    posicao_y = random.randint(-500, -50)
    velocidade = random.uniform(1.0, 3.0)
    return Obstaculo(posicao_x, posicao_y, velocidade,)

def criar_lista_obstaculos(largura_tela, quantidade):
    return [criar_obstaculo_aleatorio(largura_tela) for _ in range(quantidade)]