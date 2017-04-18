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
    return isinstance(position, tuple) and len(position) == 2 and 0 <= position[0] <= 2 and 0 <= position[1] <= 2


def _board_is_full(board):
    """
    Returns True if all positions in given board are occupied.

    :param board: Game board.
    """
    for elem in board:
        for val in elem:
            if "-" in val:
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
    winning_combinations = [
        # Horizontal - top
        ((0,0),(0,1),(0,2)),

        # Horizontal - middle
        ((1,0),(1,1),(1,2)),

        # Horizontal - bottom
        ((2,0),(2,1),(2,2)),

        # Vertical - left
        ((0,0),(1,0),(2,0)),

        # Vertical - middle
        ((0,1),(1,1),(2,1)),

        # Vertical - right
        ((0,2),(1,2),(2,2)),

        # Diagonal - forward
        ((0,2),(1,1),(2,0)),

        # Diagonal - backward
        ((0,0),(1,1),(2,2)),
    ]

    for combination in winning_combinations:
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
    
    if game['winner'] == None:
        return None
    else:
        return game['winner']


def move(game, player, position):
    """
    Performs a player movement in the game. Must ensure all the pre requisites
    checks before the actual movement is done.
    After registering the movement it must check if the game is over.
    """
    # Game over check
    if game['next_turn'] is None:
        raise InvalidMovement("Game is over.")
    # Position out of range check
    if not _position_is_valid(position):
        raise InvalidMovement('Position out of range.')
    # Position already taken check
    if not _position_is_empty_in_board(position, game['board']):
        raise InvalidMovement('Position already taken.')
    # Player moves twice check
    if not player == game['next_turn']:
        raise InvalidMovement('"' + game['next_turn'] +'" moves next')
    
    # Move is valid, set value in board
    game['board'][position[0]][position[1]] = player
    
    # Check if there's a winning combination
    if _check_winning_combinations(game['board'], player):
        game['winner'] = player
        game['next_turn'] = None
        raise GameOver('"' + player + '" wins!')
    
    # Now that move has been played, check if board is full now
    if _board_is_full(game['board']):
        game['next_turn'] = None
        raise GameOver("Game is tied!")

    # Change player
    if game['player1'] == player:
        game['next_turn'] = game['player2']
    elif game['player2'] == player:
        game['next_turn'] = game['player1']


def get_board_as_string(board):
    """
    Returns a string representation of the game board in the current state.
    """
    return "\n" + "\n--------------\n".join(["  |  ".join(row) for row in board["board"]]) + "\n"


def get_next_turn(game):
    """
    Returns the player who plays next, or None if the game is already over.
    """
    if _board_is_full(game['board']):
        return None
    else:
        return game['next_turn']
