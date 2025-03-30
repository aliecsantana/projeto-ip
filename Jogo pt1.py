import pygame

# Inicializa o Pygame
pygame.init()

# Janela
largura_janela, altura_janela = 500, 700
janela = pygame.display.set_mode((largura_janela, altura_janela))
pygame.display.set_caption('Olha a pedra!!')

# Fundo
fundo = pygame.image.load("sea.gif")
fundo = pygame.transform.scale(fundo, (largura_janela, altura_janela))

# Barco
barco = pygame.image.load("boat.png")

# Novo tamanho do barco
novo_tamanho_barco = (100, 50)  # largura, altura em pixels
barco = pygame.transform.scale(barco, novo_tamanho_barco)

# Obtém as novas dimensões do barco
barco_largura, barco_altura = barco.get_size()

# Posiciona o barco no centro da tela, mas no fundo
x = (largura_janela - barco_largura) // 2
y = (altura_janela - barco_altura) 

# Velocidade do barco
velocidade = 10

# Loop principal do jogo
executando = True
while executando:
    pygame.time.delay(50)  # Dá uma pausa para o jogo não rodar muito rápido

    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            executando = False  # Se fechar a janela, termina o loop

    # Captura as teclas pressionadas
    teclas = pygame.key.get_pressed()

    # Move o barco conforme a tecla pressionada
    if teclas[pygame.K_LEFT] and x - velocidade >= 0:
        x -= velocidade  # Move para a esquerda
    if teclas[pygame.K_RIGHT] and x + velocidade <= largura_janela - barco_largura:
        x += velocidade  # Move para a direita
    if teclas[pygame.K_UP] and y - velocidade >= 0:
        y -= velocidade  # Move para cima
    if teclas[pygame.K_DOWN] and y + velocidade <= altura_janela - barco_altura:
        y += velocidade  # Move para baixo

    # Desenha o fundo e o barco na nova posição
    janela.blit(fundo, (0, 0))
    janela.blit(barco, (x, y))

    # Atualiza a tela
    pygame.display.update()

# Encerra o Pygame
pygame.quit()
