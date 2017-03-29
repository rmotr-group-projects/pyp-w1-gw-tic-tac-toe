from tic_tac_toe.exceptions import GameOver, InvalidMovement

def _position_is_empty_in_board(position, board):
    """
    Checks if given position is empty ("-") in the board.

    :param position: Two-elements tuple representing a
                     position in the board. Example: (0, 1)
    :param board: Game board.

    Returns True if given position is empty, False otherwise.
    """
    return board[position[0]][position[1]] == '-'


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
    try:
        return (len(position) == 2 
                and all(isinstance(n, int) and -1 < n < 3 for n in position))
    except TypeError:
        return False


def _board_is_full(board):
    """
    Returns True if all positions in given board are occupied.

    :param board: Game board.
    """
    for position in board:
        if "-" in position:
            return False
    return True


def _is_winning_combination(combination, player):
    """
    Checks if all 3 positions in given combination are occupied by given player.

    :param board: Game board.
    :param combination: Tuple containing three position elements.
                        Example: ((0,0), (0,1), (0,2))

    Returns True of all three positions in the combination belongs to given
    player, False otherwise.
    """
    if all(mark if mark == player else False for mark in combination):
        return True
    return False
    

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
    for i in range(len(board)):
        if _is_winning_combination(board[i], player):
            return player
        elif _is_winning_combination([col[i] for col in board], player):
            return player
    if (_is_winning_combination(
        [board[i][i] for i in range(len(board))], player)
        or _is_winning_combination(
        [board[j][i] 
        for i,j in enumerate(range(len(board)-1,-1,-1))], player)):
            return player


# public interface
def start_new_game(player1, player2, board=None):
    """
    Creates and returns a new game configuration.
    """
    if not board:
        board = [
            ["-", "-", "-"],
            ["-", "-", "-"],
            ["-", "-", "-"]
            ]
    return {
        'player1': player1,
        'player2': player2,
        'board': board,
        'next_turn': player1,
        'winner': None,
        
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
    board = game['board']
    
    if _board_is_full(board) or game['winner']:
        raise InvalidMovement("Game is over.")
    elif player != game['next_turn']:
        raise InvalidMovement('"{}" moves next'.format(game['next_turn']))
    elif not _position_is_valid(position):
        raise InvalidMovement('Position out of range.')
    elif not _position_is_empty_in_board(position, board):
        raise InvalidMovement('Position already taken.')
    else:
        board[position[0]][position[1]] = player
        if _check_winning_combinations(board, player):
            game['winner'] = player
            raise GameOver('"{}" wins!'.format(player))
        elif _board_is_full(board):
            raise GameOver("Game is tied!")
        elif game['next_turn'] == game['player1']:
            game['next_turn'] = game['player2']
        else:
            game['next_turn'] = game['player1']
    


def get_board_as_string(game):
    """
    Returns a string representation of the game board in the current state.
    """
    board = game['board']
    board_str = ''
    for i in range(len(board)):
        board_str += ('\n' + ('{}  |  ' * (len(board)-1) + '{}') + '\n')
        if i < len(board)-1:
            board_str += '--------------'
    return board_str.format(*([board[i][j]
                              for i in range(len(board))
                              for j in range(len(board))]))

def get_next_turn(game):
    """
    Returns the player who plays next, or None if the game is already over.
    """
    return game['next_turn']
