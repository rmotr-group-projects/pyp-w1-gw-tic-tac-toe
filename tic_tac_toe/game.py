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
    
    # valid_pos
    
    if isinstance(position, tuple):
        if len(position) == 2:
            if position[0] in (0,1,2) and position[1] in (0,1,2):
                return True
    return False


def _board_is_full(board):
    """
    Returns True if all positions in given board are occupied.

    :param board: Game board.
    """
    
    for row in board:
        if row[0] == "-" or row[1] == "-" or row[2] == "-":
            return False
    return True
    


def _is_winning_combination(board, combination, player):
    for position in combination:
        if board[position[0]][position[1]] != player:
            return False
    return True
    
    """
    Checks if all 3 positions in given combination are occupied by given player.

    :param board: Game board.
    :param combination: Tuple containing three position elements.
                        Example: ((0,0), (0,1), (0,2))

    Returns True of all three positions in the combination belongs to given
    player, False otherwise.
    """
    pass


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
    combinations = \
        (
        ((0,0), (0,1),(0,2)), 
        ((1,0), (1,1),(1,2)), 
        ((2,0), (2,1),(2,2)), 
    
        ((0,0), (1,0),(2,0)),  
        ((0,1), (1,1),(2,1)), 
        ((0,2), (1,2),(2,2)), 
    
        ((0,0), (1,1),(2,2)), 
        ((2,0), (1,1),(0,2)), 
        )
    
    for comb in combinations:
      if _is_winning_combination(board, comb, player): #winning condition
          return player
       
       
        
        
    
pass


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
    
    if _board_is_full(game['board']) or game['winner']:
        raise InvalidMovement('Game is over.')

    
    if not _position_is_valid(position):
        raise InvalidMovement('Position out of range.')
        
    if not _position_is_empty_in_board(position, game['board']):
        raise InvalidMovement('Position already taken.')
        
    if game['next_turn'] != player:
        
        raise InvalidMovement('"{}" moves next.'.format(game['next_turn']))
        
    
    game['board'][position[0]][position[1]] = player
    
    winner = _check_winning_combinations(game['board'], player)
    
    

        
    if winner:
        game['winner'] = winner
        game['next_turn'] = None
        raise GameOver('"{}" wins!'.format(winner))
    elif _board_is_full(game['board']):
        raise GameOver('Game is tied!')
    else:
        if game['next_turn'] == game['player1']:
            game['next_turn'] = game['player2']
        else:
            game['next_turn'] = game['player1']
            

    


def get_board_as_string(game):
    
    bd = game['board']
    
    
    newBoardString = "\n"
    
    newBoardString += bd[0][0]+"  |  " + bd[0][1]+ "  |  " + bd[0][2]
    newBoardString += "\n"
    newBoardString +="--------------\n"
    newBoardString += bd[1][0]+"  |  " + bd[1][1]+ "  |  " + bd[1][2]
    newBoardString += "\n"
    newBoardString +="--------------\n"
    newBoardString += bd[2][0]+"  |  " + bd[2][1]+ "  |  " + bd[2][2] + "\n"
    return newBoardString
    
    
    
    pass


def get_next_turn(game):
    """
    Returns the player who plays next, or None if the game is already over.
    """
    
    if _board_is_full(game['board']) == True or game['winner']:
        return None
    
    return game['next_turn']
    
    pass
