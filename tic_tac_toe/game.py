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
    board_list = board[position[0]]
    
    return(board_list[position[1]] == "-")


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
    if not isinstance(position, tuple):
        return(False)
        
    if len(position) == 2:
        if position[0] in range(3) and position[1] in range(3):
            return(True)
    else:
        return(False)


def _board_is_full(board):
    """
    Returns True if all positions in given board are occupied.

    :param board: Game board.
    """
    for board_list in board:
        if "-" in board_list:
            return(False)
        
    return(True)


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
        # If we any position DOESN'T contain a player
        # we can just return False
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
    combinations = (
        # horizontals
        ((0,0), (0,1), (0,2)),
        ((1,0), (1,1), (1,2)),
        ((2,0), (2,1), (2,2)),

        # verticals
        ((0,0), (1,0), (2,0)),
        ((0,1), (1,1), (2,1)),
        ((0,2), (1,2), (2,2)),

        # diagonals
        ((0,0), (1,1), (2,2)),
        ((2,0), (1,1), (0,2)),
    )
    for combination in combinations:
        if _is_winning_combination(board, combination, player):
            return player
    return None


# public interface
def start_new_game(player1, player2):
    """
    Creates and returns a new game configuration.
    """
    new_game = {
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
    return(new_game)


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
    board = game['board']
    if game['winner'] or _board_is_full(board):
        raise InvalidMovement("Game is over.")
        
    elif not _position_is_valid(position):
        raise InvalidMovement('Position out of range.')
    
    elif not _position_is_empty_in_board(position, board):
        raise InvalidMovement('Position already taken.')
    
    elif get_next_turn(game) != player:
        raise InvalidMovement('"{}" moves next'.format(game['next_turn']))
    
    if player == game['player1']:
        game['next_turn'] = game['player2']
    else:
        game['next_turn'] = game['player1']
    
    board[position[0]][position[1]] = player
    
    winner = _check_winning_combinations(board, player)
    
    if winner:
        game['winner'] = winner
        game['next_turn'] = None
        raise GameOver('"{}" wins!'.format(winner))
    
    elif _board_is_full(board):
        game['next_turn'] = None
        raise GameOver('Game is tied!')


def get_board_as_string(game):
    """
    Returns a string representation of the game board in the current state.
    """
    board_string = """
{}  |  {}  |  {}
--------------
{}  |  {}  |  {}
--------------
{}  |  {}  |  {}
"""
        
    board = game['board']
    
    return board_string.format(board[0][0],board[0][1],board[0][2],board[1][0],board[1][1],board[1][2],board[2][0],board[2][1],board[2][2])


def get_next_turn(game):
    """
    Returns the player who plays next, or None if the game is already over.
    """
    return game['next_turn']
