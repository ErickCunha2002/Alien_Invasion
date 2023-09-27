# Alien Invasion

O jogo "Alien Invasion" é um jogo de nave espacial desenvolvido usando a biblioteca Pygame em Python. O objetivo do jogo é destruir a frota de aliens enquanto desvia de seus ataques.

## Como Jogar

1. **Iniciar o Jogo**: Clique no botão "JOGAR" para iniciar o jogo.

2. **Movimentação da Nave**: Use as setas direcionais (→, ←) para mover a nave para a direita e para a esquerda, respectivamente.

3. **Atirar**: Pressione a barra de espaço para disparar projéteis contra os aliens.

4. **Fim de Jogo**: O jogo termina se os aliens atingirem a parte inferior da tela ou se a nave for atingida pelos aliens. Você tem várias vidas para tentar de novo!

## Estrutura do Código

O código está organizado em classes e módulos para manter uma estrutura limpa e modularizada. Aqui está uma visão geral da estrutura:

### Classes Principais

- **AlienInvasion**: Classe principal que gerencia o jogo e seus recursos.
- **Settings**: Classe para armazenar todas as configurações do jogo.
- **Ship**: Classe para representar a nave do jogador.
- **Bullet**: Classe para representar os projéteis disparados pela nave.
- **Alien**: Classe para representar os aliens inimigos.
- **GameStats**: Classe para rastrear estatísticas do jogo.
- **Button**: Classe para criar e manipular botões.
- **Scoreboard**: Classe para exibir a pontuação e as estatísticas na tela.

### Funções Principais

- **run_game()**: Função que inicia o loop principal do jogo.
- **_check_events()**: Função para responder a eventos de teclado e mouse.
- **_update_screen()**: Função para atualizar as imagens na tela.
- **_check_play_button()**: Função para iniciar o jogo quando o botão "JOGAR" é clicado.

## Dependências

Para executar o jogo, você precisa ter a biblioteca Pygame instalada. Caso não tenha, você pode instalá-la com o seguinte comando:

```bash
pip install pygame
```

## Como Executar

Para executar o jogo, basta rodar o script "alien_invasion.py" no Python:

```bash
python alien_invasion.py
```
