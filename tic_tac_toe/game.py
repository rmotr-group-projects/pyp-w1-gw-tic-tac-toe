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
    
    return position in [(x, y) for x in range (0,3) for y in range(0,3)]



def _board_is_full(board):
    """
    Returns True if all positions in given board are occupied.

    :param board: Game board
    """
    return "-" not in [item for x in board for item in x]


def _is_winning_combination(board, combination, player):
    """
    Checks if all 3 positions in given combination are occupied by given player.

    :param board: Game board.
    :param combination: Tuple containing three position elements.
                        Example: ((0,0), (0,1), (0,2))

    Returns True of all three positions in the combination belongs to given
    player, False otherwise.
    """
    #for x in combination:
   #     if board[x[0]][x[1]] != player:
    #        return False
    #return True
    return all([board[x[0]][x[1]] == player for x in combination])
    
    
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
    l = [
    ((0, x) for x in range(3)),
    ((1, x) for x in range(3)),
    ((2, x) for x in range(3)),
    ((x, 0) for x in range(3)),
    ((x, 1) for x in range(3)),
    ((x, 2) for x in range(3)),
    ((x, x) for x in range(3)),
    ((0,2),(1,1),(2,0))
    ]
    for x in l:
        if _is_winning_combination(board,tuple(x),player):
            return player
    return None


# public interface
def start_new_game(player1, player2):
    """
    Creates and returns a new game configuration.
    """
    game = {
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
    return game

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
    if get_next_turn(game) == None:
        raise InvalidMovement('Game is over.')
    if get_next_turn(game) != player:
        raise InvalidMovement("\"{}\" moves next".format(game['next_turn']))
    if not _position_is_valid(position):
        raise InvalidMovement("Position out of range.")
    if not _position_is_empty_in_board(position, game['board']):
        raise InvalidMovement("Position already taken.")
    
    game['board'][position[0]][position[1]] = player
    if _check_winning_combinations(game['board'],player):
        game['winner'] = player
        game['next_turn'] = None
        raise GameOver('\"{}\" wins!'.format(player)) 
    elif _board_is_full(game['board']):
        game['winner'] = None
        game['next_turn'] = None
        raise GameOver('Game is tied!')
    else:
        game['winner'] = None
        if player == game['player1']:
            game['next_turn'] = game['player2']
        else:
            game['next_turn'] = game['player1']
        return
    


def get_board_as_string(game):
    """
    Returns a string representation of the game board in the current state.
    """
    
    #return str(game['board'])
    return "\n{}  |  {}  |  {}\n--------------\n{}  |  {}  |  {}\n--------------\n{}  |  {}  |  {}\n".format(game['board'][0][0], game['board'][0][1],
            game['board'][0][2], game['board'][1][0], game['board'][1][1],
            game['board'][1][2], game['board'][2][0], game['board'][2][1],
            game['board'][2][2])


def get_next_turn(game):
    """
    Returns the player who plays next, or None if the game is already over.
    """
    return game['next_turn']
