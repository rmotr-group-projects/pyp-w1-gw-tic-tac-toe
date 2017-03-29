#import exceptions
from .exceptions import GameOver, InvalidMovement


# internal helpers
def _position_is_empty_in_board(position, board):
    """
    Checks if given position is empty ("-") in the board.

    :param position: Two-elements tuple representing a
                     position in the board. Example: (0, 1)
    :param board: Game board.

    Returns True if given position is empty, False otherwise.
    """
    if board[position[0]][position[1]] == "-":
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
    if not isinstance(position, tuple):
        return False
    elif len(position) != 2:
        return False
    elif position[0] not in (0,1,2):
        return False
    elif position[1] not in (0,1,2):
        return False
    return True
        


def _board_is_full(board):
    """
    Returns True if all positions in given board are occupied.

    :param board: Game board.
    """
    for position1 in (0,1,2):
        for position2 in (0,1,2):
            if _position_is_empty_in_board((position1, position2), board):
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
    for position in combination:
        if board[position[0]][position[1]] != player:
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

    Returns the player (winner) of any of the winning combinations is completed
    by given player, or None otherwise.
    
    board, for reference:
    (0,0) | (0,1) | (0,2)
    ---------------------
    (1,0) | (1,1) | (1,2)
    ---------------------
    (2,0) | (2,1) | (2,2)
    """
    
    combinations = (
        #vertical
        ((0,0), (1,0), (2,0)),
        ((0,1), (1,1), (2,1)),
        ((0,2), (1,2), (2,2)),
        
        #horizontal
        ((0,0), (0,1), (0,2)),
        ((1,0), (1,1), (1,2)),
        ((2,0), (2,1), (2,2)),
        
        #diagonal
        ((0,0), (1,1), (2,2)),
        ((0,2), (1,1), (2,0)),
        )
    
    for combination in combinations:
        if _is_winning_combination(board,combination, player):
            return player
    return None


# public interface
def start_new_game(player1, player2):
    """
    Creates and returns a new game configuration.
    """
    return {
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
    #create board object
    board = game['board']
    #check illegal moves
    if game['winner'] or _board_is_full(board):
        raise InvalidMovement('Game is over.')
    if player != game['next_turn']:
        raise InvalidMovement('"{}" moves next.'.format(game['next_turn']))
    if not _position_is_valid(position):
        raise InvalidMovement('Position out of range.')
    if not _position_is_empty_in_board(position, board):
        raise InvalidMovement('Position already taken.')
    #make actual move
    board[position[0]][position[1]] = player
    #set winner
    winner = _check_winning_combinations(board, player)
    #explore options if a winner exists
    if winner:
        game['winner'] = winner
        game['next_turn'] = None
        raise GameOver('"{}" wins!'.format(winner))
    elif _board_is_full(board):
        game['next_turn'] = None
        raise GameOver('Game is tied!'.format(winner))
    else:
        game['next_turn'] = game['player1'] if game['next_turn'] == game['player2'] else game['player2']
    


def get_board_as_string(game):
    """
    Returns a string representation of the game board in the current state.
    """
    
    board_string = """
{}  |  {}  |  {}
--------------
{}  |  {}  |  {}
--------------
{}  |  {}  |  {}
"""
    
    current_board = game['board']
    
    #close, still error
    return board_string.format(current_board[0][0],current_board[0][1],current_board[0][2],current_board[1][0],current_board[1][1],current_board[1][2],current_board[2][0],current_board[2][1],current_board[2][2])
    
    #for line in game['board']:
     #   board_string += "  |  ".join(line) + "\n" + "--------------"
    #return board_string


def get_next_turn(game):
    """
    Returns the player who plays next, or None if the game is already over.
    """
    return game['next_turn']

