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
    # --- assumes that position is already valid.
    return board[position[0]][position[1]] == '-'

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
    #--- creates a list of all possible valid positions and checks against that.
    valid_positions = [(x, y) for x in xrange(3) for y in xrange(3)]
    return position in valid_positions


def _board_is_full(board):
    """
    Returns True if all positions in given board are occupied.

    :param board: Game board.
    """
    #--- flattens the board structure to a single, 9 length, list to make it easier to check.
    board_positions = [position for i in board for position in i]
    return '-' not in board_positions


def _is_winning_combination(board, combination, player):
    """
    Checks if all 3 positions in given combination are occupied by given player.

    :param board: Game board.
    :param combination: Tuple containing three position elements.
                        Example: ((0,0), (0,1), (0,2))

    Returns True of all three positions in the combination belongs to given
    player, False otherwise.
    """
    for x, y in combination:
        if not _position_is_valid(x, y):
            raise InvalidMovement('Position out of range.')
        if board[x][y] != player:
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
    
    # Determines whether there are more than 4 moves made already
    if len([space for row in board for space in row if space != "-"]) < 5:
        return None
    
    # --- function returns early if the player provided has won.
    # --- check horizontals
    for row in board:
        if all([col == player for col in row]):
            return player
            
    # --- check verticals
    for col in map(list, zip(*board)):
        if all([row == player for row in col]):
            return player
    
    # --- check diagonals
    diagonals = [[(0,0), (1,1), (2,2)], [(0,2), (1,1), (2,0)]]
    for diagonal in diagonals:
        if all([board[x][y] == player for x, y in diagonal]):
            return player
    
    # --- if program reached this point, the player did not win.
    # --- instructions say to return None instead of False.
    return None
    


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
    
    # --- check if game is already over
    if game['winner'] or _board_is_full(game['board']):
        raise InvalidMovement('Game is over.')
    
    # --- check if position is valid
    if not _position_is_valid(position):
        raise InvalidMovement('Position out of range.')
        
    # --- check if position is already filled
    if not _position_is_empty_in_board(position, game['board']):
        raise InvalidMovement('Position already taken.')
        
    # --- check if player turn is correct
    if not player == get_next_turn(game):
        if player == game['player1']:
            raise InvalidMovement('InvalidMovement: "%s" moves next.' % game['player2'])
        else:
            raise InvalidMovement('InvalidMovement: "%s" moves next.' % game['player1'])
    
    game['board'][position[0]][position[1]] = player
    game['winner'] = _check_winning_combinations(game['board'], player)
    
    # --- check if game is over after movement is made
    if game['winner']:
        raise GameOver('GameOver: "%s" wins!' % (game['winner']))
    elif _board_is_full(game['board']):
        raise GameOver('GameOver: Game is tied!')

def get_board_as_string(game):
    """
    Returns a string representation of the game board in the current state.
    """
    return """
%s  |  %s  |  %s
--------------
%s  |  %s  |  %s
--------------
%s  |  %s  |  %s
""" % tuple([position for row in game['board'] for position in row])


def get_next_turn(game):
    """
    Returns the player who plays next, or None if the game is already over.
    """
    flat_board = [position for row in game['board'] for position in row]
    if flat_board.count(game['player1']) == flat_board.count(game['player2']):
        return game['player1']
    else:
        return game['player2']