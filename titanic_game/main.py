import pygame
from jogo.objetos.coletaveis import criar_lista_coletaveis, criar_objeto_aleatorio
from jogo.objetos.obstaculos import criar_lista_obstaculos, criar_obstaculo_aleatorio
from jogo.objetos.titanic import Navio
from jogo.contador_coletaveis import Score
from jogo.logica_jogo import LogicaJogo


class JogoTitanic:
    def __init__(self):
        pygame.init()
        self.largura = 500
        self.altura = 700
        self.janela = pygame.display.set_mode((self.largura, self.altura))
        pygame.display.set_caption("Titanic Game")
        
        try:
            icon = pygame.image.load("imagens/titanic_oceano.png") 
            pygame.display.set_icon(icon)
        except:
            print("Ícone não encontrado, usando padrão do pygame")
        
        try:
            self.fundo = pygame.image.load("titanic_game/jogo/imagens/oceano.png").convert()
            self.fundo = pygame.transform.scale(self.fundo, (self.largura, self.altura))
        except Exception as e:
            print(f"Erro ao carregar imagem de fundo: {e}")
            print("Usando cor sólida como fallback")
            self.fundo = None
        
        self.navio = Navio(self.largura, self.altura)
        self.coletaveis = criar_lista_coletaveis(self.largura, 10)
        self.obstaculos = criar_lista_obstaculos(self.largura, 5) 
        self.contador = Score()
        self.logica_jogo = LogicaJogo()
        self.logica_jogo.definir_contador(self.contador)
        self.clock = pygame.time.Clock()
        self.rodando = True
        self.estado_jogo = "jogando"  # Estados: jogando, game_over, game_won
        
    def processar_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.rodando = False

    def atualizar(self):
        if self.estado_jogo != "jogando":
            return
            
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT]:
            self.navio.mover("esquerda", self.largura)
        if teclas[pygame.K_RIGHT]:
            self.navio.mover("direita", self.largura)
        
        for obj in self.coletaveis[:]:
            obj.mover()
            
            if obj.posicao_y > self.altura:
                self.coletaveis.remove(obj)
                self.coletaveis.append(criar_objeto_aleatorio(self.largura))
            
            if obj.verificar_colisao(self.navio.get_rect()):
                from jogo.objetos.coletaveis import Coletes, Tesouros, Relogios
                if isinstance(obj, Coletes):
                    self.contador.atualizar_contador("coletes")
                elif isinstance(obj, Tesouros):
                    self.contador.atualizar_contador("tesouros")
                elif isinstance(obj, Relogios):
                    self.contador.atualizar_contador("relogios")
                    self.logica_jogo.aumentar_tempo(10)  # Aumenta o tempo ao coletar relógio

                self.coletaveis.remove(obj)
                self.coletaveis.append(criar_objeto_aleatorio(self.largura))
        
        for obstaculo in self.obstaculos[:]:
            obstaculo.mover()
           
            if obstaculo.posicao_y > self.altura:
                self.obstaculos.remove(obstaculo)
                novo_obstaculo = criar_obstaculo_aleatorio(self.largura)
                self.obstaculos.append(novo_obstaculo)

            if obstaculo.verificar_colisao(self.navio.get_rect()):
                self.logica_jogo.reduzir_tempo(5)  # Reduz o tempo ao bater em iceberg
                self.obstaculos.remove(obstaculo)
                self.obstaculos.append(criar_obstaculo_aleatorio(self.largura))
        
        # Verifica o estado do jogo
        resultado = self.logica_jogo.atualizar()
        if resultado != "continuar":
            self.estado_jogo = resultado
      
    def renderizar(self):
        # Desenha o fundo (imagem ou cor sólida)
        if self.fundo:
            self.janela.blit(self.fundo, (0, 0))
        else:
            self.janela.fill((0, 0, 100))  # Cor de fallback
        
        # Desenha os outros elementos
        for obj in self.coletaveis:
            obj.desenhar(self.janela)

        for obstaculo in self.obstaculos:
            obstaculo.desenhar(self.janela)

        self.navio.desenhar(self.janela)
        self.contador.desenhar(self.janela)
        self.logica_jogo.desenhar_timer(self.janela)
        
        # Desenha mensagens de fim de jogo
        if self.estado_jogo == "game_over":
            self.desenhar_mensagem("GAME OVER", (255, 0, 0))
        elif self.estado_jogo == "game_won":
            self.desenhar_mensagem("VOCÊ VENCEU!", (0, 255, 0))
            
        pygame.display.flip()
    
    def desenhar_mensagem(self, texto, cor):
        fonte = pygame.font.Font(None, 72)
        superficie = fonte.render(texto, True, cor)
        pos_x = self.largura // 2 - superficie.get_width() // 2
        pos_y = self.altura // 2 - superficie.get_height() // 2
        self.janela.blit(superficie, (pos_x, pos_y))

    def executar(self):
        while self.rodando:
            self.clock.tick(60)
            self.processar_eventos()
            self.atualizar()
            self.renderizar()
            
            if self.estado_jogo != "jogando":
                pygame.time.delay(3000)
                self.rodando = False
        
        self.contador.liberar_memoria()
        pygame.quit()

if __name__ == "__main__":
    jogo = JogoTitanic()
    jogo.executar()
