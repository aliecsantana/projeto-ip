# 🚢 TitanCIn 1912

## ❓ Sobre o Projeto

Jogo desenvolvido em Python com o uso da biblioteca PyGame, inspirado no Titanic. O jogador deve desviar de obstáculos e coletar itens enquanto acumula pontos.

## 👥 Equipe e Divisão de Trabalho

- **Alice Santana `<ass11>`**: Criação dos objetos coletáveis, imagens e arquitetura do projeto  
- **Kraus Jatobá `<kjsj>`**: Criação dos obstáculos e sons  
- **Lucas Teixeira `<lta>`**: Criação dos objetos coletáveis  
- **Marcos Alexandre `<malb>`**: Criação da lógica do jogo e dos menus  

## 🧠 Arquitetura do Projeto

O projeto segue o paradigma de Orientação a Objetos e está estruturado da seguinte forma:

- `main.py`: ponto de entrada do jogo, onde o loop principal é iniciado  
- `navio.py`: classe do Titanic, controlado pelo jogador  
- `item.py`: define os itens coletáveis — coletes salva-vidas, relógios e baús  
- `iceberg.py`: classe responsável pelos obstáculos do tipo iceberg  
- `game.py`: gerencia a lógica geral do jogo, como colisões, pontuação e movimentação dos objetos  
- `utils.py`: funções auxiliares para carregamento de imagens e verificação de colisões  
- `assets/`: contém imagens, sons e capturas de tela utilizadas pelo jogo  

## 🖼️ Capturas de Tela

### Tela Inicial  
![Tela Inicial](assets/screenshots/tela_inicial.png)

### Em Jogo  
![Em Jogo](assets/screenshots/em_jogo.png)

### Game Over  
![Game Over](assets/screenshots/game_over.png)

## 🛠️ Ferramentas, Bibliotecas e Frameworks

- **Python 3.10**: Linguagem principal do projeto  
- **PyGame**: Biblioteca para desenvolvimento de jogos 2D  
  - *Justificativa*: Oferece uma estrutura acessível para jogos com suporte a sprites, colisões, áudio e controle de eventos  
- **VSCode**: Editor de código utilizado por todos os membros  
- **GitHub**: Utilizado para controle de versão e colaboração em equipe  

## 💡 Conceitos Utilizados

- **Orientação a Objetos**  
- **Listas e métodos de lista**  
- **Estruturas condicionais**  
- **Loops**  
- **Eventos do teclado**  
- **Funções**  

## 💥 Desafios e Lições Aprendidas

### ❌ Maior Erro

Subestimamos o tempo necessário para integrar todas as partes do jogo. Começamos codando separadamente e deixamos a integração para o fim, o que gerou conflitos.

**Como resolvemos**: Realizamos reuniões de integração e refatoramos o código para melhorar a coesão.

### 🧊 Maior Desafio

Implementar as colisões entre os objetos, especialmente entre o navio, os icebergs e os itens coletáveis.

**Como resolvemos**: Estudamos a documentação do PyGame sobre `spritecollide()` e organizamos os objetos em grupos distintos para facilitar o controle.

### 📚 Lições Aprendidas

- A importância de definir uma boa arquitetura desde o início  
- Como utilizar bibliotecas externas e documentações oficiais  
- Como colaborar efetivamente utilizando Git e GitHub  
- A relevância da comunicação e do acompanhamento contínuo no projeto  

## ▶️ Como Rodar o Projeto

### 🧩 1. Clonando ou Baixando o Repositório

#### 🔁 Clonar com Git (recomendado)
git clone https://github.com/aliecsantana/projeto-ip.git
cd projeto-ip

#### 🐍 2. Instalando o Python 3.13.3
Acesse: https://www.python.org/downloads/release/python-3133/
Baixe o instalador correspondente ao seu sistema operacional e marque a opção "Add Python to PATH" durante a instalação.

#### 📦 3. Instalando o PyGame
No terminal, execute:
pip install pygame

#### ▶️ 4. Executando o Arquivo main.py
Certifique-se de estar na pasta correta e execute:
python main.py