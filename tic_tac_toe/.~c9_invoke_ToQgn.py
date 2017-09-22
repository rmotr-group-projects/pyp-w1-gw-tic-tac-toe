# internal helpers
def _position_is_empty_in_board(position, board):
    """
    Checks if given position is empty ("-") in the board.

    :param position: Two-elements tuple representing a
                     position in the board. Example: (0, 1)
    :param board: Game board.

    Returns True if given position is empty, False otherwise.
    """
    for x, y in position:
        row = x
        column = y
    count_rows = 0
    count_columns = 0
    for rows in board:
        if count_rows == row:
            for columns in board:
                if count_columns == column:
                    if columns == '-':
                        return True
                    else: return False
                count_columns += 1
        count_rows += 1
        
        
    if board[position[0]][position[1]] == '-':


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
        if (position[0] and position[1]) in range(3):
            return True
        return False


def _board_is_full(board):
    """
    Returns True if all positions in given board are occupied.

    :param board: Game board.
    """
    pass


def _is_winning_combination(board, combination, player):
    """
    Checks if all 3 positions in given combination are occupied by given player.

    :param board: Game board.
    :param combination: Tuple containing three position elements.
                        Example: ((0,0), (0,1), (0,2))

    Returns True of all three positions in the combination belongs to given
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
    pass


# public interface
def start_new_game(player1, player2):
    """
    Creates and returns a new game configuration.
    """
    pass


def get_winner(game):
    """
    Returns the winner player if any, or None otherwise.
    """
    pass 

def move(game, player, position):
    """
    Performs a player movement in the game. Must ensure all the pre requisites
    checks before the actual movement is done.
    After registering the movement it must check if the game is over.
    """
    pass


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
""".format(*[mark for val in game['board'] for mark in val])
    return board_string


def get_next_turn(game):
    """
    Returns the player who plays next, or None if the game is already over.
    """
    pass
