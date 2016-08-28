from .exceptions import InvalidMovement, GameOver

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
    
    if isinstance(position, tuple) and len(position) == 2 and position[0] >= 0 and position[1] >= 0 and position[0] <= 2 and position[1] <= 2:
        return True
    """
    isinstance(position, tuple) # is it a tuple?
    len(position) == 2 # does it have 2 values?
    position[0], position[1] >= 0 # is it greater than or equal to zero?
    position[0], position[1] <= 2 # is it less than or equal to two?
    """

def _board_is_full(board):
    """
    Returns True if all positions in given board are occupied.

    :param board: Game board.
    """
    for line in board:
        for position in line:
            if position != '-':
                return False
                
    return True
    
    #for line in board:
        #for position in line:
            #if position != "-":
                #return False

def _is_winning_combination(board, combination, player):
    """
    Checks if all 3 positions in given combination are occupied by given player.

    :param board: Game board.
    :param combination: Tuple containing three position elements.
                        Example: ((0,0), (0,1), (0,2)) horizontal win
                                 ((0,0), (1,0), (2,0)) vertical win
                                 ((0,0), (1,1), (2,2)) diagonal1
                                 ((0,2), (1,1), (2,0)) diagnoal2

    Returns True of all three positions in the combination belongs to given
    player, False otherwise.
    """
    
    for win in combination:
        if board[win[0]][win[1]] != player:
            return False
    
    return True

    #for position in combination:
        #if board[position[0][1]] != player:
            #return False
        
    #return all(board[position[0][1]]) == player
            
    
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
    # this might help ;-)
    # (0,0) | (0,1) | (0,2)
    # ---------------------
    # (1,0) | (1,1) | (1,2)
    # ---------------------
    # (2,0) | (2,1) | (2,2)
    combinations = (
        # horizontals
        ((0,0), (0,1), (0,2)),    
        ((1,0), (1,1), (1,2)),    
        ((2,0), (2,1), (2,2)),
        #verticals
        ((0,0), (1,0), (2,0)),
        ((0,1), (1,1), (2,1)),
        ((0,2), (1,2), (2,2)),
        #diagonals
        ((0,0), (1,1), (2,2)),
        ((0,2), (1,1), (2,0)),
    )
    
    for win in combinations:
        if _is_winning_combination(board, win, player):
            return player
    
    return None
    
    """
    position1 = combination[0]
    position2 = combination[1]
    position3 = combination[2]
    
    if board[position1][0] == board[position2][0] and board[position3][0]:
        return True
    
    if board[position1][1] == board[position2][1] and board[position3][1]:
        return True
        
    if combination == ((0,0), (1,1), (2,2)) or ((0,2), (1,1), (2,0)):
        return True
    """

# public interface
def start_new_game(player1, player2):
    """
    Creates and returns a new game configuration.
    """
    return {
        'player1' : player1,
        'player2' : player2,
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
    if get_next_turn(game) == None:
        raise GameOver("The Game is Over")
    elif get_next_turn(game) != player:
        raise InvalidMovement("\"{}\" moves next".format(game['next_turn']))
    elif not _position_is_valid(position):
        raise InvalidMovement("Position out of range.")
    elif not _position_is_empty_in_board(position, game['board']):
        raise InvalidMovement("Position already taken.")
    else:
        game['board'][position[0]][position[1]] = player
        if _check_winning_combinations(game['board'], player) == player:
            game['winner'] = player
            game['next_turn'] = None
            raise GameOver("\"{}\" wins!".format(player))
        elif _board_is_full(game['board']): 
            game['next_turn'] = None
            raise GameOver("Game is tied!")
        elif not _board_is_full(game['board']):
            if player == game['player1']:
                game['next_turn'] = game['player2']
            else:
                game['next_turn'] = game['player1']
"""
if game['next_turn'] != player:
        raise InvalidMovement("\"{}\" moves next".format(game['next_turn']))
    elif game['board'][position[0]][position[1]] != '-':
        raise InvalidMovement("Position already taken.")
    elif game['winner'] != None:
        raise GameOver("The Game is Over")
    else:
        game['board'][position[0]][position[1]] = player
        if player == game['player1']:
            game['next_turn'] = game['player2']
        else:
            game['next_turn'] = game['player1']        
"""

def get_board_as_string(game):
    """
    Returns a string representation of the game board in the current state.
    """
    #return "{} | {} | {}\n{} | {} | {}\n{} | {} | {}\n".format(game['board'])
    first_line = '  |  '.join(game['board'][0])
    second_line = '  |  '.join(game['board'][1])
    third_line = '  |  '.join(game['board'][2])
    separater = '\n--------------\n'
    string_board = '\n' + first_line + separater + second_line + separater + third_line + '\n'
    return string_board


def get_next_turn(game):
    """
    Returns the player who plays next, or None if the game is already over.
    """
    return game['next_turn']
