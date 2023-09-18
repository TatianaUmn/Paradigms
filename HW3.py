# Задача Написать игру в “Крестики-нолики”. 
# Использованы  императивную и  процедурную парадигмы


def print_board(board):
    print("Игровое поле:")
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("---------")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("---------")
    print(f"{board[6]} | {board[7]} | {board[8]}")

def check_winner(board):            # Проверка выигрышных комбинаций
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Горизонтальные
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Вертикальные
        [0, 4, 8], [2, 4, 6]              # Диагонали
    ]
    for combination in winning_combinations:
        if board[combination[0]] == board[combination[1]] == board[combination[2]] != ' ':
            return True
    return False

def make_move(board, cell_num, marker):
    if board[cell_num] == ' ':
        board[cell_num] = marker
    else:
        print("Выбранная клетка уже занята. Попробуйте снова.")
        return False
    return True

def play():
    board = [' '] * 9
    print("Добро пожаловать в игру 'Крестики-нолики'!")
    print_board(list(range(1, 10)))  # Выводим начальное игровое поле с номерами клеток
    player = 'X'
    while True:
        cell_num = int(input(f"Ход игрока {player}. Введите номер клетки (1-9): ")) - 1
        if not make_move(board, cell_num, player):
            continue
        print_board(board)
        if check_winner(board):
            print(f"Игрок {player} победил!")
            break
        elif ' ' not in board:
            print("Ничья!")
            break
        player = 'O' if player == 'X' else 'X'

play()