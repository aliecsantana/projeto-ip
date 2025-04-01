import pygame

# Inicializa o Pygame
pygame.init()

# Janela
largura_janela, altura_janela = 500, 700
janela = pygame.display.set_mode((largura_janela, altura_janela))
pygame.display.set_caption("Titanic Game")

# Fundo
fundo = pygame.image.load("sea.gif")
fundo = pygame.transform.scale(fundo, (largura_janela, altura_janela))

# Loop principal do jogo
executando = True
while executando:
    pygame.time.delay(50)  # Dá uma pausa para o jogo não rodar muito rápido

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False  # Se fechar a janela, termina o loop

    # Atualiza a tela
    pygame.display.update()

# Encerra o Pygame
pygame.quit()