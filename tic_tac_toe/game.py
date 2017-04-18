# -*- coding: utf-8 -*-
# internal helpers

from .exceptions import InvalidMovement, GameOver


def _position_is_empty_in_board(position, board):
    """
    Checks if given position is empty ("-") in the board.

    :param position: Two-elements tuple representing a
                     position in the board. Example: (0, 1)
    :param board: Game board.

    Returns True if given position is empty, False otherwise.
    """
    row,col = position
    return board[row][col] == "-"


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
    row,col = position
    if type(position) != tuple:
        return False
    if len(position) != 2:
        return False
    if row or col >= 3 or row or col <0:
        return False
    return True
    
    
def _board_is_full(board):
    """
    Returns True if all positions in given board are occupied.

    :param board: Game board.
    """
    full = True
    for row in board:
        for col in row:
            if col == '-':
                full = False
    return full
    
    
def _is_winning_combination(board, combination, player):
    """
    Checks if all 3 positions in given combination are occupied by given player.

    :param board: Game board.
    :param combination: Tuple containing three position elements.
                        Example: ((0,0), (0,1), (0,2))

    Returns True of all three positions in the combination belongs to given
    player, False otherwise.
    """
    for pos in combination:
        if board[pos[0]][pos[1]] != player:
            return False
    return True
 
   
def _check_winning_combinations(board, player):
    """
    There are 8 posible combinations (3 horizontals, 3, verticals and 2 diagonals)
    to win the Tic-tac-toe game.
    This helper loops through all these combinations and checks if any of them
    belongs to the given player.

    :param board: Game board.
    :param player: One of the two playing players.

    Returns the player (winner) if any of the winning combinations is completed
    by given player, or None otherwise.
    """
    combos = {
        'horizontal_top': ((0,0), (0,1), (0,2)), 
        'horizontal_middle': ((1,0), (1,1), (1,2)), 
        'horizontal_bottom': ((2,0), (2,1), (2,2)), 
        'vertical_left': ((0,0), (1,1), (2,0)), 
        'vertical_middle': ((0,1), (1,1), (2,1)), 
        'vertical_right': ((0,2), (1,1), (2,2)), 
        'diagonal_1': ((0,0), (1,1), (2,2)), 
        'diagonal_2': ((2,0), (1,1), (0,2))  
    }
    
    for pattern,combination in combos.items():
        if _is_winning_combination(board, combination ,player):
            return player
    return None


# public interface
def start_new_game(player1, player2):
    
    return {
        'player1': player1,
        'player2': player2,
        'board': [
            ["-", "-", "-"],
            ["-", "-", "-"],
            ["-", "-", "-"],
        ],
        'next_turn': "X",
        'winner': None
    }
    
    
def get_winner(game):
    """
    Returns the winner player if any, or None otherwise.
    """
    

def move(game, player, position):
    """
    Performs a player movement in the game. Must ensure all the pre requisites
    checks before the actual movement is done.
    After registering the movement it must check if the game is over.
    """
    past_player=player
    board = game['board']
    
    if game["next_turn"] != player:
        raise InvalidMovement("{} moves next".format(game["next_turn"]))
        
    if not _position_is_empty_in_board(position,board):
        raise InvalidMovement("Position already taken.")
    
    if not _position_is_valid(position):
        raise InvalidMovement("Position out of range.")
      
    board[position[0]][position[1]] = player

    #check for winning conditions
    _check_winning_combinations(board, player)


def get_board_as_string(game):
    """
    Returns a string representation of the game board in the current state.
    """
    
    return """
{}  |  {}  |  {}
--------------
{}  |  {}  |  {}
--------------
{}  |  {}  |  {}
""".format(
game['board'][0][0], game['board'][0][1], game['board'][0][2], 
game['board'][1][0], game['board'][1][1], game['board'][1][2], 
game['board'][2][0], game['board'][2][1], game['board'][2][2])


def get_next_turn(game):
    """
    Returns the player who plays next, or None if the game is already over.
    """
    pass