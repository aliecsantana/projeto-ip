import pygame

class Navio:
    def __init__(self, largura_janela, altura_janela):
        # Carrega a imagem do Titanic
        try:
            self.imagem = pygame.image.load("titanic_game/jogo/imagens/titanic.png")
            self.largura = 60
            self.altura = 100
            self.imagem = pygame.transform.scale(self.imagem, (self.largura, self.altura))
        except Exception as e:
            print(f"Erro ao carregar imagem do navio: {e}")
            # Caso a imagem não seja carregada
            self.imagem = None
            self.largura = 60
            self.altura = 100
            self.cor = (200, 200, 200)
            
        self.x = largura_janela // 2 - self.largura // 2
        self.y = altura_janela - self.altura - 20
        self.velocidade = 5

    def desenhar(self, tela):
        if self.imagem:
            tela.blit(self.imagem, (self.x, self.y))
        else:
            # Caso a imagem não seja carregada
            pygame.draw.rect(tela, self.cor, (self.x, self.y, self.largura, self.altura))

    def mover(self, direcao, limite_largura):
        if direcao == "esquerda" and self.x > 0:
            self.x -= self.velocidade
        elif direcao == "direita" and self.x < limite_largura - self.largura:
            self.x += self.velocidade

    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.largura, self.altura)
