import pygame
import random

class Coletaveis:
    def configurar(self, posicao_x, posicao_y, velocidade):
        self.posicao_x = posicao_x
        self.posicao_y = posicao_y
        self.velocidade = velocidade
        self.coletado = False
        self.largura = 30
        self.altura = 30
        self.cor = (255, 255, 255)
    
    def mover(self):
        if not self.coletado:
            self.posicao_y += self.velocidade
    
    def desenhar(self, tela):
        if not self.coletado:
            pygame.draw.rect(tela, self.cor, (self.posicao_x, self.posicao_y, self.largura, self.altura))
    
    def verificar_colisao(self, area_jogador):
        if not self.coletado:
            area_objeto = pygame.Rect(self.posicao_x, self.posicao_y, self.largura, self.altura)
            if area_objeto.colliderect(area_jogador):
                self.coletado = True
                return True
        return False

class Coletes(Coletaveis):
    def configurar(self, posicao_x, posicao_y, velocidade):
        super().configurar(posicao_x, posicao_y, velocidade)
        self.cor = (255, 255, 0)
    
    def desenhar(self, tela):
        super().desenhar(tela)
        pygame.draw.polygon(tela, (0, 0, 0), [
            (self.posicao_x + 5, self.posicao_y + 5),
            (self.posicao_x + self.largura - 5, self.posicao_y + 5),
            (self.posicao_x + self.largura//2, self.posicao_y + self.altura - 5)
        ])

class Tesouros(Coletaveis):
    def configurar(self, posicao_x, posicao_y, velocidade):
        super().configurar(posicao_x, posicao_y, velocidade)
        self.cor = (212, 175, 55)
        self.largura = 35
        self.altura = 25
    
    def desenhar(self, tela):
        super().desenhar(tela)
        pygame.draw.rect(tela, (139, 69, 19), (self.posicao_x + 5, self.posicao_y, self.largura - 10, 5))

class Relogios(Coletaveis):
    def configurar(self, posicao_x, posicao_y, velocidade):
        super().configurar(posicao_x, posicao_y, velocidade)
        self.cor = (0, 0, 255)
        self.raio = 15
    
    def desenhar(self, tela):
        if not self.coletado:
            centro_x = self.posicao_x + self.raio
            centro_y = self.posicao_y + self.raio
            pygame.draw.circle(tela, self.cor, (centro_x, centro_y), self.raio)
            pygame.draw.line(tela, (255, 255, 255), (centro_x, centro_y), (centro_x, centro_y - self.raio//2), 2)
            pygame.draw.line(tela, (255, 255, 255), (centro_x, centro_y), (centro_x + self.raio//2, centro_y), 2)

def criar_objeto_aleatorio(largura_tela):
    posicao_x = random.randint(20, largura_tela - 40)
    posicao_y = random.randint(-500, -30)
    velocidade = random.randint(2, 5)
    
    tipo = random.choice(["coletes", "tesouros", "relogios"])
    
    if tipo == "coletes":
        objeto = Coletes()
    elif tipo == "tesouros":
        objeto = Tesouros()
    else:
        objeto = Relogios()
    
    objeto.configurar(posicao_x, posicao_y, velocidade)
    return objeto

def criar_lista_coletaveis(largura_tela, quantidade):
    return [criar_objeto_aleatorio(largura_tela) for _ in range(quantidade)]