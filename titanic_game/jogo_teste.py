import pygame
from coletaveis_teste import criar_lista_coletaveis, criar_objeto_aleatorio

class Navio:
    def __init__(self, largura_janela, altura_janela):
        self.largura = 60
        self.altura = 100
        self.x = largura_janela // 2 - self.largura // 2
        self.y = altura_janela - self.altura - 20
        self.velocidade = 5
        self.cor = (200, 200, 200)
    
    def mover(self, direcao, limite_largura):
        if direcao == "esquerda" and self.x > 0:
            self.x -= self.velocidade
        elif direcao == "direita" and self.x < limite_largura - self.largura:
            self.x += self.velocidade
    
    def desenhar(self, tela):
        pygame.draw.rect(tela, self.cor, (self.x, self.y, self.largura, self.altura))
    
    def get_rect(self):
        return pygame.Rect(self.x, self.y, self.largura, self.altura)

class JogoTitanic:
    def __init__(self):
        pygame.init()
        self.largura = 500
        self.altura = 700
        self.janela = pygame.display.set_mode((self.largura, self.altura))
        pygame.display.set_caption("Titanic Game")
        self.navio = Navio(self.largura, self.altura)
        self.coletaveis = criar_lista_coletaveis(self.largura, 10)
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
                self.coletaveis.remove(obj)
                self.coletaveis.append(criar_objeto_aleatorio(self.largura))

    def renderizar(self):
        self.janela.fill((0, 0, 100))
        
        for obj in self.coletaveis:
            obj.desenhar(self.janela)
        
        self.navio.desenhar(self.janela)
        pygame.display.flip()

    def executar(self):
        while self.rodando:
            self.clock.tick(60)
            self.processar_eventos()
            self.atualizar()
            self.renderizar()
        
        pygame.quit()

if __name__ == "__main__":
    jogo = JogoTitanic()
    jogo.executar()