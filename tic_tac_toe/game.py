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
    if type(position) is not tuple:
        return False;
    if len(position) != 2:
        return False;
    if position[0] < 0 or position[0] > 2:
        return False
    if position[1] < 0 or position[1] > 2:
        return False
    return True


def _board_is_full(board):
    """
    Returns True if all positions in given board are occupied.

    :param board: Game board.
    """
    for i in range(3):
        for j in range(3):
            if _position_is_empty_in_board((i,j), board):
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
            return False;
    return True

def _is_played_played_this_position(board, position, player): #todo
    """
    Checks if player given has played in the givent position in the board
    :param board: Game board
    :param position: Tuple containing position
                     Example: (0,0), (2,1)

    Returns if given player played at that position. Returns True if so,
    otherwise returns False   
    """
    return board[position[0]][position[1]] == player

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
    col_one = ((0, 0), (1, 0), (2, 0))
    col_two = ((0, 1), (1, 1), (2, 1))
    col_three = ((0, 2), (1, 2), (2, 2))

    row_one = ((0, 0), (0, 1), (0, 2))
    row_two = ((1, 0), (1, 1), (1, 2))
    row_three = ((2, 0), (2, 1), (2, 2))

    diag_one= ((0, 0), (1, 1), (2, 2))
    diag_two= ((0, 2), (1, 1), (2, 0))

    rows = (row_one, row_two, row_three)
    cols = (col_one, col_two, col_three)
    diagonals = (diag_one, diag_two)

    winning_combinations = (rows, cols, diagonals)
    for tuples in winning_combinations:
        for combination in tuples:
            if _is_winning_combination(board, combination, player) ==  True:

                return player
    return None

def _get_row_strt(row):
    ans = ""
    two_spaces = "  "
    delimiter = "|" 
    ans += row[0] + two_spaces + delimiter;
    ans += two_spaces + row[1] + two_spaces + delimiter;
    ans += two_spaces + row[2]

    return ans

# public interface
def start_new_game(player1, player2):
    """
    Creates and returns a new game configuration.
    """
    game = {}
    game["player1"] = "X"
    game["player2"] = "O"
    empty_board_row = ["-", "-", "-"]
    empty_board = [empty_board_row.copy(), empty_board_row.copy(), empty_board_row.copy()]
    game["board"] = empty_board
    game["next_turn"] = "X"
    game["winner"]= None
    return game


def get_winner(game):
    """
    Returns the winner player if any, or None otherwise.
    """
    board = game["board"]
    players = ("X", "O")
    for player in players:
        if _check_winning_combinations(board, player):
            return player
    return None   


def move(game, player, position):
    """
    Performs a player movement in the game. Must ensure all the pre requisites
    checks before the actual movement is done.
    After registering the movement it must check if the game is over.
    """
    if _position_is_valid(position) == False:
        raise InvalidMovement("Position out of range.")
    board = game["board"]
    next = get_next_turn(game)

    if next is None:
        raise InvalidMovement("Game is over.")

    if _position_is_empty_in_board(position, board) == False:
        raise InvalidMovement("Position already taken.")
    if game["next_turn"] != player:
        raise InvalidMovement('"' + game["next_turn"] + '"' +" moves next")
    board = game["board"]
    board[position[0]][position[1]] = player # move
    next_player = "X"
    if game["next_turn"] == "X":
        next_player = "O"
    game["next_turn"] = next_player

    winner = get_winner(game)

    if winner is not None:
        #'"X" wins!'
        game["winner"] = winner
        raise GameOver('"' + winner + '"' +' wins!')
    next = get_next_turn(game)
    if next is None:
        raise GameOver("Game is tied!")

def get_board_as_string(game):
    """
    Returns a string representation of the game board in the current state.
    """
    board = game["board"]
    ans = "\n"
    number =0
    for row in board:
        ans += _get_row_strt(row) + "\n"
        if number != 2:
            ans+= "--------------"
            ans += "\n"
        number +=1

    return ans


def get_next_turn(game):
    """
    Returns the player who plays next, or None if the game is already over.
    """
    if get_winner(game) is not None:
        return None

    board = game["board"]
    for i in range(3):
        for j in range(3):
            if _position_is_empty_in_board((i, j), board):
                return game["next_turn"]
    return None
