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
    
    if board[row][indexInRow] == '-':
        return True
    else:
        return False
    
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
        
    if position in valid_positions:
        return True
    else:
        return False
    
    pass


def _board_is_full(board):
    """
    Returns True if all positions in given board are occupied.

    :param board: Game board.
    """
    
    
    isFull = True
    for positionList in board:
        for position in positionList: 
            if position == '-':
                isFull = False
    return isFull
            
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

    #((0,0), (0,1), (0,2))
    isWinningCombo = True
    for position in combination:
        positionRow = position[0]
        positionColumn = position[1]
        if board[positionRow][positionColumn] != player:
            isWinningCombo = False
            
    return isWinningCombo
    
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
        if _is_winning_combination(board, combination, player) == True:
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
    
    current_player = player
    players = ['X', 'O']
    next_player = [p for p in players if p != current_player ]
    
    
    if get_next_turn(game) == None:
       raise InvalidMovement('Game is over')
       
    elif _position_is_valid(position) == False:
        raise InvalidMovement('Position out of range.')
    
    elif _position_is_empty_in_board(position, board) == False:
       raise InvalidMovement('Position already taken.')
    
    elif _position_is_valid(position) and _position_is_empty_in_board(position, board): 
        row = position[0]
        column = position[1]
        board[row][column] = player
        if _check_winning_combinations(board, player) == player:
            game['winner'] = player
            if player == "X":
                raise GameOver('"X" wins!')
            else:
                raise GameOver('"O" wins!')
        elif game['winner'] == None and _board_is_full(board):
            raise GameOver('Game is tied!')
    
    game['next_turn'] = next_player[0]

    pass


def get_board_as_string(game):
    """
    Returns a string representation of the game board in the current state.
    """
    board = game['board'] 
    string = []
    for row in board:
        string.append("  |  ".join(row))
        string.append("".join(["\n","--------------","\n"]))
    
    string.pop()
    result = "".join(string)
    #print(result)
    return result

def get_next_turn(game):
    """
    Returns the player who plays next, or None if the game is already over.
    """
    if game['winner'] != None:
        return None
    else:
        return game['next_turn']
    pass

    # if !_position_is_empty_in_board:
        #game['next_turn'] = None
    # elif game['next_turn'] == 'X':
    #     game['next_turn'] = 'O'
    # elif game['next_turn'] == 'O':
    #     game['next_turn'] = 'X'
    # return game['next_turn']