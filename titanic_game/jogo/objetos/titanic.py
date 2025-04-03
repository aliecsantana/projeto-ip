import pygame

class Navio:
    def __init__(self, largura_janela, altura_janela):
        self.sprite = pygame.image.load("titanic_game/sprites/barco/barco.png")
        self.largura = 60
        self.altura = 100
        self.imagem = pygame.transform.scale(self.sprite, (self.largura, self.altura))
        self.x = largura_janela // 2 - self.largura // 2
        self.y = altura_janela - self.altura - 20
        self.velocidade = 5
    
    def mover(self, direcao, limite_largura):
        if direcao == "esquerda" and self.x > 0:
            self.x -= self.velocidade
        elif direcao == "direita" and self.x < limite_largura - self.largura:
            self.x += self.velocidade
    
    def desenhar(self, tela):
         tela.blit(self.imagem, (self.x, self.y))
    
    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.largura, self.altura)