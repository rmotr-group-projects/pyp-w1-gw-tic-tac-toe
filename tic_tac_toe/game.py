# internal helpers
import random
from tic_tac_toe.exceptions import GameOver
from tic_tac_toe.exceptions import InvalidMovement

def _position_is_empty_in_board(position, board):
    """
    Checks if given position is empty ("-") in the board.
    :param position: Two-elements tuple representing a
                     position in the board. Example: (0, 1)
    :param board: Game board.

    Returns True if given position is empty, False otherwise.
    """
    #checks if each position in the board is "-", denoting if its empty
    if board[position[0]][position[1]] == "-":
        return True
    else:
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
    if type(position) == tuple:
        if len(position) == 2:
            if 0 <= position[0] <= 2 and 0 <= position[1] <= 2:
                return True
            else:
                return False
        else: 
            return False
    else:
        return False

def _board_is_full(board):
    """
    Returns True if all positions in given board are occupied.
    :param board: Game board.
    """
    if (reduce(lambda x,y: x+y,board)).count("-") == 0:
        return True
    else:
        return False

def _is_winning_combination(board, combination, player):
    """
    Checks if all 3 positions in given combination are occupied by given player.

    :param board: Game board.
    :param combination: Tuple containing three position elements.
                        Example: ((0,0), (0,1), (0,2)) 

    Returns True if all three positions in the combination belongs to given
    player, False otherwise.
    """
    if board[combination[0][0]][combination[0][1]] == player and board[combination[1][0]][combination[1][1]] == player and board[combination[2][0]][combination[2][1]] == player:
        return True
    else:
        return False
    """
    if combination.count(player) == 3:
        return True
    else: return False
    """ 
    
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
    
    combinations = (((0,0),(0,1),(0,2)),
                    ((0,0),(1,0),(2,0)),
                    ((0,0),(1,1),(2,2)),
                    ((0,2),(1,1),(2,0)),
                    ((0,2),(1,2),(2,2)),
                    ((2,0),(2,1),(2,2)),
                    ((1,0),(1,1),(1,2)),
                    ((0,1),(1,1),(2,1)))
    for singleCombo in combinations:
        if _is_winning_combination(board,singleCombo,player) == True:
            return player
    return None
    """
    #loop through and select each row
    for row in range(0,3):
        combination = board[row]
        if _is_winning_combination(board, combination, player) == True:
            return player
        else: 
            return None

    #loop through and select each column
    for column in range(0,3):
        combination = []
        #select each position and check if index was players move
        for position in range(0,3):
            combination.append(board[column[position]])
            
    if _is_winning_combination(board, combination, player) == True:
        return player
    else: return None
    
    combination = [board[0][0], board[1][1], board[2][2]]
    if _is_winning_combination(board, combination, player) == True:
        return player
    else: return None
    
    combination = [board[0][2], board[1][1], board[2][0]]
    if _is_winning_combination(board, combination, player) == True:
        return player
    else: return None
    """

def start_new_game(player1, player2):
    game = {
        'player1': "X",
        'player2': "O",
        'board': [
                ["-", "-", "-"],
                ["-", "-", "-"],
                ["-", "-", "-"],
        ],
        'next_turn': "X",
        'winner': None
    }
    return game

def get_winner(game):
    """
    Returns the winner player if any, or None otherwise.
    """
    return game['winner']
 
def move(game, player, position=None):
    """
    Performs a player movement in the game. Must ensure all the pre requisites
    checks before the actual movement is done.
    After registering the movement it must check if the game is over.
    """
    if get_winner(game) != None or _board_is_full(game['board']) == True:
        raise InvalidMovement('Game is over.')
        
    elif player != game['next_turn']:
        if game['next_turn'] == game['player1']:
            raise InvalidMovement('"X" moves next')
        else:
            raise InvalidMovement('"O" moves next')
        
    elif _position_is_valid(position) == False:
        raise InvalidMovement("Position out of range.")
    
    elif _position_is_empty_in_board(position, game['board']) == False:
        raise InvalidMovement("Position already taken.")
    
    else:
        board = game['board']
        board[position[0]][position[1]] = player

    game['winner'] = _check_winning_combinations(game["board"], player)
    
    if _check_winning_combinations(game['board'], player) != None:
        if get_winner(game) == game['player1']:
            raise GameOver('"X" wins!')
        else:
            raise GameOver('"O" wins!')
        
    if _board_is_full(game['board']) == True:
        raise GameOver("Game is tied!")
    
    if game['next_turn'] == game['player1']:
        game['next_turn'] = 'O'
    else:
        game['next_turn'] = 'X'
        
    get_next_turn(game)
    get_board_as_string(game)
    
def get_board_as_string(game):
    board = "\n"
    dash = 0
    for line in game['board']:
        board = board + print_line(line)
        if dash != 2:
            board = board + print_dashs()
            dash = dash + 1
    return board
    
def print_line(line):
    return line[0] + "  |  " + line[1] + "  |  " + line[2] + "\n"

def print_dashs():
    return "--------------\n"

def get_next_turn(game):
    """
    Returns the player who plays next, or None if the game is already over.
    """
    if game['winner'] != None:
        return None
    if _board_is_full(game['board']):
        return None
    else: return game['next_turn']

    
    
