import pygame
import random # Importa a biblioteca random para gerar números aleatórios

# Classe base para todos os objetos coletáveis no jogo
class Coletaveis:
    # Função para configurar as propriedades básicas do objeto coletável
    def configurar(self, posicao_x, posicao_y, velocidade):
        self.posicao_x = posicao_x # Posição horizontal do objeto
        self.posicao_y = posicao_y # Posição vertical do objeto
        self.velocidade = velocidade # Velocidade de queda do objeto
        self.coletado = False # Indica se o objeto foi coletado pelo jogador
        self.largura = 30 # Largura do objeto
        self.altura = 30 # Altura do objeto
        self.cor = (255, 255, 255) # Cor do objeto (branco)
    
    # Função para mover o objeto verticalmente na tela
    def mover(self):
        if not self.coletado:
            self.posicao_y += self.velocidade # Move o objeto para baixo de acordo com sua velocidade
    
    # Função para desenhar o objeto na tela
    def desenhar(self, tela):
        if not self.coletado:
            pygame.draw.rect(tela, self.cor, (self.posicao_x, self.posicao_y, self.largura, self.altura)) # Desenha um retângulo representando o objeto
    
    # Função para verificar a colisão do objeto com o navio
    def verificar_colisao(self, area_jogador):
        if not self.coletado:
            area_objeto = pygame.Rect(self.posicao_x, self.posicao_y, self.largura, self.altura) # Cria um retângulo que representa a área do objeto
            if area_objeto.colliderect(area_jogador): # Verifica se há sobreposição com a área do jogador
                self.coletado = True
                return True
        return False

# Classe que representa os coletes salva-vidas
class Coletes(Coletaveis):
    def configurar(self, posicao_x, posicao_y, velocidade):
        super().configurar(posicao_x, posicao_y, velocidade) # Chama o método "configurar" da classe pai
        self.cor = (255, 255, 0) # Define a cor específica para coletes (amarelo)
    
    # Função para desenhar o colete na tela
    def desenhar(self, tela):
        if not self.coletado:
            pygame.draw.rect(tela, self.cor, (self.posicao_x, self.posicao_y, self.largura, self.altura)) # Desenha o retângulo base do colete
            # Desenha um triângulo preto no centro do colete
            pygame.draw.polygon(tela, (0, 0, 0), [
                (self.posicao_x + 5, self.posicao_y + 5), # Ponto superior esquerdo
                (self.posicao_x + self.largura - 5, self.posicao_y + 5), # Ponto superior direito
                (self.posicao_x + self.largura//2, self.posicao_y + self.altura - 5) # Ponto inferior central
            ])

# Classe que representa os tesouros
class Tesouros(Coletaveis):
    def configurar(self, posicao_x, posicao_y, velocidade):
        # Chama o método "configurar" da classe pai
        super().configurar(posicao_x, posicao_y, velocidade)
        self.cor = (212, 175, 55) # Define a cor específica para tesouros (dourado)
        self.largura = 35 # Largura específica para tesouros
        self.altura = 25 # Altura específica para tesouros
    
    # Função para desenhar o tesouro na tela
    def desenhar(self, tela):
        if not self.coletado:
            pygame.draw.rect(tela, self.cor, (self.posicao_x, self.posicao_y, self.largura, self.altura)) # Desenha o retângulo base do tesouro
            pygame.draw.rect(tela, (139, 69, 19), (self.posicao_x + 5, self.posicao_y, self.largura - 10, 5)) # Desenha uma faixa marrom no topo do tesouro

# Classe que representa os relógios
class Relogios(Coletaveis):
    def configurar(self, posicao_x, posicao_y, velocidade):
        super().configurar(posicao_x, posicao_y, velocidade) # Chama o método "configurar" da classe pai
        self.cor = (0, 0, 255) # Define a cor específica para relógios (azul)
        self.raio = 15 # Raio do círculo que representa o relógio
    
    # Função para desenhar o relógio na tela
    def desenhar(self, tela):
        if not self.coletado:
            # Calcula o centro do relógio
            centro_x = self.posicao_x + self.raio
            centro_y = self.posicao_y + self.raio
            pygame.draw.circle(tela, self.cor, (centro_x, centro_y), self.raio) # Desenha o círculo base do relógio
            pygame.draw.line(tela, (255, 255, 255), (centro_x, centro_y), (centro_x, centro_y - self.raio//2), 2) # Desenha o ponteiro dos minutos (linha vertical)
            pygame.draw.line(tela, (255, 255, 255), (centro_x, centro_y), (centro_x + self.raio//2, centro_y), 2) # Desenha o ponteiro das horas (linha horizontal)

# Função para criar um objeto coletável aleatório
def criar_objeto_aleatorio(largura_tela):
    posicao_x = random.randint(20, largura_tela - 40) # Gera uma posição x aleatória dentro dos limites da tela
    posicao_y = random.randint(-500, -30) # Gera uma posição y aleatória acima da tela
    velocidade = random.randint(3, 7) # Gera uma velocidade aleatória entre 3 e 7
    
    # Escolhe aleatoriamente um tipo de objeto entre as opções
    tipo = random.choice(["coletes", "tesouros", "relogios"])
    
    if tipo == "coletes":
        objeto = Coletes()
    elif tipo == "tesouros":
        objeto = Tesouros()
    else:
        objeto = Relogios()
    
    objeto.configurar(posicao_x, posicao_y, velocidade) # Configura o objeto com as propriedades geradas
    return objeto

# Função para criar uma lista de objetos coletáveis
def criar_lista_coletaveis(largura_tela, quantidade):
    return [criar_objeto_aleatorio(largura_tela) for i in range(quantidade)]