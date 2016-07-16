from .exceptions import *

# internal helpers
def _position_is_empty_in_board(position, board): #N
    """
    Checks if given position is empty ("-") in the board.

    :param position: Two-elements tuple representing a
                     position in the board. Example: (0, 1)
    :param board: Game board.

    Returns True if given position is empty, False otherwise.
    """
    x, y = position
    return board[x][y] == '-'
    


def _position_is_valid(position): #Sam Foo
    """
    Checks if given position is a valid. To consider a position as valid, it
    must be a two-elements tuple, containing values from 0 to 2.
    Examples of valid positions: (0,0), (1,0)
    Examples of invalid positions: (0,0,1), (9,8), False

    :param position: Two-elements tuple representing a
                     position in the board. Example: (0, 1)

    Returns True if given position is valid, False otherwise.
    """
    if len(position) > 2:
        return False
    for dimension in position:
        if 0 >= dimension >= 2:
            return False
    return True


def _board_is_full(board): #Kenneth
    """
    Returns True if all positions in given board are occupied.

    :param board: Game board.
    """
    status = False
    if True not in [('-' in row) for row in board]:
        status = True
    return status


def _is_winning_combination(board, combination, player): #N
    """
    Checks if all 3 positions in given combination are occupied by given player.

    :param board: Game board.
    :param combination: Tuple containing three position elements.
                        Example: ((0,0), (0,1), (0,2))

    Returns True of all three positions in the combination belongs to given
    player, False otherwise.
    """
    players_comb = [board[x][y] for (x,y) in combination]
    return [player] * 3 == players_comb


def _check_winning_combinations(board, player): #Sam Foo
    #Check horizontals
    #x = [1,2,3]
    #y = [4,5,6]
    #zip() in conjunction with the * operator can be used to unzip a list:
    #zip(x,y) == [(1,4),(2,5),(3,6)]
    #*zip(zip(x,y)) = [[1,2,3],[4,5,6]]
    #zip(['x','*',9],[1,2,4],['&',5,7]) == [(x,1,&),(*,2,5),(9,4,7)] ->let call this matrix
    #*zip(matrix) == [['x','*',9],[1,2,4],['&',5,7]]
    #map(list, zip(*board))
    
    for i in range(2):
        for line in board:#range(len(board)):
            #if "-" in board[line]:
                return None
            if line == [player] * 3:
                return player
        board = list(map(list, zip(*board))) #transpose, redo horiz. check
            
    #Check diagonals
    length = len(board)
    diagonal_1 = [board[i][i] for i in range(length)]
    diagonal_2 = [board[i][-i-1] for i in range(length)]
    diagonals = [diagonal_1,diagonal_2]
    if [player] * 3 in diagonals:
        return player
    else:
        return None

# public interface
def start_new_game(player1="X", player2="O"): #Kenneth
    """
    Creates and returns a new game configuration.
    """
    
    return {
        'player1': player1,
        'player2': player2,
        'board': [
                ['-','-','-'],
                ['-','-','-'],
                ['-','-','-']
            ],
        'next_turn': player1,
        'winner': None    
    }

def get_winner(game): #N
    """
    Returns the winner player if any, or None otherwise.
    """
    return game['winner']


def move(game, player, position): #Sam Foo
    """
    Performs a player movement in the game. Must ensure all the pre requisites
    checks before the actual movement is done.
    After registering the movement it must check if the game is over.
    """
    #check if the game is over: get_winner see if returns winner
    if game['winner']:
        raise InvalidMovement("Game is over.")

    #check if the position is valid
    if not _position_is_valid(position):
        raise InvalidMovement('Position out of range.')
    
    #check if the position is already taken
    if not _position_is_empty_in_board(position,game['board']):
        raise InvalidMovement('Position already taken.')
    
    #place the player in the given position
    (x,y) = position
    game['board'][x][y] = player
    
    
    
    
    

    
    #determines and updates the winner
    

    #


def get_board_as_string(game): #Nicolas
    """
    Returns a string representation of the game board in the current state.
    """
    representation = ""
    for line in game['board']:
        for element in line:
            representation += element + " | "
        representation += "\n--------------\n"
    return representation


def get_next_turn(game): #Kenneth
    """
    Returns the player who plays next, or None if the game is already over.
    """
    if get_winner(game):
        return None
    else:
        return game['next_turn']
