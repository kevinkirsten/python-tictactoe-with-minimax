
# Jogo da Velha com MINIMAX

Um Jogo da Velha desenvolvido em Python utilizando o algoritmo Minimax.

Utilizado como parte da avaliação para a disciplina MAC0425 - Inteligência Artificial (1.º semestre de 2021)

Ministrada pelo Professor Dr. Flavio Soares Correa da Silva do IME-USP (Instituto de Matemática e Estatística da Universidade de São Paulo)

## Execute na nuvem

Acesse e teste este código em:

[https://replit.com/@kevinkirsten/python-tictactoe-with-minimax](https://replit.com/@kevinkirsten/python-tictactoe-with-minimax)

## Execute Localmente

Certifique-se de ter o [Python 3](https://www.python.org/) instalado.

Clone o projeto.

```bash
  git clone https://github.com/kevinkirsten/python-tictactoe-with-minimax
```

Vá até o diretório do projeto.

```bash
  cd python-tictactoe-with-minimax
```

Rode o arquivo em seu computador.

## Lições Aprendidas

Com o desenvolvimento deste jogo da velha, entendi o funcionamento do algoritmo Minimax em relação a sua funcionalidade para maximizar os ganhos mínimos, e minimizar as perdas máximas de uma partida.

### Os principais pontos do algoritmo são:
- É um algoritmo recursivo usado para a tomada de decisões em teoria dos jogos. Ele fornece o melhor movimento para o jogador assumindo que o oponente também está jogando da maneira mais otimizada possível.
- O algoritmo utiliza a Recursão e Busca em Profundidade para procurar através de uma árvore com as possíveis jogadas de ambos os jogadores.
- É amplamente utilizado em jogos de turno com dois jogadores tais como o Xadrez, Damas, Go/Weiqi/Baduk e entre outros.

### Em resumo, o funcionamento do algoritmo pode ser descrito como:
- Temos dois jogadores, um denominado MAX e outro MIN, ambos são oponentes um do outro.
- Tomamos um determinado estado inicial do tabuleiro.
- É então executado um algoritmo de Busca em Profundidade (DFS) para a exploração de toda a árvore de possibilidades do jogo.
- Para cada jogada da árvore de possibilidades é dada uma pontuação:
    - Quando o jogador MAX ganha, a jogada ganha um score = **+1**.
    - Quando o jogador MAX perde, a jogada ganha um score = **-1**.
    - Quando acontece um empate, a jogada ganha um score = **0**. 
- Em seguida, para a respectiva jogada de cada jogador:
  - O jogador MAX selecionará o valor **maximizado**.
  - O jogador MIN selecionará o valor **minimizado**.
- O algoritmo minimax segue todo o caminho até o nó inicial da árvore que é o tabuleiro inicial e, em seguida, retrocede a árvore conforme a recursão.

### Complexidade do algoritmo Minimax:
- **Complexidade de tempo**: uma vez que executamos uma busca em profundidade (DFS) para a árvore do jogo, a complexidade é **O(b<sup>m</sup>)**.
- **Complexidade do espaço**: é **O(bm)**.
- Em ambos os casos, **b** é o fator de ramificação da árvore do jogo, ou seja, os movimentos possíveis para cada jogada e **m** é a profundidade máxima da árvore.

Adicionalmente, o Minimax parte de uma Busca em Profundidade, para jogos mais complexos como o Xadrez, é comum definirmos uma profundidade máxima para a árvore de possibilidades do jogo.

Muitos jogos utilizam esta técnica para a escolha da dificuldade, apenas variando este parâmetro.

## Feedback

Se você tiver algum feedback, entre em contato comigo pelo email [kevinkirstenlucas@gmail.com](mailto:kevinkirstenlucas@gmail.com?subject=[GitHub]%20python-tictactoe-with-minimax).

## License

[MIT](https://choosealicense.com/licenses/mit/)
