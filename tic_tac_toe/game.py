# internal helpers
def _position_is_empty_in_board(position, board):
    """
    Checks if given position is empty ("-") in the board.

    :param position: Two-elements tuple representing a
                     position in the board. Example: (0, 1)
    :param board: Game board.

    Returns True if given position is empty, False otherwise.
    """
    x = int(position[0])
    y = int(position[1])
    for row in board:
        for tile in row:
            if board[x][y] == "-":
                return True
            else:
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
    if position in ((0,0), (0,1), (0,2), (1,0), (1,1), (1,2), (2,0), (2,1), (2,2)):
        return True
    else:
        return False

def _board_is_full(board):
    """
    Returns True if all positions in given board are occupied.

    :param board: Game board.
    """
    for row in board:
        for tile in row:
            if _position_is_empty_in_board(tile, row):
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
    
    """
    for player in game:
        if board == [
            ["X", "O", "O"],
            ["O", "X", "X"],
            ["O", "O", "X"],
        ]: or == [
            ["O", "O", "X"],
            ["O", "X", "X"],
            ["X", "O", "O"],
        ] or == [
            ["X", "X", "X"],
            ["X", "O", "O"],
            ["O", "O", "X"],
        ] or == [
            ["X", "O", "O"],
            ["X", "X", "X"],
            ["O", "O", "X"],
        ] or == [
            ["X", "O", "O"],
            ["O", "O", "X"],
            ["X", "X", "X"],
        ] or == [
            ["X", "O", "X"],
            ["O", "O", "X"],
            ["O", "X", "X"],
        ] or == [
            ["X", "X", "O"],
            ["O", "X", "O"],
            ["O", "X", "X"],
        ] or == [
            ["X", "X", "O"],
            ["X", "O", "O"],
            ["X", "O", "X"],
        ]:
            return player
        elif board == [
            ["O", "X", "X"],
            ["X", "O", "O"],
            ["X", "X", "O"],
        ] or == [
            ["X", "X", "O"],
            ["X", "O", "O"],
            ["O", "X", "X"],
        ] or == [
            ["O", "O", "O"],
            ["O", "X", "X"],
            ["X", "X", "O"],
        ] or == [
            ["O", "X", "X"],
            ["O", "O", "O"],
            ["X", "X", "O"],
        ] or == [
            ["O", "X", "X"],
            ["X", "X", "O"],
            ["O", "O", "O"],
        ] or == [
            ["O", "X", "O"],
            ["X", "X", "O"],
            ["X", "O", "O"],
        ] or == board = [
            ["O", "O", "X"],
            ["X", "O", "X"],
            ["X", "O", "O"],
        ]
        
    """    
        
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
    'next_turn': "X",
    'winner': None}
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
    board = game['board']
    x = int(position[0])
    y = int(position[1])
    
    for row in board:
        for tile in row:
            if _position_is_empty_in_board(position, board):
                if _position_is_valid(position):
                    board[x][y] = player

def get_board_as_string(game):
    """
    Returns a string representation of the game board in the current state.
    """
    board = game['board']
    return """
{}  |  {}  |  {}
--------------
{}  |  {}  |  {}
--------------
{}  |  {}  |  {}
""".format(board[0][0], board[0][1], board[0][2], board[1][0], board[1][1], board[1][2], board[2][0], board[2][1], board[2][2])



def get_next_turn(game):
    """
    Returns the player who plays next, or None if the game is already over.
    """
    if game['next turn'] == 'X':
        return 'X'

    if game['next turn'] == 'Y':
        return 'Y'
        