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

    if type(position) != tuple:
        return False
    elif len(position) > 2:
        return False
    elif position[0] not in range(3):
        return False
    elif position[1] not in range(3):
        return False
    else:
        return True


def _board_is_full(board):
    """
    Returns True if all positions in given board are occupied.

    :param board: Game board.
    """
    flat_board = [marker for row in board for marker in row]
    status = [True if place != '-' else False for place in flat_board]
    return all(status)


def _is_winning_combination(board, combination, player):
    """
    Checks if all 3 positions in given combination are occupied by given player.

    :param board: Game board.
    :param combination: Tuple containing three position elements.
                        Example: ((0,0), (0,1), (0,2))

    Returns True of all three positions in the combination belongs to given
    player, False otherwise.
    """
    
    return all([
        True if board[each[0]][each[1]] is player
        else False for each in combination
        ])


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
    winning_combinations = (
        ((0, 0), (1, 1), (2, 2)),
        ((0, 2), (1, 1), (2, 0)),
        ((0, 0), (1, 0), (2, 0)),
        ((0, 1), (1, 1), (2, 1)),
        ((0, 2), (1, 2), (2, 2)),
        ((0, 0), (0, 1), (0, 2)),
        ((1, 0), (1, 1), (1, 2)),
        ((2, 0), (2, 1), (2, 2)) 
    )

    win_list = [
        True if _is_winning_combination(board, each, player)
        else False for each in winning_combinations
    ]
    
    if any(win_list):
        return player
    else:
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
    'next_turn': "X",
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
    board = game['board']

    if game['winner'] is not None or _board_is_full(game['board']):
        raise InvalidMovement('Game is over.')
        
    if player != get_next_turn(game):
        raise InvalidMovement('"{}" moves next.'.format(game['next_turn']))
        
    if not _position_is_valid(position):
        raise InvalidMovement('Position out of range.')
        
    if not _position_is_empty_in_board(position, board):
        raise InvalidMovement('Position already taken.')
    
    board[position[0]][position[1]] = player
    winner = _check_winning_combinations(board, player)
    print(winner)
    if winner is not None:
        game['winner'] = winner
        raise GameOver('"{}" wins!'.format(winner))
    elif _board_is_full(board):
        raise GameOver('Game is tied!')
    else:
        for each in [game['player1'], game['player2']]:
            if each != player:
                game['next_turn'] = each


def get_board_as_string(game):
    """
    Returns a string representation of the game board in the current state.
    """
    return """
{0}  |  {1}  |  {2}
--------------
{3}  |  {4}  |  {5}
--------------
{6}  |  {7}  |  {8}
""".format(
    game['board'][0][0], game['board'][0][1], game['board'][0][2],
    game['board'][1][0], game['board'][1][1], game['board'][1][2],
    game['board'][2][0], game['board'][2][1], game['board'][2][2]
    )


def get_next_turn(game):
    """
    Returns the player who plays next, or None if the game is already over.
    """
    return game['next_turn']
