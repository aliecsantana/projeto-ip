import pygame
import sys
import time

class Botao:
    def __init__(self, x, y, largura, altura, texto, cor=(200, 200, 200), cor_hover=(150, 150, 150)):
        self.rect = pygame.Rect(x, y, largura, altura)
        self.texto = texto
        self.cor = cor
        self.cor_hover = cor_hover
        self.cor_atual = cor
        self.fonte = pygame.font.SysFont('Verdana', 22)
        self.ativo = True

    def desenhar(self, tela):
        if not self.ativo:
            return
            
        # Desenha o botão
        pygame.draw.rect(tela, self.cor_atual, self.rect, 0, 10)
        pygame.draw.rect(tela, (50, 50, 50), self.rect, 2, 10)
        
        # Desenha o texto
        texto_surface = self.fonte.render(self.texto, True, (0, 0, 0))
        texto_rect = texto_surface.get_rect(center=self.rect.center)
        tela.blit(texto_surface, texto_rect)
    
    def verificar_hover(self, pos_mouse):
        if not self.ativo:
            return False
            
        if self.rect.collidepoint(pos_mouse):
            self.cor_atual = self.cor_hover
            return True
        else:
            self.cor_atual = self.cor
            return False
    
    def verificar_clique(self, pos_mouse):
        if not self.ativo:
            return False
            
        return self.rect.collidepoint(pos_mouse)

class TelaInicial:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
        
        # Carrega a imagem de fundo
        try:
            self.fundo = pygame.image.load("titanic_game/jogo/imagens/menu.png").convert()
            self.fundo = pygame.transform.scale(self.fundo, (largura, altura))
        except Exception as e:
            print(f"Erro ao carregar imagem de menu: {e}")
            self.fundo = None
        
        # Cria os botões
        botao_largura = 200
        botao_altura = 50
        
        # Posiciona os botões na parte inferior da tela
        pos_x = largura // 2 - botao_largura // 2
        
        self.botao_comecar = Botao(pos_x, altura - 220, botao_largura, botao_altura, "Iniciar", 
                                   cor=(100, 200, 100), cor_hover=(80, 180, 80))
        
        self.botao_sair = Botao(pos_x, altura - 160, botao_largura, botao_altura, "Sair", 
                               cor=(200, 100, 100), cor_hover=(180, 80, 80))
        
        # Fonte para o texto de controles
        self.fonte_controles = pygame.font.SysFont('Verdana', 16)
    
    def atualizar(self):
        pos_mouse = pygame.mouse.get_pos()
        self.botao_comecar.verificar_hover(pos_mouse)
        self.botao_sair.verificar_hover(pos_mouse)
    
    def desenhar(self, tela):
        # Desenha o fundo
        if self.fundo:
            tela.blit(self.fundo, (0, 0))
        else:
            tela.fill((4, 22, 38))  # Cor de fundo alternativa
        
        # Desenha os botões
        self.botao_comecar.desenhar(tela)
        self.botao_sair.desenhar(tela)
        
        # Desenha o texto de controles no canto esquerdo
        linha1 = self.fonte_controles.render("Controles:", True, (255, 255, 255))
        linha2 = self.fonte_controles.render("Mover-se: A, D ou Setas", True, (255, 255, 255))
        linha3 = self.fonte_controles.render("Pausar: Barra de Espaço", True, (255, 255, 255))
        
        margem = 20  # Margem da borda esquerda
        tela.blit(linha1, (margem, self.altura - 80))
        tela.blit(linha2, (margem, self.altura - 60))
        tela.blit(linha3, (margem, self.altura - 40))
        
        pygame.display.flip()

class TelaFimJogo:
    def __init__(self, largura, altura, resultado, contador_score=None):
        self.largura = largura
        self.altura = altura
        self.resultado = resultado
        self.contador_score = contador_score
        
        # Cria os botões
        botao_largura = 200
        botao_altura = 50
        
        # Posiciona os botões no centro da tela
        pos_x = largura // 2 - botao_largura // 2
        
        self.botao_menu = Botao(pos_x, altura // 2 + 50, botao_largura, botao_altura, "Voltar ao Menu", 
                               cor=(100, 100, 200), cor_hover=(80, 80, 180))
        
        self.botao_jogar_novamente = Botao(pos_x, altura // 2 + botao_altura + 70, botao_largura, botao_altura, 
                                         "Jogar Novamente", cor=(100, 200, 100), cor_hover=(80, 180, 80))
        
        # Fonte para o texto de resultado
        self.fonte_resultado = pygame.font.SysFont('Verdana', 28, bold=True)
        self.fonte_detalhes = pygame.font.SysFont('Verdana', 20)
    
    def atualizar(self):
        pos_mouse = pygame.mouse.get_pos()
        self.botao_menu.verificar_hover(pos_mouse)
        self.botao_jogar_novamente.verificar_hover(pos_mouse)
    
    def desenhar(self, tela):
        # Desenha o fundo
        tela.fill((4, 22, 38))
        
        # Desenha o texto de resultado
        if self.resultado == "game_won":
            texto_parabens = "Parabéns!"
            texto = "Você venceu!!!"
            cor = (0, 255, 0)
            
            texto_parabens_surface = self.fonte_resultado.render(texto_parabens, True, cor)
            tela.blit(texto_parabens_surface, (self.largura // 2 - texto_parabens_surface.get_width() // 2, self.altura // 3 - 40))
        else:
            texto = "Parece que o tempo acabou..."
            cor = (255, 0, 0)
        
        texto_surface = self.fonte_resultado.render(texto, True, cor)
        tela.blit(texto_surface, (self.largura // 2 - texto_surface.get_width() // 2, self.altura // 3))
        
        # Informação sobre coletes coletados
        if self.contador_score:
            coletes_coletados = self.contador_score.obter_contagem("coletes")
            if self.resultado == "game_over":
                texto_coletes = f"Você coletou {coletes_coletados} de 10 coletes necessários."
                texto_coletes_surface = self.fonte_detalhes.render(texto_coletes, True, (255, 255, 255))
                tela.blit(texto_coletes_surface, (self.largura // 2 - texto_coletes_surface.get_width() // 2, self.altura // 3 + 40))
        
        # Desenha os botões
        self.botao_menu.desenhar(tela)
        self.botao_jogar_novamente.desenhar(tela)
        
        pygame.display.flip()

class TelaObjetivo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
        self.tempo_inicio = time.time()
        self.duracao = 5 #Tela de objetivo no inicio
        self.fonte = pygame.font.SysFont('Verdana', 24)
    
    def ainda_ativo(self):
        tempo_atual = time.time()
        return tempo_atual - self.tempo_inicio < self.duracao
    
    def desenhar(self, tela):
        if not self.ainda_ativo():
            return
        
        # Desenha o fundo
        superficie = pygame.Surface((self.largura, 100), pygame.SRCALPHA)
        superficie.fill((0, 0, 0, 180))
        tela.blit(superficie, (0, self.altura // 2 - 50))
        
        # Desenha o texto
        texto = "Obtenha 10 coletes para ganhar!"
        texto_surface = self.fonte.render(texto, True, (255, 255, 255))
        tela.blit(texto_surface, (self.largura // 2 - texto_surface.get_width() // 2, 
                                 self.altura // 2 - texto_surface.get_height() // 2))

class TelaPausa:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura
        self.fonte = pygame.font.SysFont('Verdana', 36)
    
    def desenhar(self, tela):
        # Desenha o fundo
        superficie = pygame.Surface((self.largura, 100), pygame.SRCALPHA)
        superficie.fill((0, 0, 0, 180))
        tela.blit(superficie, (0, self.altura // 2 - 50))
        
        # Desenha o texto
        texto = "PAUSADO"
        texto_surface = self.fonte.render(texto, True, (255, 255, 255))
        tela.blit(texto_surface, (self.largura // 2 - texto_surface.get_width() // 2, 
                                 self.altura // 2 - texto_surface.get_height() // 2))
