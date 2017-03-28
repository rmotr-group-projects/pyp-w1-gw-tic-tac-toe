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
    row,col = position
    return board[row][col] == '-'

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
    return isinstance(position,tuple)\
        and len(position) == 2\
        and 0 <= position[0] <= 2\
        and 0 <= position[1] <= 2


def _board_is_full(board):
    """
    Returns True if all positions in given board are occupied.

    :param board: Game board.
    """
    for row in board:
        for space in row:
            if space == '-':
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
    return all(board[row][col] == player for row,col in combination)


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
    for row in range(3):
        if _is_winning_combination(board, ((row,col) for col in range(3)), player):
            return player
    for col in range(3):
        if _is_winning_combination(board, ((row,col) for row in range(3)), player):
            return player
    if _is_winning_combination(board, ((d,d) for d in range(3)), player):
        return player
    if _is_winning_combination(board, ((d,2-d) for d in range(3)), player):
        return player
    else:
        return None
    


# public interface
def start_new_game(player1, player2):
    """
    Creates and returns a new game configuration.
    """
    game = {'player1':player1,
            'player2':player2,
            'board':[['-']*3 for i in range(3)],
            'next_turn':player1,
            'winner':None}
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
    next_turn = game['next_turn']
    if next_turn != player:
        raise InvalidMovement('"{}" moves next.'.format(next_turn))
    if game['winner'] or _board_is_full(board):
        raise InvalidMovement('Game is over.')
    if not _position_is_valid(position):
        raise InvalidMovement("Position out of range.")
    if not _position_is_empty_in_board(position, board):
        raise InvalidMovement("Position already taken.")



    row, col = position
    board[row][col] = player
    p1 = game['player1']
    p2 = game['player2']
    game['next_turn'] = p1 if player == p2 else p2
    
    if _check_winning_combinations(board, player):
        game['winner'] = player
        raise GameOver('"{}" wins!'.format(player))
    if _board_is_full(board):
        raise GameOver('Game is tied!')
    
def get_board_as_string(game):
    """
    Returns a string representation of the game board in the current state.
    """
    
    row_strings = ['\n{r[0]}  |  {r[1]}  |  {r[2]}\n'.format(r=row) for row in game['board']]
    return "--------------".join(row_strings)


def get_next_turn(game):
    """
    Returns the player who plays next, or None if the game is already over.
    """
    return game['next_turn']
