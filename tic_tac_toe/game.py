from .exceptions import *

# internal helpers
def _position_is_empty_in_board(position, board):
    """
    Checks if given position is empty ("-") in the board.

    :param position: Two-elements tuple representing a
                     position in the board. Example: (0, 1)
    :param board: Game board.

    Returns True if given position is empty, False otherwise.
    """
    return board[position[0]][position[1]] is '-'


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
    return isinstance(position, tuple)              and \
           len(position) is 2                       and \
           (0, 0) <= (position[0], position[1]) <= (2, 2)

def _board_is_full(board):
    """
    Returns True if all positions in given board are occupied.

    :param board: Game board.
    """
    return all(all(col is not '-' for col in row) for row in board)


def _is_winning_combination(board, combination, player):
    """
    Checks if all 3 positions in given combination are occupied by given player.

    :param board: Game board.
    :param combination: Tuple containing three position elements.
                        Example: ((0,0), (0,1), (0,2))

    Returns True of all three positions in the combination belongs to given
    player, False otherwise.
    """
    return all(board[pos[0]][pos[1]] is player for pos in combination)


def _check_winning_combinations(board, player):
    """
    There are 8 posible combinations (3 horizontals, 3, verticals and 2 diagonals)
    to win the Tic-tac-toe game.
    This helper loops through all these combinations and checks if any of them
    belongs to the given player.

    :param board: Game board.
    :param player: One of the two playing players.

    Returns the player (winner) of any of the winning combinations is completed
    by given player, or None otherwise.
    """
    horizontals = [ tuple((row, col)                for col in range(3)) for row     in range(3) ]
    verticals   = [ tuple((row, col)                for row in range(3)) for col     in range(3) ]
    diagonals   = [ tuple((row, abs(row - col_aux)) for row in range(3)) for col_aux in [0,2]    ]
    
    winning_combs = horizontals + verticals + diagonals
    
    if any(_is_winning_combination(board, comb, player) for comb in winning_combs):
        return player
    return None

# public interface
def start_new_game(player1, player2):
    """
    Creates and returns a new game configuration.
    """
    return { 'player1': player1, 'player2': player2,
             'board': [ ['-', '-', '-'] for _ in range(3) ],
             'next_turn': player1, 'winner': None }

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
    if game['winner'] or _board_is_full(game['board']):
        raise InvalidMovement('Game is over.')
    if not _position_is_valid(position):
        raise InvalidMovement('Position out of range.')
    if not _position_is_empty_in_board(position, game['board']):
        raise InvalidMovement('Position already taken.')
    if player is not get_next_turn(game):
        raise InvalidMovement('"{0}" moves next'.format(get_next_turn(game)))
    
    game['board'][position[0]][position[1]] = player
    game['next_turn'] = game['player2'] if player is game['player1'] else game['player1']
    
    winner = _check_winning_combinations(game['board'], player)
    if winner:
        game['winner'] = winner
        raise GameOver('"{0}" wins!'.format(winner))
    if _board_is_full(game['board']):
        raise GameOver('Game is tied!')

def get_board_as_string(game):
    """
    Returns a string representation of the game board in the current state.
    """
    
    board = game["board"]
    board_string = '\n'
    
    for y_index, inner_list in enumerate(board):
        for x_index, position in enumerate(inner_list):
            if y_index < len(board):
                if x_index is 0:
                    board_string += (position + "  | ")
                elif x_index is 1:
                    board_string += (" " + position + "  | ")
                elif x_index is 2:
                    board_string += (" " + position)
                    
                if x_index == (len(inner_list) - 1) and y_index < (len(board) - 1):
                    board_string += '\n--------------\n'
    return board_string + '\n'


def get_next_turn(game):
    """
    Returns the player who plays next, or None if the game is already over.
    """
    return game['next_turn']
