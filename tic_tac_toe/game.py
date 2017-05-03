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
    return type(position) == tuple and len(position) == 2 and position[0] in range(0, 3) and position[1] in range(0, 3)


def _board_is_full(board):
    """
    Returns True if all positions in given board are occupied.

    :param board: Game board.
    """
    return all([square != "-" for row in board for square in row])


def _is_winning_combination(board, combination, player):
    """
    Checks if all 3 positions in given combination are occupied by given player.

    :param board: Game board.
    :param combination: Tuple containing three position elements.
                        Example: ((0,0), (0,1), (0,2))

    Returns True of all three positions in the combination belongs to given
    player, False otherwise.
    """
    return all([board[p[0]][p[1]] == player for p in combination])


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
    horizontal = [((0, 0), (0, 1), (0, 2)), ((1, 0), (1, 1), (1, 2)), ((2, 0), (2, 1), (2, 2))]
    vertical = [((0, i), (1, i), (2, i)) for i in range(3)]
    diagonal = [((0, 0), (1, 1), (2, 2)), ((0, 2), (1, 1), (2, 0))]
    combos = horizontal + vertical + diagonal
    
    if any([_is_winning_combination(board, combo, player) for combo in combos]):
        return player
    

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
    if _check_winning_combinations(game["board"], game["player1"]):
        return game["player1"]
    elif _check_winning_combinations(game["board"], game["player2"]):
        return game["player2"]


def move(game, player, position):
    """
    Performs a player movement in the game. Must ensure all the pre requisites
    checks before the actual movement is done.
    After registering the movement it must check if the game is over.
    
    game is over -- exception InvalidMovement, 'Game is over'
    player out of turn -- exception InvalidMovement, '"O" moves next'
    position is invalid -- exception InvalidMovement, 'Position out of range.'
    position is occupied -- exception InvalidMovement, 'Position already taken.'
    
    change the square to player
    change game["next_turn"]
    check if game is over - if it is, change game["winner"], raise GameOver, 
    """
    if game['winner']:
        raise InvalidMovement('Game is over.')
    if game["next_turn"] != player:
        raise InvalidMovement('"%s" moves next' % game["next_turn"])
    if not _position_is_valid(position):
        raise InvalidMovement('Position out of range.')
    if not _position_is_empty_in_board(position, game["board"]):
        raise InvalidMovement("Position already taken.")
    
    game["board"][position[0]][position[1]] = player
    game["next_turn"] = game["player1"] if player == game["player2"] else game["player2"]
    
    winner = get_winner(game)
    if winner:
        game["winner"] = winner
        raise GameOver('"%s" wins!' % winner)
    
    tie = _board_is_full(game["board"])
    
    if tie:
        game["winner"] = "tie"
        raise GameOver('Game is tied!')
    

def get_board_as_string(game):
    """
    Returns a string representation of the game board in the current state.
    """
    
    squares = [square for row in game['board'] for square in row]
    return """
{}  |  {}  |  {}
--------------
{}  |  {}  |  {}
--------------
{}  |  {}  |  {}
""".format(*squares)


def get_next_turn(game):
    """
    Returns the player who plays next, or None if the game is already over.
    """
    if game['winner']:
        return None
    else:
        return game['next_turn']
