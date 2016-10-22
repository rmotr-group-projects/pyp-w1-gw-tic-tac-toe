from .exceptions import InvalidMovement, GameOver


# internal helpers
def _switch_player(game,player):
    next_player = game['player1']
    
    if (player == next_player):
        next_player = game['player2']
    
    game['next_player'] = next_player
    
    return next_player
    

def _position_is_empty_in_board(position, board):
    """
    Checks if given position is empty ("-") in the board.

    :param position: Two-elements tuple representing a
                     position in the board. Example: (0, 1)
    :param board: Game board.

    Returns True if given position is empty, False otherwise.
    """
    result = None
    if board[position[0]][position[1]] == '-':
        result = True
    else:
        result = False
    return result


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
    # if x in position
    result = False
    
    if type(position) == tuple and len(position) == 2:
        if len([x for x in position if x >= 0 and x <= 2 and type(x) == int]) == 2:
            result = True

    return result
    
    '''
    if (position[0] < 0 or position[0] > 2 and position[1] < 0 or position[1] >2):
        result = False
    return result
    '''

def _board_is_full(board):
    """
    Returns True if all positions in given board are occupied.

    :param board: Game board.
    """
    result = True
    
    if (any('-' in sublist for sublist in board)):
        result = False
    
    return result
    
    
def _is_winning_combination(board, combination, player):
    """
    Checks if all 3 positions in given combination are occupied by given player.

    :param board: Game board.
    :param combination: Tuple containing three position elements.
                        Example: ((0,0), (0,1), (0,2))

    Returns True of all three positions in the combination belongs to given
    player, False otherwise.
    """
    # ((0, 0), (0, 1), (0, 2))
    for x in combination:
        if board[x[0]][x[1]] != player:
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
    
    combinations = [
        ((0, 0), (0, 1), (0, 2)),
        ((1, 0), (1, 1), (1, 2)),
        ((2, 0), (2, 1), (2, 2)),
        ((0, 0), (1, 0), (2, 0)),
        ((0, 1), (1, 1), (2, 1)),
        ((0, 2), (1, 2), (2, 2)),
        ((0, 0), (1, 1), (2, 2)),
        ((2, 0), (1, 1), (0, 2)),
    ]
    
    for combination in combinations:
        print(combination)
        if _is_winning_combination(board, combination, player):
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
    
    if get_next_turn(game) != player:
        raise InvalidMovement('"{}" moves next'.format(get_next_turn(game)))
    
    if not _position_is_valid(position):
        raise InvalidMovement('Position out of range.')
        
    
    if _board_is_full(game['board']) or game['winner'] != None:
        raise InvalidMovement('Game is over.')
        
    if not _position_is_empty_in_board(position, game['board']):
        raise InvalidMovement('Position already taken.')
    
    if _position_is_empty_in_board(position, game['board']):
        game['board'][position[0]][position[1]] = player
        game['next_turn'] = _switch_player(game, player)
    
    if _check_winning_combinations(game['board'], player):
        game['winner'] = player
        raise GameOver('"{}" wins!'.format(player))
    elif _board_is_full(game['board']):
        raise GameOver('Game is tied!')



def get_board_as_string(game):
    """
    Returns a string representation of the game board in the current state.
    """
    game = game['board']
    
    return '''
{}  |  {}  |  {}
--------------
{}  |  {}  |  {}
--------------
{}  |  {}  |  {}
'''.format(game[0][0], game[0][1], game[0][2], game[1][0], game[1][1], game[1][2], game[2][0], game[2][1], game[2][2])
        


def get_next_turn(game):
    """
    Returns the player who plays next, or None if the game is already over.
    """
    return game['next_turn']
