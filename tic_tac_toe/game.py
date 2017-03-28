# internal helpers
from .exceptions import GameOver, InvalidMovement

def _position_is_empty_in_board(position, board):
    """
    Checks if given position is empty ("-") in the board.

    :param position: Two-elements tuple representing a
                     position in the board. Example: (0, 1)
    :param board: Game board.

    Returns True if given position is empty, False otherwise.
    """

    return board[position[0]][position[1]] == "-"


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
        if len(position)==2:
            x, y = position
            if isinstance(x, int) and isinstance(y, int) :
                if all(0 <= values <=2 for values in position):
                    return True
    return False
    


def _board_is_full(board):
    """
    Returns True if all positions in given board are occupied.

    :param board: Game board.
    """
    for outer_list in board:
        for inner_list in outer_list:
            if inner_list == "-":
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

    for win in combination:
        if board[win[0]][win[1]] != player:
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
        # horizontal wins
        ((0,0), (0,1), (0,2)),    
        ((1,0), (1,1), (1,2)),    
        ((2,0), (2,1), (2,2)),
        # vertical wins
        ((0,0), (1,0), (2,0)),
        ((0,1), (1,1), (2,1)),
        ((0,2), (1,2), (2,2)),
        # diagonal wins
        ((0,0), (1,1), (2,2)),
        ((0,2), (1,1), (2,0)),
    )
    
    for win in combinations:
        if _is_winning_combination(board, win, player):
            return player

# public interface
def start_new_game(player1, player2):
    """
    Creates and returns a new game configuration.
    """
    initial_game_config = {
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
    return initial_game_config

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

    if game['winner'] or _board_is_full(game['board']):
        raise InvalidMovement("Game is over.")
    
    elif get_next_turn(game) != player:
        raise InvalidMovement('"{}" moves next'.format(game['next_turn']))
    if _position_is_valid(position):
        if not _position_is_empty_in_board(position, game['board']):
            raise InvalidMovement("Position already taken.")
        game['board'][position[0]][position[1]] = player
        if game['next_turn'] == game['player1']:
            game['next_turn'] = game['player2']
        else:
            game['next_turn'] = game['player1']
    else:
        raise InvalidMovement("Position out of range.")
    
    if _check_winning_combinations(game['board'], player):
        game['winner'] = player
        game['next_turn'] = None
        raise GameOver('"{}" wins!'.format(player)) 
    elif _board_is_full(game['board']) and not game['winner']:
        game['winner'] = None
        game['next_turn'] = None
        raise GameOver('Game is tied!')
        

def get_board_as_string(game):
    """
    Returns a string representation of the game board in the current state.
    """
    first_line = '  |  '.join(game['board'][0])
    second_line = '  |  '.join(game['board'][1])
    third_line = '  |  '.join(game['board'][2])
    separater = '\n--------------\n'
    string_board = '\n' + first_line + separater + second_line + separater + third_line + '\n'
    return string_board


def get_next_turn(game):
    """
    Returns the player who plays next, or None if the game is already over.
    """
    return game['next_turn']
