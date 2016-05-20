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
    if not isinstance(position, tuple):
        return False
    if len(position) != 2:
        return False
    if position[0] < 0 or position[1] < 0:
        return False
    if position[0] > 2:
        return False
    if position[1] > 2:
        return False
    return True

def _board_is_full(board):
    """
    Returns True if all positions in given board are occupied.

    :param board: Game board.
    """
    for row in board:
        for position in row:
            if position == '-':
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
    for x, y in combination:
        if board[x][y] != player:
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
    combinations = [ [(0, 0), (0, 1), (0,2)],
                    [(1, 0), (1, 1), (1,2)],
                    [(2, 0), (2, 1), (2,2)],
                    [(0, 0), (1, 0), (2,0)],
                    [(0, 1), (1, 1), (2,1)],
                    [(0, 2), (1, 2), (2,2)],
                    [(0, 0), (1, 1), (2,2)],
                    [(0, 2), (1, 1), (2,0)],
        ]

    for combination in combinations:
        if _is_winning_combination(board, combination, player):
            return player
   
        
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
    if not _position_is_valid(position):
        raise InvalidMovement("Position out of range.")

    if _board_is_full(game['board']) or game['winner'] is not None:
        raise InvalidMovement("Game is over.")
        
    if game['next_turn'] != player:
        raise InvalidMovement('"{}" moves next'.format(game['next_turn']))
    
    if not _position_is_empty_in_board(position, game['board']):
        raise InvalidMovement("Position already taken.")
    
    
        
    # Make a move
    game['board'][position[0]][position[1]] = player
    if get_next_turn(game) == 'X':
        game['next_turn'] ='O'
    else:
        game['next_turn'] = 'X'
    
    
    result = _check_winning_combinations(game['board'], player)
    if result is not None:
        game['winner'] = player
        raise GameOver('"{}" wins!'.format(result))
    if _board_is_full(game['board']):     
        raise GameOver("Game is tied!")
    
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
    if _board_is_full(game['board']):
        return None
    else:
        return game['next_turn']