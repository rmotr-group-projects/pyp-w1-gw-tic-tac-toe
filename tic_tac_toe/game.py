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
    # board as a list of 3 lists, with a char '-' representing empty position.
    # position is a tuple (x_coordinate, y_coordinate).
    row, column = position
    return board[row][column] == '-'


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
    # Check if two element tuple:
    if not isinstance(position, tuple):
        return False
    if not len(position) == 2:
        return False


    # Check if tuple values are valid for board
    for coordinate_axis in [0,1]:
        if position[coordinate_axis] not in list(range(0,3)):
            return False

    return True


def _board_is_full(board):
    """
    Returns True if all positions in given board are occupied.

    :param board: Game board.
    """
    for row in board:
        if '-' in row:
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
        row, column = position
        if board[row][column] != player:
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
    #Check if player has all three along a horizonal or vertical:
    for coordinate in range(0,3):
        if _is_winning_combination(board, ((coordinate,0), (coordinate,1), (coordinate,2)), player) \
            or _is_winning_combination(board, ((0,coordinate), (1,coordinate), (2,coordinate)), player):
                return player

    # Check if a player has either diagonal:
    if _is_winning_combination(board, ((0,0), (1,1), (2,2)), player) \
        or _is_winning_combination(board, ((0,2), (1,1), (2,0)), player):
            return player

    return None


# public interface
def start_new_game(player1, player2):
    """
    Creates and returns a new game configuration.
    """
    #board = [['-']*3]*3  # <---- Does not work???
    board = [['-','-','-'],['-','-','-'],['-','-','-']]
    defaultgame = {
        'player1': player1,
        'player2': player2,
        'board': board,
        'next_turn': 'X',
        'winner': None
    }
    return defaultgame


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
    
    # Check if board full.
    if (_board_is_full(game['board'])):
        raise InvalidMovement('Game is over.')
        
    # Check if there is a winner.
    if game['winner']:
        raise InvalidMovement('Game is over.')

    # Check that it is this player's turn.
    if player != game['next_turn']:
        raise InvalidMovement('"{}" moves next'.format(game['next_turn']))

    # Check if the position is valid.
    if not _position_is_valid(position):
        raise InvalidMovement('Position out of range.')

    # Check if position is take.
    if not _position_is_empty_in_board(position, game['board']):
        raise InvalidMovement('Position already taken.')

    # Execute player move.
    row, column = position
    game['board'][row][column] = player

    # Check if tie.
    if (_board_is_full(game['board'])):
        raise GameOver('Game is tied!')
        
    # Check if winner.
    if _check_winning_combinations(game['board'], player):
        game['winner'] = player
        raise GameOver('"{}" wins!'.format(player))

    # Update the next move.
    game['next_turn'] = game['player1'] if (player == game['player2']) else game['player2']


def get_board_as_string(game):
    """
    Returns a string representation of the game board in the current state.
    """
    board = game.get('board')
    row1 = '{}  |  {}  |  {}'.format(board[0][0], board[0][1], board[0][2])
    row2 = '{}  |  {}  |  {}'.format(board[1][0], board[1][1], board[1][2])
    row3 = '{}  |  {}  |  {}'.format(board[2][0], board[2][1], board[2][2])
    delimeter = '--------------'
    return '\n' + row1 + '\n' + delimeter + '\n' + row2 + '\n' + delimeter + '\n' + row3 + '\n'


def get_next_turn(game):
    """
    Returns the player who plays next, or None if the game is already over.
    """
    if (get_winner(game) is None) and (_board_is_full(game['board']) == False):
        return game['next_turn']
