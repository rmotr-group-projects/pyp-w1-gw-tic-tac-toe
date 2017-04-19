# internal helpers

from tic_tac_toe.exceptions import * 

def _position_is_empty_in_board(position, board):
    """
    Checks if given position is empty ("-") in the board.

    :param position: Two-elements tuple representing a
                     position in the board. Example: (0, 1)
    :param board: Game board.

    Returns True if given position is empty, False otherwise.
    """
    row = position[0]
    indexInRow = position[1]
    
    return (board[row][indexInRow] == '-')
    
    pass


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
        
    return (position in valid_positions)
    
    pass


def _board_is_full(board):
    """
    Returns True if all positions in given board are occupied.

    :param board: Game board.
    """
    return not True in ['-' in row for row in board]
            
    pass


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
        positionRow, positionColumn = position
        if board[positionRow][positionColumn] != player:
            return False
            
    return True
    
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
    winningCombinations = [
        ((0,0), (0,1), (0,2)), #left-right top row
        ((0,0), (1,1), (2,2)), #diagonal - top left to bottom right
        ((0,0), (1,0), (2,0)), #vertical left side
        ((0,2), (1,1), (2,0)), #diagonal - top right to bottom left
        ((0,1), (1,1), (2,1)), #middle
        ((0,2), (1,2), (2,2)), #vertical right
        ((1,0), (1,1), (1,2)), #middle row horizontal
        ((2,0), (2,1), (2,2)), #bottom row horizontal 
        ]
        
    for combination in winningCombinations:
        if (_is_winning_combination(board, combination, player)):
            return player
            
    pass

# public interface
def start_new_game(player1, player2):
    """
    Creates and returns a new game configuration.
    """
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
    pass


def get_winner(game):
    """
    Returns the winner player if any, or None otherwise.
    """
    return game['winner']
    pass


def move(game, player, position):
    """
    Performs a player movement in the game. Must ensure all the pre requisites
    checks before the actual movement is done.
    After registering the movement it must check if the game is over.
    """
    board = game['board']
    
    #Check if game is over
    if get_next_turn(game) is None:
       raise InvalidMovement('Game is over.')
       
    # if player is not assigned as next_turn in game, raise that its other players turn
    if player is not game['next_turn']:
        raise InvalidMovement('"{}" moves next'.format(game['next_turn']))
        
    # If position is not valid move, raise position is out of range   
    if not (_position_is_valid(position)):
        raise InvalidMovement('Position out of range.')
    
    #If position is not empty, raise position is already taken
    if not (_position_is_empty_in_board(position, board)):
       raise InvalidMovement('Position already taken.')
       
    row = position[0]
    column = position[1]
    board[row][column] = player


    #Check if winning combination, raise winner
    if _check_winning_combinations(board, player) is player:
        game['winner'] = player
        raise GameOver('"{}" wins!'.format(player))

    #Check if game ends in a tie
    if game['winner'] == None and _board_is_full(board):
        raise GameOver('Game is tied!')
    
    #assign next turn after player move
    game['next_turn'] = game['player1'] if (player == game['player2']) else game['player2']

    pass


def get_board_as_string(game):
    """
    Returns a string representation of the game board in the current state.
    """
    board = game['board'] 
    string = []
    string.append('\n        ')
    #'O  |  O  |  X
    

    for row in board:
        string.append("  |  ".join(row))
        string.append("".join(["\n        --------------\n        "]))
    string.pop()
    string.append("\n        ")
    result = "".join(string)
    #print(result)
    return result
    
def get_next_turn(game):
    """
    Returns the player who plays next, or None if the game is already over.
    """
    if (get_winner(game) == None) and (_board_is_full(game['board']) == False):
        #raise InvalidMovement('Game is over.')
    #if game['winner'] != None:
        #return None
    #else:
        return game['next_turn']
    pass

