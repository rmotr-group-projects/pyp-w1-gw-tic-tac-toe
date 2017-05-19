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
    return True if board[position[0]][position[1]] == '-' else False


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
    if isinstance(position, tuple):    
        if position[0] in range(3) and position[1] in range(3) and len(position) == 2:
            return True
    return False


def _board_is_full(board):
    """
    Returns True if all positions in given board are occupied.

    :param board: Game board.
    """
    for row in board:
        for item in row:
            if item == '-':
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
    player_win = [player, player, player]
    check_win = [
        board[combination[0][0]][combination[0][1]], 
        board[combination[1][0]][combination[1][1]],
        board[combination[2][0]][combination[2][1]]
    ]
    if player_win == check_win:
        return True
    return False


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
    horizontal1 = _is_winning_combination(board, ((0, 0), (0, 1), (0, 2)), player)
    horizontal2 = _is_winning_combination(board, ((1, 0), (1, 1), (1, 2)), player)
    horizontal3 = _is_winning_combination(board, ((2, 0), (2, 1), (2, 2)), player)
    vertical1 = _is_winning_combination(board, ((0, 0), (1, 0), (2, 0)), player)
    vertical2 = _is_winning_combination(board, ((0, 1), (1, 1), (2, 1)), player)
    vertical3 = _is_winning_combination(board, ((0, 2), (1, 2), (2, 2)), player)
    diagonal1 = _is_winning_combination(board, ((0, 0), (1, 1), (2, 2)), player)
    diagonal2 = _is_winning_combination(board, ((0, 2), (1, 1), (2, 0)), player)
    
    if (horizontal1 or horizontal2 or horizontal3 or 
                vertical1 or vertical2 or vertical3 or diagonal1 or diagonal2):
        return player
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
    # If the board is full, or their is a winner no sense in going any further
    if (_board_is_full(game['board']) or game['winner']):
        raise InvalidMovement('Game is over.')
        
    if player != game['next_turn']:
        raise InvalidMovement('"{}" moves next.'.format(game['next_turn']))
        
    if not _position_is_valid(position):
        raise InvalidMovement('Position out of range.')
    
    if not _position_is_empty_in_board(position, game['board']):
        raise InvalidMovement('Position already taken.')
    
    game['board'][position[0]][position[1]] = player
    win = _check_winning_combinations(game['board'], player)
    if win:
        game['winner'] = player
        game['next_turn'] = None
        raise GameOver('"{}" wins!'.format(win))
    elif _board_is_full(game['board']):
        game['next_turn'] = None
        raise GameOver('Game is tied!')
    else:
        if player == game['player1']:
            game['next_turn'] = game['player2']
        else:
            game['next_turn'] = game['player1']

def get_board_as_string(game):
    """
    Returns a string representation of the game board in the current state.
    """
    string_board = """
{}  |  {}  |  {}
--------------
{}  |  {}  |  {}
--------------
{}  |  {}  |  {}
""".format(*[item for row in game['board'] for item in row])
    return string_board


def get_next_turn(game):
    """
    Returns the player who plays next, or None if the game is already over.
    """
    return game['next_turn']
