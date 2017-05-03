from .exceptions import InvalidMovement, GameOver

# Public functions (game starter, basic checks, make a move and such).
def start_new_game(player1, player2):
    """
    Creates and returns a new game configuration.
    """
    
    game = {
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
    
    return game
    
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
"""
    
    return board_string.format(*([elem for row in game['board'] for elem in row]))

def get_winner(game):
    """
    Returns the winner player if any, or None otherwise.
    """
    
    return game['winner']

def move(game, player, position):
    board = game['board']

    #illegal moves section
    if game['winner'] or _board_is_full(board):
        raise InvalidMovement('Game is over.')
    
    if player != get_next_turn(game):
        raise InvalidMovement('"{}" moves next.'.format(game['next_turn']))
    
    if not _position_is_valid(position):
        raise InvalidMovement('Position out of range.')
    
    if not _position_is_empty_in_board(position, board):
        raise InvalidMovement('Position already taken.')
    
    # make move section
    board[position[0]][position[1]] = player  #using indices in tuple on the board positions
  
    winner = _check_winning_combinations(board, player)    # winner?; returns None if none
    
    if winner:    #record results section
        game['winner'] = winner
        game['next_turn'] = None
        raise GameOver('"{}" wins!'.format(winner))
    elif _board_is_full(board):    # board is full AND no winner...
        game['next_turn'] = None
        raise GameOver('Game is tied!')
    else:                                   #else, continue with the game marking the next turn
        game['next_turn'] = (game['player1'] if game['next_turn'] == game['player2'] 
                            else game['player2'])

def get_next_turn(game):
    """
    Returns the player who plays next, or None if the game is already over.
    """
    return game['next_turn']
    
# Helpers / Verifications
def _position_is_empty_in_board(position, board):
    """
    Checks if given position is empty ("-") in the board.

    :param position: Two-elements tuple representing a
                     position in the board. Example: (0, 1)
    :param board: Game board.

    Returns True if given position is empty, False otherwise.
    """
    return True if board[position[0]][position[1]] == "-" else False


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
    if isinstance(position, tuple) and len(position) == 2:
        if len(list(filter(lambda x: 0 <= x <= 2, position))) == len(position):
            return True
    return False


def _board_is_full(board):
    """
    Returns True if all positions in given board are occupied.

    :param board: Game board.
    """

    return all([False if cell == "-" else True for row in board for cell in row])


def _is_winning_combination(board, combination, player):
    """
    Checks if all 3 positions in given combination are occupied by given player.

    :param board: Game board.
    :param combination: Tuple containing three position elements.
                        Example: ((0,0), (0,1), (0,2))

    Returns True of all three positions in the combination belongs to given
    player, False otherwise.
    """

    # Loop through all positions in the combination given.
    for position in combination:
        # If current position isn't filled with the player's Symbol,
        # return false.
        if board[position[0]][position[1]] != player:
            return False
    # If there's no False return, then it checks as a True statement
    # and the player won the game.
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
        # Verticals
        ((0,0), (1,0), (2,0)),
        ((0,1), (1,1), (2,1)),
        ((0,2), (1,2), (2,2)),
        # Horizontal
        ((0,0), (0,1), (0,2)),
        ((1,0), (1,1), (1,2)),
        ((2,0), (2,1), (2,2)),
        # Diagonals
        ((0,0),(1,1),(2,2)),
        ((2,0),(1,1),(0,2)),
        )
    
    # Looping through combinations
    for combination in combinations:
        # Use winning combination helper to check if there's any combination 
        # in the board and return the player as a winner
        if _is_winning_combination(board, combination, player):
            return player
    return None
