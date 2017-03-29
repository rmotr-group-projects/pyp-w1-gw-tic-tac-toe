from exceptions import *
# internal helpers
def _position_is_empty_in_board(position, board):
    """
    Checks if given position is empty ("-") in the board.

    :param position: Two-elements tuple representing a
                     position in the board. Example: (0, 1)
    :param board: Game board.

    Returns True if given position is empty, False otherwise.
    """
    # if position on board is "-" return True
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
    if isinstance(position,int):
        return False
    elif len(position) > 2:
        return False
    if position[0] > 2 or position[1] < 0:
        return False
    if position[1] > 2 or position[1] < 0:
        return False
    return True

def _board_is_full(board):
    """
    Returns True if all positions in given board are occupied.

    :param board: Game board.
    """
    # board = [[row0],[row1],[row2]]
    for row in board:
        for column in row:
            if column == '-':
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
    """
    first_row = ((0, 0), (0, 1), (0, 2))
    second_row = ((1, 0), (1, 1), (1, 2))
    third_row = ((2, 0), (2, 1), (2, 2))
    first_col = ((0, 0), (1, 0), (2, 0))
    second_col = ((0, 1), (1, 1), (2, 1))
    third_col = ((0, 2), (1, 2), (2, 2))
    diag_1 = ((0, 0), (1, 1), (2, 2))
    diag_2 = ((0, 2), (1, 1), (2, 0))
    winning_combinations  = [first_row, second_row, third_row, first_col, second_col, third_col, diag_1, diag_2]
                            
    for combination in winning_combinations:
        if _is_winning_combination(board, combination, player):
            return player
    return None


# public interface
def start_new_game(player1, player2):
    """
    Creates and returns a new game configuration.
    """
    return {
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


def get_winner(game):
    """
    Returns the winner player if any, or None otherwise.
    """
    if _check_winning_combinations(game['board'], game['player1']):
        return(game['player1'])
    elif _check_winning_combinations(game['board'], game['player2']):
        return(game['player2'])
    else:
        return None


def move(game, player, position):
    """
    Performs a player movement in the game. Must ensure all the pre requisites
    checks before the actual movement is done.
    After registering the movement it must check if the game is over.
    """
    # check input
    if (_board_is_full(game['board'])) or (game['winner'] != None):
        raise InvalidMovement("Game is over.")
    if game['next_turn'] != player:
        if game['next_turn'] == 'O':
            raise InvalidMovement('"O" moves next.')
        else:
            raise InvalidMovement('"X" moves next.')
    if  not _position_is_valid(position):
        raise InvalidMovement('Position out of range.')
    if not _position_is_empty_in_board(position, game['board']):
        raise InvalidMovement('Position already taken.')
        
    # make move, toggle next player
    game['board'][position[0]][position[1]] = player
    if player == game['player1']:
        game['next_turn'] = game['player2']
    elif player == game['player2']:
        game['next_turn'] = game['player1']
    
    
    # check game endings
    game['winner'] = get_winner(game)
    if game['winner'] == game['player1']:
        raise GameOver('"X" wins!')
    elif game['winner'] == game['player2']:
        raise GameOver('"O" wins!')
    elif _board_is_full(game['board']) and game['winner'] == None:  
        raise GameOver("Game is tied!")
    return                                                                                                                      

def get_board_as_string(game):
    """
    Returns a string representation of the game board in the current state.
    """
    
    lines = len(game['board']) - 1
    board_string = '\n'
    for row in game['board']:
        board_string += ('%s  |  %s  |  %s\n' % (row[0], row[1], row[2]))
        if lines >0:
            board_string += '--------------\n'
            lines -= 1
    return  board_string                                                                                                                    


def get_next_turn(game):
    """
    Returns the player who plays next, or None if the game is already over.
    """
    return game['next_turn']
