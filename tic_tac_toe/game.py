from tic_tac_toe.exceptions import *


# internal helpers
def _position_is_empty_in_board(position, board):
    """
    Checks if given position is empty ("-") in the board.

    :param position: Two-elements tuple representing a
                     position in the board. Example: (0, 1)
    :param board: Game board.

    Returns True if given position is empty, False otherwise.
    """

    return True if board[position[0]][position[1]] is "-" else False


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

    valid_positions = (
        (0, 0), (0, 1), (0, 2),
        (1, 0), (1, 1), (1, 2),
        (2, 0), (2, 1), (2, 2),
    )

    return True if position in valid_positions else False


def _board_is_full(board):
    """
    Returns True if all positions in given board are occupied.

    :param board: Game board.
    """

    # Note: Lets make this pretty into a nested comprehension or something
    for row in board:
        for position in row:
            if position is "-":
                return False
    else:
        return True


def _is_winning_combination(board, combination, player):  # Not in tests
    """
    Checks if all 3 positions in given combination are occupied by given player.

    :param board: Game board.
    :param combination: Tuple containing three position elements.
                        Example: ((0,0), (0,1), (0,2))

    Returns True if all three positions in the combination belongs to given
    player, False otherwise.
    """
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

    win_combs = (
        ((0, 0), (0, 1), (0, 2)),
        ((1, 0), (1, 1), (1, 2)),
        ((2, 1), (2, 1), (2, 2)),
        ((0, 0), (1, 0), (2, 0)),
        ((0, 1), (1, 1), (2, 1)),
        ((0, 2), (1, 2), (2, 2)),
        ((0, 0), (1, 1), (2, 2)),
        ((0, 2), (1, 1), (2, 0))
    )

    winner = None

    for comb in win_combs:
        bingo = all([board[pos[0]][pos[1]] == player for pos in comb])

        if bingo:
            winner = player
            break

    return winner


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

    if _board_is_full(game['board']) or get_winner(game):
        raise InvalidMovement('Game is over.')

    if player is not game['next_turn']:
        raise InvalidMovement('"O" moves next')

    pos_valid = _position_is_valid(position)
    if not pos_valid:
        raise InvalidMovement("Position out of range.")

    pos_empty = _position_is_empty_in_board(position, game['board'])
    if not pos_empty:
        raise InvalidMovement("Position already taken.")

    game['board'][position[0]][position[1]] = player

    if _check_winning_combinations(game['board'], player):
        game['winner'] = player
        raise GameOver('"{}" wins!'.format(player))

    if _board_is_full(game['board']):
        raise GameOver('Game is tied!')

    if game['next_turn'] is game['player1']:
        game['next_turn'] = game['player2']
    else:
        game['next_turn'] = game['player1']


def get_board_as_string(game):
    """
    Returns a string representation of the game board in the current state.
    """

    b = game['board']

    board_string = """
{}  |  {}  |  {}
--------------
{}  |  {}  |  {}
--------------
{}  |  {}  |  {}
""".format(
            b[0][0], b[0][1], b[0][2],
            b[1][0], b[1][1], b[1][2],
            b[2][0], b[2][1], b[2][2],
        )

    return board_string


def get_next_turn(game):
    """
    Returns the player who plays next, or None if the game is already over.
    """

    return game['next_turn']
