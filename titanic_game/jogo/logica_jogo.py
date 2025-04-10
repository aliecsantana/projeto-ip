import pygame
import time

class LogicaJogo:
    def __init__(self, contador_score=None):
        # Inicializa as variáveis de tempo
        self.tempo_inicio = time.time()
        self.tempo_atual = 0
        self.tempo_limite = 180  # Limite de tempo; podemos ajustar
        self.fonte_timer = pygame.font.SysFont('Verdana', 24)
        self.contador_score = contador_score
        self.objetivo_coletes = 10  # Número de coletes necessários para vencer
        self.pausado = False
        self.tempo_pausado = 0  # Tempo total em que o jogo esteve pausado
        self.momento_pausa = 0  # Momento em que o jogo foi pausado
    
    def atualizar(self):
        # Se o jogo estiver pausado, não atualiza o tempo
        if not self.pausado:
            # Atualiza o tempo e retorna game over se o tempo acabar
            self.tempo_atual = time.time() - self.tempo_inicio - self.tempo_pausado
            self.tempo_restante = max(0, self.tempo_limite - self.tempo_atual)
            
            # Verifica se o jogador coletou coletes suficientes para vencer
            if self.contador_score and self.contador_score.obter_contagem("coletes") >= self.objetivo_coletes:
                return "game_won"
            
            # Verifica as condições de acabar o jogo
            if self.tempo_restante <= 0:
                return "game_over"
        
        return "continuar"
    
    def desenhar_timer(self, tela):
        # Mostra o tempo na tela
        minutos = int(self.tempo_restante // 60)
        segundos = int(self.tempo_restante % 60)
        
        texto_timer = f"Tempo: {minutos:02d}:{segundos:02d}"
        
        superficie_timer = self.fonte_timer.render(texto_timer, True, (255, 255, 255))
        
        tela.blit(superficie_timer, (tela.get_width() - superficie_timer.get_width() - 20, 20))
    
    def resetar_timer(self):
        # Reseta o tempo para o caso de um novo jogo
        self.tempo_inicio = time.time()
        self.tempo_pausado = 0
        self.pausado = False
    
    def reduzir_tempo(self, segundos=5):
        # Reduz o tempo limite quando o navio bate em um iceberg
        self.tempo_limite = max(0, self.tempo_limite - segundos)
    
    def aumentar_tempo(self, segundos=5):
        # Aumenta o tempo limite quando o navio coleta um relógio
        self.tempo_limite += segundos
    
    def definir_contador(self, contador):
        self.contador_score = contador
        
    def alternar_pausa(self):
        # Alterna o estado de pausa
        if not self.pausado:
            # Pausando o jogo
            self.pausado = True
            self.momento_pausa = time.time()
        else:
            # Despausando o jogo
            self.pausado = False
            # Adiciona o tempo que ficou pausado ao contador total de tempo pausado
            self.tempo_pausado += time.time() - self.momento_pausa
