from .exceptions import *

# internal helpers
def _position_is_empty_in_board(position, board):
    """
    Checks if given position is empty ("-") in the board.

    :param position: Two-elements tuple representing a
                     position in the board. Example: (0, 1)
    :param board: Game board.

    Returns True if given position is empty, False otherwise.
    """
    if _position_is_valid(position):
        if board[position[0]][position[1]] == '-':
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
    if isinstance(position, tuple):
        if len(position) == 2:
            if position[0] <= 2 and position[1] <= 2:
                if position[0] >= 0 and position[1] >= 0:
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
    for position in combination:
        if board[position[0]][position[1]] != player:
            # if any position is not the player's character then it must be False
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

    Returns the player (winner) if any of the winning combinations is completed
    by given player, or None otherwise.
    """

    up_down = (
    ((0, 0), (1, 0), (2, 0)),
    ((0, 1), (1, 1), (2, 1)),
    ((0, 2), (1, 2), (2, 2))
    )
    
    diag = (
    ((0, 0), (1, 1), (2, 2)),
    ((0, 2), (1, 1), (2, 0)),
    )
    
    left_right = (
    ((0, 0), (0, 1), (0, 2)),
    ((1, 0), (1, 1), (1, 2)),
    ((2, 0), (2, 1), (2, 2))
    )
    
    for combo in up_down:
      if _is_winning_combination(board, combo, player):
          return player
    
    for combo in left_right:
      if _is_winning_combination(board, combo, player):
          return player
    
    for combo in diag:
      if _is_winning_combination(board, combo, player):
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
    
    if game['winner']:
        raise InvalidMovement("Game is over.")
    if _board_is_full(game['board']):
        raise InvalidMovement("Game is over.")
    if _position_is_valid(position) is False:
        raise InvalidMovement("Position out of range.")
    if _position_is_empty_in_board(position, game['board']) is False:
        raise InvalidMovement("Position already taken.")
    if player != game['next_turn']:
        raise InvalidMovement('"{}" moves next.'.format(game['next_turn']))

    game['board'][position[0]][position[1]] = player
    if player == "X":
        game['next_turn'] = 'O'
    else:
        game['next_turn'] = 'X'
    if _check_winning_combinations(game['board'], player) is not None:
        game['winner'] = player
        raise GameOver('"{}" wins!'.format(player))

    elif _board_is_full(game['board']):
        game['next_turn'] = None
        raise GameOver("Game is tied!")


# if theres a winner or the board is full >> raise invalidmovement(gameover)
# if the player is not the next player >> raise invalid movement (next_turn is next)


def get_board_as_string(game):
    """
    Returns a string representation of the game board in the current state.
    """
    moves = []
    for row in game['board']:
        moves.extend([pos for pos in row])
    
    #for row in game['board']:
    #    for pos in row:
    #       return pos
    
    #[pos for pos in row for row in game['board']]
    
    return """
{}  |  {}  |  {}
--------------
{}  |  {}  |  {}
--------------
{}  |  {}  |  {}
""".format(moves[0], moves[1], moves[2], moves[3], moves[4], moves[5], moves[6], moves[7], moves[8])


def get_next_turn(game):
    """
    Returns the player who plays next, or None if the game is already over.
    """
    if game['winner']:
        return None
    return game['next_turn']
