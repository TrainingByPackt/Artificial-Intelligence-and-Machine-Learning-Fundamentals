# The first 73 lines contain the code of Activity 02
# Lines 74 - 109 contain the code of Activity 03
# Lines 110 - 130 contain the code of Activity 04
# The code for this activity starts on Line 124


from random import choice

combo_indices = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

EMPTY_SIGN = '.'
AI_SIGN = 'X'
OPPONENT_SIGN = 'O'


def print_board(board):
    print(" ")
    print(' '.join(board[:3]))
    print(' '.join(board[3:6]))
    print(' '.join(board[6:]))
    print(" ")


def opponent_move(board, row, column):
    index = 3 * (row - 1) + (column - 1)
    if board[index] == EMPTY_SIGN:
        return board[:index] + OPPONENT_SIGN + board[index+1:]
    return board

# Replaced in Activity-04
# def all_moves_from_board(board, sign):
#     move_list = []
#     for i, v in enumerate(board):
#         if v == EMPTY_SIGN:
#             move_list.append(board[:i] + sign + board[i+1:])
#     return move_list
#
# def ai_move(board):
#     return choice(all_moves_from_board(board, AI_SIGN))


def game_won_by(board):
    for index in combo_indices:
        if board[index[0]] == board[index[1]] == board[index[2]] != EMPTY_SIGN:
            return board[index[0]]
    return EMPTY_SIGN


def game_loop():
    board = EMPTY_SIGN * 9
    empty_cell_count = 9
    is_game_ended = False
    while empty_cell_count > 0 and not is_game_ended:
        if empty_cell_count % 2 == 1:
            board = ai_move(board)
        else:
            row = int(input('Enter row: '))
            col = int(input('Enter column: '))
            board = opponent_move(board, row, col)
        print_board(board)
        is_game_ended = game_won_by(board) != EMPTY_SIGN
        empty_cell_count = sum(1 for cell in board if cell == EMPTY_SIGN)
    print('Game has been ended.')

# ----------Activity 03---------------


def all_moves_from_board_list(board_list, sign):
    move_list = []
    for board in board_list:
        move_list.extend(all_moves_from_board(board, sign))
    return move_list


def filter_wins(move_list, ai_wins, opponent_wins):
    for board in move_list:
        won_by = game_won_by(board)
        if won_by == AI_SIGN:
            ai_wins.append(board)
            move_list.remove(board)
        elif won_by == OPPONENT_SIGN:
            opponent_wins.append(board)
            move_list.remove(board)


def count_possibilities():
    board = EMPTY_SIGN * 9
    move_list = [board]
    ai_wins = []
    opponent_wins = []
    for i in range(9):
        print('step ' + str(i) + '. Moves: ' + str(len(move_list)))
        sign = AI_SIGN if i % 2 == 0 else OPPONENT_SIGN
        move_list = all_moves_from_board_list(move_list, sign)
        filter_wins(move_list, ai_wins, opponent_wins)
    print('First player wins: ' + str(len(ai_wins)))
    print('Second player wins: ' + str(len(opponent_wins)))
    print('Draw', str(len(move_list)))
    print('Total', str(len(ai_wins) + len(opponent_wins) + len(move_list)))

# ----------Activity 04---------------

# Overridden in Activity 05
# def ai_move(board):
#     new_boards = all_moves_from_board(board, AI_SIGN)
#     for new_board in new_boards:
#         if game_won_by(new_board) == AI_SIGN:
#             return new_board
#     return choice(new_boards)


# def all_moves_from_board(board, sign):
#     move_list = []
#     for i, v in enumerate(board):
#         if v == EMPTY_SIGN:
#             new_board = board[:i] + sign + board[i+1:]
#             move_list.append(new_board)
#             if game_won_by(new_board) == AI_SIGN:
#                 return [new_board]
#     return move_list

# ----------Activity 05---------------


def player_can_win(board, sign):
    next_moves = all_moves_from_board(board, sign)
    for next_move in next_moves:
        if game_won_by(next_move) == sign:
            return True
    return False


def ai_move(board):
    new_boards = all_moves_from_board(board, AI_SIGN)
    for new_board in new_boards:
        if game_won_by(new_board) == AI_SIGN:
            return new_board
    safe_moves = []
    for new_board in new_boards:
        if not player_can_win(new_board, OPPONENT_SIGN):
            safe_moves.append(new_board)
    return choice(safe_moves) if len(safe_moves) > 0 else new_boards[0]


def all_moves_from_board(board, sign):
    move_list = []
    for i, v in enumerate(board):
        if v == EMPTY_SIGN:
            new_board = board[:i] + sign + board[i+1:]
            move_list.append(new_board)
            if game_won_by(new_board) == AI_SIGN:
                return [new_board]
    if sign == AI_SIGN:
        safe_moves = []
        for move in move_list:
            if not player_can_win(move, OPPONENT_SIGN):
                safe_moves.append(move)
        return safe_moves if len(safe_moves) > 0 else move_list[0:1]
    else:
        return move_list
