# internal helpers
from exceptions import *

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
    
    if not isinstance(position, tuple) or not len(position) == 2:
        return False
    
    if position[0] > 2 or position[0] < 0 or position[1] > 2 or position[1] < 0:
        return False
        
    return True


def _board_is_full(board):
    """
    Returns True if all positions in given board are occupied.

    :param board: Game board.
    """
    
    
    # return all([[item != '-' for item in line] for line in board]])
    return all([space != '-' for item in board for space in item])

def _is_winning_combination(board, combination, player):
    """
    Checks if all 3 positions in given combination are occupied by given player.

    :param board: Game board.
    :param combination: Tuple containing three position elements.
                        Example: ((0,0), (0,1), (0,2))

    Returns True of all three positions in the combination belongs to given
    player, False otherwise.
    """
    
    for comb_pos1,comb_pos2 in combination:
        if board[comb_pos1][comb_pos2] != player:
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
    """
    
    zeros = [0,0,0]
    ones = [1,1,1]
    twos = [2,2,2]
    ran3 = [0,1,2]
    
    comb = [[(0,0),(1,1),(2,2)],[(0,2),(1,1),(2,0)]]
    for row in [zeros,ones,twos]:
        temp_list = []
        for item in zip(row,ran3):
            temp_list.append(item)
        comb.append(temp_list) 
    for col in [zeros, ones, twos]:
        temp_list = []
        for item in zip(ran3,col):
            temp_list.append(item)
        comb.append(temp_list)
        
    
    for combination in comb:
        if _is_winning_combination(board,combination,player):
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
        'next_turn' : player1,
        'winner' : None
    }

    return game

def get_winner(game):
    """
    Returns the winner player if any, or None otherwise.
    """ 
    if _check_winning_combinations(game['board'], game['player1']):
        game['winner'] = player1
        return player1
    elif _check_winning_combinations(game['board'], game['player2']):
        game['winner'] = player2
        return player2
    else:
        return None


def move(game, player, position):
    """
    Performs a player movement in the game. Must ensure all the pre requisites
    checks before the actual movement is done.
    After registering the movement it must check if the game is over.
    """
    if _board_is_full(game['board']) or game['winner']:
            raise InvalidMovement('Game is over.')
        # elif not game['winner']:
            # raise GameOver('Game is tied!')
    elif game['next_turn'] != player:
        raise InvalidMovement('"{}" moves next.'.format(game['next_turn']))
    elif not _position_is_empty_in_board(position, game['board']):
        raise InvalidMovement('Position already taken.')
    elif not _position_is_valid(position):
        raise InvalidMovement('Position out of range.')
    
    game['board'][position[0]][position[1]] = player
    if game['next_turn'] == game['player1']:
        game['next_turn'] = game['player2']
    else:
        game['next_turn'] = game['player1']
        

    if _check_winning_combinations(game['board'], player):
        game['winner'] = player
        raise GameOver()
    elif _board_is_full(game['board']):
        raise GameOver("Game is tied!")


def get_board_as_string(game):
    """
    Returns a string representation of the game board in the current state.
    """
    # a = game['board'][0][0]
    # b = game['board'][0][1]
    # c = game['board'][0][2]
    # d = game['board'][1][0]
    # e = game['board'][1][1]
    # f = game['board'][1][2]
    # g = game['board'][2][0]
    

    board = game['board']
    
    return """
{0}  |  {1}  |  {2}
--------------
{3}  |  {4}  |  {5}
--------------
{6}  |  {7}  |  {8}
""".format(*(board[0] + board[1] + board[2]))



def get_next_turn(game):
    """
    Returns the player who plays next, or None if the game is already over.
    """
    return game['next_turn']