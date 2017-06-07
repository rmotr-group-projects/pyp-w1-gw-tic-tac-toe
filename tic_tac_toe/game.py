from __future__ import print_function
from itertools import product
from pprint import pprint

try:
    from tic_tac_toe.exceptions import *
except ImportError:
    from exceptions import *


def check_axis(data, n):
    """Returns any values occurring n number of times"""

    return len([x for x in data if data.count(x) == n])

def generate_grid():
    """Returns 3x3 grid coordinates as a tuple of tuples"""

    return ((row, col) for row, col in product(range(3), range(3)))


def _position_is_empty_in_board(position, board):
    """
    Checks if given position is empty ("-") in the board.

    :param position: Two-elements tuple representing a
                     position in the board. Example: (0, 1)
    :param board: Game board.

    Returns True if given position is empty, False otherwise.
    """

    row, col = position
    if board[row][col] == '-':
        return True
    return False


def _position_is_valid(position):
    """
    Checks if given position is a valid. To consider a position as valid, it
    must be a two-elements tuple, containing values from 0 to 2.
    Examples of valid positions: (0,0), (1,0)
    Examples of invalid positions: (0,0,1), (9,8), False

    :param position: Two-elements tuple representing a
                     position in the board. Example: (0, 1)

    Returns True if given position is valid, False otherwise.
    """
    if position not in generate_grid():
        return False
    return True


def _board_is_full(board):
    """
    Returns True if all positions in given board are occupied.

    :param board: Game board.
    """
    grid = generate_grid()
    if any(((row, col) in grid for row, col in grid if board[row][col] == '-')):
        return False

    return True

def _check_winning_combinations(board, player):
    """
     Returns the player (winner) of any of the winning combinations is completed
     by given player, or None otherwise.

     :param board: Game board.
     :param player: One of the two playing players.

     """

    grid = generate_grid()
    row, col = zip(*((row, col) for row, col in grid if board[row][col] == player))

    if check_axis(row, 3) != 0 or check_axis(col, 3) != 0:
        # horizontal /vertical moves
        return player

    if (1, 1) in zip(row, col):
        # Diagonal moves
        if ((0, 0) and (2, 2)) or ((2, 0) and (0, 2)) in zip(row, col):
            return player

    return False

def start_new_game(player1, player2):
    """
    Creates and returns a new game configuration.
    """

    board = [['-' for i in range(3)] for i in range(3)]

    return {
            'player1': player1,
            'player2': player2,
            'board': board,
            'next_turn': player1,
            'winner': None
            }


def get_winner(game):
    """
    Returns the winner player if any, or None otherwise.
    """
    return game['winner']


def move(game, player, position):
    """
    Performs a player movement in the game. Must ensure all the pre requisites
    checks before the actual movement is done.
    After registering the movement it must check if the game is over.
    """
    if not _position_is_valid(position):
        raise InvalidMovement('Position out of range.')
    if not _position_is_empty_in_board(position, game['board']):
        raise InvalidMovement('Position already taken.')

    if game['next_turn'] != player:
        raise InvalidMovement('"{}" moves next'.format(game['next_turn']))


    row, col = position
    game['board'][row][col] = player

    if not _check_winning_combinations(game['board'], player):
        get_next_turn(game)

def get_board_as_string(game):
    """
    Returns a string representation of the game board in the current state.
    """

    str_board = '\n'
    for row_dex, row in enumerate(game['board']):
        for col_dex, col in enumerate(row):
            if col_dex == 1:
                str_board += '  |  {}  |  '.format(col)
            else:
                str_board += str(col)
        if row_dex != 2:
            str_board += '\n--------------\n'
    str_board += '\n'

    return str_board


def get_next_turn(game):
    """
    Returns the player who plays next, or None if the game is already over.
    """

    if not game['winner']:
        if game['next_turn'] == game['player1']:
            game['next_turn'] = game['player2']
        else:
            game['next_turn'] = game['player1']


if __name__ == '__main__':
    player1 = 'X'
    player2 = 'O'

    a_game = start_new_game(player1, player2)
    move(a_game, player1, (0,0))
    pprint(a_game)
    move(a_game, player1, (1,0))


