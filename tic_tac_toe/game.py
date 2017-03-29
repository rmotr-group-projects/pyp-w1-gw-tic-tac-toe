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
    row = position[0]
    col = position[1]
    if board[row][col] == "-":
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
    if isinstance(position, tuple) and len(position) <= 2 and len(position) >= 0 and position[0] >= 0 and position[0] <= 2 and position[1] >= 0 and position[1] <= 2:
        return True
    else:
        return False


def _board_is_full(board):
    """
    Returns True if all positions in given board are occupied.

    :param board: Game board.
    """
    for row in board:
        for cell in row:
            if cell == "-":
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
    cell_1 = combination[0]
    cell_2 = combination[1]
    cell_3 = combination[2]
    
    count = 0
    
    if board[cell_1[0]][cell_1[1]] == player and board[cell_2[0]][cell_2[1]] == player and board[cell_3[0]][cell_3[1]] == player:
        return True
    else:
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


def move(game, player, position):
    """
    Performs a player movement in the game. Must ensure all the pre requisites
    checks before the actual movement is done.
    After registering the movement it must check if the game is over.
    """
    status = ""
    
    if not _position_is_valid(position):
        raise InvalidMovement('Position out of range.')
    if game['winner'] or _board_is_full(game['board']):
        raise InvalidMovement('Game is over.')
    if game['board'][position[0]][position[1]] != "-":
        raise InvalidMovement('Position already taken.')
    if player != game['next_turn']:
        raise InvalidMovement('"{}" moves next' .format(game['next_turn']))

    if player == game['player1']:
        game['next_turn'] = game['player2']
    else:
        game['next_turn'] = game['player1']
        
    game['board'][position[0]][position[1]] = player
    
    if _check_winning_combinations(game['board'], player) != None:
        game['winner'] = player
        raise GameOver('"{}" wins!' .format(game['winner']))
    
    if _board_is_full(game['board']) == True and _check_winning_combinations(game['board'], player) == None:
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
