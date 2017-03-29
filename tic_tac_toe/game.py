from .exceptions import *
from itertools import chain

# internal helpers
def _position_is_empty_in_board(position, board):
    """
    Checks if given position is empty ("-") in the board.

    :param position: Two-elements tuple representing a
                     position in the board. Example: (0, 1)
    :param board: Game board.

    Returns True if given position is empty, False otherwise.
    """
    return board[position[0]][position[1]] == "-"
    

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
    valid_positions = [
        (0,0), (0,1), (0,2),
        (1,0), (1,1), (1,2),
        (2,0), (2,1), (2,2),
    ]
    
    return position in valid_positions


def _board_is_full(board):
    """
    Returns True if all positions in given board are occupied.

    :param board: Game board.
    """
    for position in board:
        if '-' in position:
            return False
    return True


def _is_winning_combination(board, combination, player):
    """
    Checks if all 3 positions in given combination are occupied by given player.

    :param board: Game board.
    :param combination: Tuple containing three position elements.
                        Example: ((0,0), (0,1), (0,2))

    Returns True of all three positions in the combination belongs to given
    player, False otherwise.
    """

    return all(board[row][col] == player for row,col in combination)


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
    for row in range(3):
        if _is_winning_combination(board,((row,col) for col in range(3)),player):
            return player
    for col in range(3):
        if _is_winning_combination(board,((row,col) for row in range(3)),player):
            return player
    if _is_winning_combination(board,((diag,diag) for diag in range(3)), player):
        return player #0,0 1,1 2,2
    if _is_winning_combination(board,((diag,2-diag) for diag in range(3)), player):
        return player #0,2 1,1 2,0
    return None


# public interface
def start_new_game(player1, player2):
    """
    Creates and returns a new game configuration.
    """
    board = {
        'player1': player1,
        'player2': player2,
        'board': [
            ["-", "-", "-"],
            ["-", "-", "-"],
            ["-", "-", "-"],
        ],
        'next_turn': player1,
        'winner': None
    }
    return board


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
    #full board
    if _board_is_full(game['board']) or game['winner']:
        raise InvalidMovement('Game is over.')
    #next player is valid
    if game['next_turn'] != player:
        raise InvalidMovement('"{}" moves next'.format(game['next_turn']))
    #position isn't valid
    if not _position_is_valid(position):
        raise InvalidMovement("Position out of range.")
    #position is empty
    if not _position_is_empty_in_board(position, game["board"]):
        raise InvalidMovement("Position already taken.")
    
    
    #making the move
    row,col = position #(0,1) row = 0, col = 1
    game['board'][row][col] = player
    
    #update next player
    player1 = game['player1']
    player2 = game['player2']
    game['next_turn'] = player1 if player == player2 else player2
    
    #check winner combination and update if there is a winner
    if _check_winning_combinations(game["board"], player):
        game['winner'] = player
        raise GameOver('"{}" wins!'.format(player))
    
    #no winner game is tied if board full
    if _board_is_full(game['board']):
        raise GameOver('Game is tied!')
    


def get_board_as_string(game):
    """
    Returns a string representation of the game board in the current state.
    """
    format_board = """
{}  |  {}  |  {}
--------------
{}  |  {}  |  {}
--------------
{}  |  {}  |  {}
"""
    
    return format_board.format(*chain.from_iterable(game["board"]))



def get_next_turn(game):
    """
    Returns the player who plays next, or None if the game is already over.
    """
    return game['next_turn']
