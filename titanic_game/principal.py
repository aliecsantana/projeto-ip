import pygame

# Inicialização do Pygame
pygame.init()

# Configurações da janela
largura_janela, altura_janela = 500, 700
janela = pygame.display.set_mode((largura_janela, altura_janela))
pygame.display.set_caption("Titanic Game - Versão Simplificada")

# Classe do Navio
class Navio:
    def __init__(self):
        self.largura = 60
        self.altura = 100
        self.x = largura_janela // 2 - self.largura // 2
        self.y = altura_janela - self.altura - 20
        self.velocidade = 5
        self.cor = (200, 200, 200)  # Cinza
    
    def desenhar(self, tela):
        pygame.draw.rect(tela, self.cor, (self.x, self.y, self.largura, self.altura))
    
    def mover(self, direcao):
        if direcao == "esquerda" and self.x > 0:
            self.x -= self.velocidade
        elif direcao == "direita" and self.x < largura_janela - self.largura:
            self.x += self.velocidade

# Criação do navio
navio = Navio()

# Loop principal simplificado
executando = True
while executando:
    # Eventos
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False
    
    # Controles
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        navio.mover("esquerda")
    if teclas[pygame.K_RIGHT]:
        navio.mover("direita")
    
    # Renderização
    janela.fill((0, 0, 100))  # Fundo azul marinho
    navio.desenhar(janela)
    pygame.display.update()

# Encerramento
pygame.quit()