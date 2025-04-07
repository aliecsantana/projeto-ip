import pygame
import random

pygame.init()

largura_tela = 800
altura_tela = 600
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.set_caption("Jogo dos Coletáveis")

tamanho_imagem = (45, 45)

img_colete = pygame.transform.scale(pygame.image.load("titanic_game/jogo/imagens/colete.png").convert_alpha(),tamanho_imagem)
img_tesouro = pygame.transform.scale(pygame.image.load("titanic_game/jogo/imagens/tesouro.png").convert_alpha(),tamanho_imagem)
img_relogio = pygame.transform.scale(pygame.image.load("titanic_game/jogo/imagens/relogio.png").convert_alpha(),tamanho_imagem)

class Coletaveis:
    def configurar(self, posicao_x, posicao_y, velocidade, imagem=None):
        self.posicao_x = posicao_x
        self.posicao_y = posicao_y
        self.velocidade = velocidade
        self.coletado = False
        self.imagem = imagem
        self.largura = 45
        self.altura = 45
        self.cor = (255, 255, 255)

    def mover(self):
        if not self.coletado:
            self.posicao_y += self.velocidade

    def desenhar(self, tela):
        if not self.coletado:
            if self.imagem:
                tela.blit(self.imagem, (self.posicao_x, self.posicao_y))
            else:
                pygame.draw.rect(tela, self.cor, (self.posicao_x, self.posicao_y, self.largura, self.altura))

    def verificar_colisao(self, area_jogador):
        if not self.coletado:
            area_objeto = pygame.Rect(self.posicao_x, self.posicao_y, self.largura, self.altura)
            if area_objeto.colliderect(area_jogador):
                self.coletado = True
                return True
        return False

class Coletes(Coletaveis):
    def configurar(self, posicao_x, posicao_y, velocidade, imagem):
        super().configurar(posicao_x, posicao_y, velocidade, imagem)
        self.largura, self.altura = imagem.get_size()

class Tesouros(Coletaveis):
    def configurar(self, posicao_x, posicao_y, velocidade, imagem):
        super().configurar(posicao_x, posicao_y, velocidade, imagem)
        self.largura, self.altura = imagem.get_size()

class Relogios(Coletaveis):
    def configurar(self, posicao_x, posicao_y, velocidade, imagem):
        super().configurar(posicao_x, posicao_y, velocidade, imagem)
        self.largura, self.altura = imagem.get_size()

velocidade_acumulada = 1

def criar_objeto_aleatorio(largura_tela):
    global velocidade_acumulada

    posicao_x = random.randint(20, largura_tela - 60)
    posicao_y = random.randint(-500, -30)
    velocidade = random.randint(2, 3) * velocidade_acumulada

    tipos = ["coletes", "tesouros", "relogios"]
    tipo = random.choices(tipos, weights=[1, 3, 1], k=1)[0]

    if tipo == "coletes":
        objeto = Coletes()
        objeto.configurar(posicao_x, posicao_y, velocidade, img_colete)
    elif tipo == "tesouros":
        objeto = Tesouros()
        objeto.configurar(posicao_x, posicao_y, velocidade, img_tesouro)
        velocidade_acumulada *= 1.02
    else:
        objeto = Relogios()
        objeto.configurar(posicao_x, posicao_y, velocidade, img_relogio)

    return objeto

def criar_lista_coletaveis(largura_tela, quantidade):
    nova_quantidade = max(1, quantidade // 3)
    return [criar_objeto_aleatorio(largura_tela) for i in range(nova_quantidade)]