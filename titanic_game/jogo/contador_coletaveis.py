import pygame
import sys

class Score:
    def __init__(self):
        #Contador dos coletáveis que o navio pegou até agora
        self.coletaveis = {
            "coletes": 0,
            "tesouros": 0,
            "relogios": 0,
        }
        #Fonte do contador
        self.fonte = pygame.font.SysFont('Arial', 20)
    
    def atualizar_contador(self, tipo_objeto):
        if tipo_objeto in self.coletaveis:
            self.coletaveis[tipo_objeto] += 1
    
    def desenhar(self, tela):
        #Desenha contador no topo da tela
        posicao_y = 10
        
        # Desenha cada contador
        for tipo, quantidade in self.coletaveis.items():
            texto = f"{tipo}: {quantidade}"
            superficie_texto = self.fonte.render(texto, True, (255, 255, 255))
            tela.blit(superficie_texto, (10, posicao_y))
            posicao_y += 25  # Espaçamento entre as linhas

    def obter_contagem(self, tipo_objeto):
        #Retorna a contagem atual de um tipo específico de objeto
        return self.coletaveis.get(tipo_objeto, 0)
    
    def liberar_memoria(self):
        # Limpa os contadores
        self.coletaveis = {
            "coletes": 0,
            "tesouros": 0,
            "relogios": 0,
        }
        # Libera a fonte
        self.fonte = None
