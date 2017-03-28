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

    # Make sure that...
    #    position is a tuple
    #    position's length is 2
    #    every value in the tuple is an int
    #    every int in the tuple is either 0, 1 or 2
    # if not, return False

    if not isinstance(position, tuple) \
            or len(position) != 2 \
            or not all(isinstance(x, int) for x in position) \
            or any(x for x in position if not 0 <= x <= 2):
        return False

    return True


def _board_is_full(board):
    """
    Returns True if all positions in given board are occupied.

    :param board: Game board.
    """

    # looks for "-" in every position in the board
    # returns False if it finds one
    for row in board:
        if any(column for column in row if column == "-"):
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

    """
    ### Code before refactoring into a comprehension list:

    for a_tuple in combination:

        # e.g. a_tuple = (0,0)
        # if board[0][0] != "X"
        if board[a_tuple[0]][a_tuple[1]] != player:

            return False
    """

    if any(a_tuple for a_tuple in combination if board[a_tuple[0]][a_tuple[1]] != player):
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
    winning_combinations = (
        ((0, 0), (0, 1), (0, 2)),
        ((1, 0), (1, 1), (1, 2)),
        ((2, 0), (2, 1), (2, 2)),
        ((0, 0), (1, 0), (2, 0)),
        ((0, 1), (1, 1), (2, 1)),
        ((0, 2), (1, 2), (2, 2)),
        ((0, 0), (1, 1), (2, 2)),
        ((0, 2), (1, 1), (2, 0))
    )

    if any(combination for combination in winning_combinations if _is_winning_combination(board, combination, player)):
        return player

    return None

# public interface
def start_new_game(player1, player2):
    """
    Creates and returns a new game configuration.
    """
    return {
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

    # Is the board full? Or do we already have a winner? Then game is over.
    if _board_is_full(game['board']) or game['winner'] != None:
        raise InvalidMovement('Game is over.')

    # if the next player is not the one who should make the move
    if not get_next_turn(game) == player:
        raise InvalidMovement('"' + str(get_next_turn(game)) + '" moves next.')

    # make sure the move is in a valid position
    if _position_is_valid(position) == False:
        raise InvalidMovement("Position out of range.")

    # make sure the move in an empty position
    if not _position_is_empty_in_board(position, game['board']):
        raise InvalidMovement("Position already taken.")


    # Everything seems fine. LET'S PLAY!

    # Put X or O in the position
    game['board'][position[0]][position[1]] = player

    # Do we have a winner?
    # game['winner'] = X, O, or None
    game['winner'] = _check_winning_combinations(game['board'], player)

    # If not None, then we raise the winner
    if game['winner'] != None:
        raise GameOver('"' + game['winner'] + '" wins!')

    # No winner? But is the board full now? Then the game is tied.
    elif _board_is_full(game['board']):
        raise GameOver('Game is tied!')

    # No winner? Game's not tied? Then game continues.
    # So let's put the next player in game['next_turn']
    else:
        game['next_turn'] = "X" if player == "O" else "O"


def get_board_as_string(game):
    """
    Returns a string representation of the game board in the current state.
    """
    str_board = "\n"  # every board starts with a blank line
    row = 0  # used to print the board

    # creates a board of 5 lines. 3 rows, 2 dashed.
    for line in range(1, 6):

        # every odd line
        if line % 2 != 0:

            # add a row to the string str_board
            str_board += "{}  |  {}  |  {}".format(game['board'][row][0], game['board'][row][1], game['board'][row][2])

            # increment the row
            row += 1

        # every even line
        else:
            str_board += "--------------"

        str_board += "\n"  # add line break at the end of every line

    return str_board


def get_next_turn(game):
    """
    Returns the player who plays next, or None if the game is already over.
    """
    return game['next_turn']
