import pygame
from jogo.objetos.coletaveis import criar_lista_coletaveis, criar_objeto_aleatorio
from jogo.objetos.obstaculos import criar_lista_obstaculos, criar_obstaculo_aleatorio
from jogo.objetos.titanic import Navio
from jogo.contador_coletaveis import Score
from jogo.logica_jogo import LogicaJogo
from jogo.telas import TelaInicial, TelaFimJogo, TelaObjetivo, TelaPausa


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
            print("Icone nao encontrado, usando padrao do pygame")
        
        self.carregar_recursos()
        self.inicializar_jogo()
        
        # Estado do jogo: "menu", "jogando", "pausado", "game_over", "game_won"
        self.estado_jogo = "menu"
        
        # Inicializa as telas
        self.tela_inicial = TelaInicial(self.largura, self.altura)
        self.tela_objetivo = None
        self.tela_fim_jogo = None
        self.tela_pausa = TelaPausa(self.largura, self.altura)
        
        self.clock = pygame.time.Clock()
        self.rodando = True
    
    def carregar_recursos(self):
        try:
            self.fundo = pygame.image.load("titanic_game/jogo/imagens/oceano.png").convert()
            self.fundo = pygame.transform.scale(self.fundo, (self.largura, self.altura))
        except Exception as e:
            print(f"Erro ao carregar imagem de fundo: {e}")
            print("Usando cor solida como fallback")
            self.fundo = None
    
    def inicializar_jogo(self):
        self.navio = Navio(self.largura, self.altura)
        self.coletaveis = criar_lista_coletaveis(self.largura, 10)
        self.obstaculos = criar_lista_obstaculos(self.largura, 5) 
        self.contador = Score()
        self.logica_jogo = LogicaJogo()
        self.logica_jogo.definir_contador(self.contador)
        self.logica_jogo.resetar_timer()
        self.tela_objetivo = TelaObjetivo(self.largura, self.altura)
        
    def processar_eventos(self):
        eventos = pygame.event.get()
        
        for evento in eventos:
            if evento.type == pygame.QUIT:
                self.rodando = False
                return
        
        if self.estado_jogo == "menu":
            pos_mouse = pygame.mouse.get_pos()
            self.tela_inicial.botao_comecar.verificar_hover(pos_mouse)
            self.tela_inicial.botao_sair.verificar_hover(pos_mouse)
            
            for evento in eventos:
                if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                    if self.tela_inicial.botao_comecar.verificar_clique(pos_mouse):
                        self.estado_jogo = "jogando"
                        self.inicializar_jogo()
                        return
                    if self.tela_inicial.botao_sair.verificar_clique(pos_mouse):
                        self.rodando = False
                        return
            return
        
        elif self.estado_jogo in ["game_over", "game_won"]:
            if self.tela_fim_jogo:
                pos_mouse = pygame.mouse.get_pos()
                self.tela_fim_jogo.botao_menu.verificar_hover(pos_mouse)
                self.tela_fim_jogo.botao_jogar_novamente.verificar_hover(pos_mouse)
                
                for evento in eventos:
                    if evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                        if self.tela_fim_jogo.botao_menu.verificar_clique(pos_mouse):
                            self.estado_jogo = "menu"
                            return
                        if self.tela_fim_jogo.botao_jogar_novamente.verificar_clique(pos_mouse):
                            self.estado_jogo = "jogando"
                            self.inicializar_jogo()
                            return
            return
        
        for evento in eventos:
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_SPACE:
                if self.estado_jogo == "jogando":
                    self.estado_jogo = "pausado"
                    self.logica_jogo.alternar_pausa()
                    return
                elif self.estado_jogo == "pausado":
                    self.estado_jogo = "jogando"
                    self.logica_jogo.alternar_pausa()
                    return

    def atualizar(self):
        if self.estado_jogo == "menu":
            self.tela_inicial.atualizar()
            return
        
        elif self.estado_jogo in ["game_over", "game_won"]:
            if self.tela_fim_jogo:
                self.tela_fim_jogo.atualizar()
            return
        
        elif self.estado_jogo == "pausado":
            # Quando pausado, não atualiza o jogo
            return
            
        # Atualização durante o jogo
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT] or teclas[pygame.K_a]:
            self.navio.mover("esquerda", self.largura)
        if teclas[pygame.K_RIGHT] or teclas[pygame.K_d]:
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
            self.tela_fim_jogo = TelaFimJogo(self.largura, self.altura, resultado)
      
    def renderizar(self):
        if self.estado_jogo == "menu":
            self.tela_inicial.desenhar(self.janela)
            return
        
        elif self.estado_jogo in ["game_over", "game_won"]:
            if self.tela_fim_jogo:
                self.tela_fim_jogo.desenhar(self.janela)
            return
        
        if self.fundo:
            self.janela.blit(self.fundo, (0, 0))
        else:
            self.janela.fill((0, 0, 100))
        
        # Desenha os outros elementos
        for obj in self.coletaveis:
            obj.desenhar(self.janela)

        for obstaculo in self.obstaculos:
            obstaculo.desenhar(self.janela)

        self.navio.desenhar(self.janela)
        self.contador.desenhar(self.janela)
        self.logica_jogo.desenhar_timer(self.janela)
        
        # Desenha a mensagem de objetivo se ainda estiver ativa
        if self.tela_objetivo and self.tela_objetivo.ainda_ativo():
            self.tela_objetivo.desenhar(self.janela)
        
        # Se o jogo estiver pausado, mostra a tela de pausa
        if self.estado_jogo == "pausado":
            self.tela_pausa.desenhar(self.janela)
        
        pygame.display.flip()
    
    def executar(self):
        while self.rodando:
            self.clock.tick(60)
            self.processar_eventos()
            self.atualizar()
            self.renderizar()
        
        self.contador.liberar_memoria()
        pygame.quit()

if __name__ == "__main__":
    jogo = JogoTitanic()
    jogo.executar()
