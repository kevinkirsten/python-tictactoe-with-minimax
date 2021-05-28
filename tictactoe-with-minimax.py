import time


class Player:
    players = []

    def __init__(self, name='', letter=''):
        self.name = name
        self.letter = letter
        Player.players.append(self)


def create_board():
    board = {
        1: ' ', 2: ' ', 3: ' ',
        4: ' ', 5: ' ', 6: ' ',
        7: ' ', 8: ' ', 9: ' '
    }
    return board


def print_board(board):
    print(' ' + board[1] + ' │ ' + board[2] + ' │ ' + board[3] + ' ')
    print('───┼───┼───')
    print(' ' + board[4] + ' │ ' + board[5] + ' │ ' + board[6] + ' ')
    print('───┼───┼───')
    print(' ' + board[7] + ' │ ' + board[8] + ' │ ' + board[9] + ' ')
    print('')


def space_is_empty(board, position):
    if board[position] == ' ':
        return True
    else:
        return False


def find_computer_obj():
    for player in Player.players:
        if player.name == 'computer':
            return player


def find_human_obj():
    for player in Player.players:
        if player.name == 'human':
            return player


def play_again():
    print('')
    option = input('Deseja jogar novamente? Digite "s" para Sim ou qualquer tecla para encerrar: ')
    if option == 's' or option == 'S':
        print('')
        main()
    else:
        exit()


def delay():
    time.sleep(0.5)


def insert_letter(board, letter, position):
    delay()
    if space_is_empty(board, position):
        board[position] = letter
        print('')
        print_board(board)

        if check_tie(board):
            print('Empate!')
            play_again()
        elif victory(board):
            if letter == find_computer_obj().letter:
                print('O computador ganhou!')
            elif letter == find_human_obj().letter:
                print('Você ganhou!')
            play_again()
        return

    else:
        print('A posição escolhida está ocupada!')
        delay()
        position = int(input('Escolha uma nova posição: '))
        insert_letter(board, letter, position)
        return


def check_rows_win(board, letter=None):
    if letter is None:
        if board[1] == board[2] and board[1] == board[3] and board[1] != ' ':
            return True
        elif board[4] == board[5] and board[4] == board[6] and board[4] != ' ':
            return True
        elif board[7] == board[8] and board[7] == board[9] and board[7] != ' ':
            return True
        else:
            return False
    else:
        if board[1] == board[2] and board[1] == board[3] and board[1] == letter:
            return True
        elif board[4] == board[5] and board[4] == board[6] and board[4] == letter:
            return True
        elif board[7] == board[8] and board[7] == board[9] and board[7] == letter:
            return True
        else:
            return False


def check_columns_win(board, letter=None):
    if letter is None:
        if board[1] == board[4] and board[1] == board[7] and board[1] != ' ':
            return True
        elif board[2] == board[5] and board[2] == board[8] and board[2] != ' ':
            return True
        elif board[3] == board[6] and board[3] == board[9] and board[3] != ' ':
            return True
        else:
            return False
    else:
        if board[1] == board[4] and board[1] == board[7] and board[1] == letter:
            return True
        elif board[2] == board[5] and board[2] == board[8] and board[2] == letter:
            return True
        elif board[3] == board[6] and board[3] == board[9] and board[3] == letter:
            return True
        else:
            return False


def check_diagonal_win(board, letter=None):
    if letter is None:
        if board[1] == board[5] and board[1] == board[9] and board[1] != ' ':
            return True
        elif board[7] == board[5] and board[7] == board[3] and board[7] != ' ':
            return True
        else:
            return False
    else:
        if board[1] == board[5] and board[1] == board[9] and board[1] == letter:
            return True
        elif board[7] == board[5] and board[7] == board[3] and board[7] == letter:
            return True
        else:
            return False


def victory(board):
    if check_rows_win(board):
        return True
    elif check_columns_win(board):
        return True
    elif check_diagonal_win(board):
        return True
    else:
        return False


def player_won(board, player):
    if check_rows_win(board, player):
        return True
    elif check_columns_win(board, player):
        return True
    elif check_diagonal_win(board, player):
        return True
    else:
        return False


def check_tie(board):
    for key in board.keys():
        if board[key] == ' ':
            return False

    return True


def human_movement(board, human):
    position = int(input('Digite a posição para sua jogada "' + human.letter + '": '))
    insert_letter(board, human.letter, position)
    return


def computer_movement(board, computer):
    best_score = -800
    best_move = 0

    for key in board.keys():
        if board[key] == ' ':
            board[key] = computer.letter
            score = minimax(board, 0, False)
            board[key] = ' '
            if score > best_score:
                best_score = score
                best_move = key
    print('Jogada do computador:', best_move)
    insert_letter(board, computer.letter, best_move)
    return


def minimax(board, depth, is_maximizing):
    computer = find_computer_obj()
    human = find_human_obj()

    if player_won(board, computer.letter):
        return 1
    elif player_won(board, human.letter):
        return -1
    elif check_tie(board):
        return 0

    if is_maximizing:
        best_score = -800
        for key in board.keys():
            if board[key] == ' ':
                board[key] = computer.letter
                score = minimax(board, depth + 1, False)  # Next move should minimize
                board[key] = ' '
                if score > best_score:
                    best_score = score
        return best_score

    else:
        best_score = 800
        for key in board.keys():
            if board[key] == ' ':
                board[key] = human.letter
                score = minimax(board, depth + 1, True)  # Next move should maximize
                board[key] = ' '
                if score < best_score:
                    best_score = score
        return best_score


def define_first_player():
    """
    if human goes first -> return True
    if computer goes first -> return False
    """
    delay()
    option = int(input('Digite 1 para jogar primeiro, ou 0 para o computador iniciar: '))
    if option == 1:
        print('Você é o primeiro a jogar! Boa Sorte!')
        return True
    elif option == 0:
        print('O Computador joga primeiro! Boa Sorte!')
        return False
    else:
        print('Digite uma opção válida!')
        define_first_player()


def create_players(config):
    human = Player('human', 'X')
    computer = Player('computer', '0')

    if config == 0:
        human.letter = 'O'
        computer.letter = 'X'

    return human, computer


def main():
    print('##################################################')
    print('#                 Jogo da Velha                  #')
    print('##################################################')
    print('Na sua rodada, digite o número referente a posição')
    print('que você deseja jogar, seguindo o mapa abaixo:')
    print('')
    delay()
    print(' 1 │ 2 │ 3 ')
    print('───┼───┼───')
    print(' 4 │ 5 │ 6 ')
    print('───┼───┼───')
    print(' 7 │ 8 │ 9 ')
    print('')

    board = create_board()
    human_goes_first = define_first_player()
    print('')

    if human_goes_first:
        human, computer = create_players(1)
        print_board(board)
        while not victory(board):
            delay()
            human_movement(board, human)
            delay()
            computer_movement(board, computer)

    else:
        human, computer = create_players(0)
        while not victory(board):
            delay()
            computer_movement(board, computer)
            delay()
            human_movement(board, human)


if __name__ == '__main__':
    main()
