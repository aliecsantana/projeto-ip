import pygame

class Navio:
    def __init__(self, largura_janela, altura_janela):
        self.largura = 60
        self.altura = 100
        self.x = largura_janela // 2 - self.largura // 2
        self.y = altura_janela - self.altura - 20
        self.velocidade = 5
        self.cor = (200, 200, 200)
    
    def mover(self, direcao, limite_largura):
        if direcao == "esquerda" and self.x > 0:
            self.x -= self.velocidade
        elif direcao == "direita" and self.x < limite_largura - self.largura:
            self.x += self.velocidade
    
    def desenhar(self, tela):
        pygame.draw.rect(tela, self.cor, (self.x, self.y, self.largura, self.altura))
    
    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.largura, self.altura)