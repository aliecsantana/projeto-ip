import pygame
from jogo.objetos.coletaveis_teste import criar_lista_coletaveis, criar_objeto_aleatorio
from jogo.objetos.titanic import Navio
from jogo.contador_coletaveis import Score

class JogoTitanic:
    def __init__(self):
        pygame.init()
        self.largura = 500
        self.altura = 700
        self.janela = pygame.display.set_mode((self.largura, self.altura))
        pygame.display.set_caption("Titanic Game")
        self.navio = Navio(self.largura, self.altura)
        self.coletaveis = criar_lista_coletaveis(self.largura, 10)
        self.contador = Score()
        self.clock = pygame.time.Clock()
        self.rodando = True

    def processar_eventos(self):
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                self.rodando = False

    def atualizar(self):
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
                from jogo.objetos.coletaveis_teste import Coletes, Tesouros, Relogios
                if isinstance(obj, Coletes):
                    self.contador.atualizar_contador("coletes")
                elif isinstance(obj, Tesouros):
                    self.contador.atualizar_contador("tesouros")
                elif isinstance(obj, Relogios):
                    self.contador.atualizar_contador("relogios")

                self.coletaveis.remove(obj)
                self.coletaveis.append(criar_objeto_aleatorio(self.largura))

    def renderizar(self):
        self.janela.fill((0, 0, 100))
        
        for obj in self.coletaveis:
            obj.desenhar(self.janela)
        
        self.navio.desenhar(self.janela)
        self.contador.desenhar(self.janela)
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