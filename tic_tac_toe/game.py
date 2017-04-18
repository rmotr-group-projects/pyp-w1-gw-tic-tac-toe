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
    if (not isinstance(position, tuple) 
        or not (isinstance(position[0], int) and isinstance(position[1], int))
        or not len(position) == 2
        or not ((0 <= position[0] < 3) and (0 <= position[1] < 3))):
            
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
    vertical_positions = [[(y, x) for y in range(3)] for x in range(3)]
    horizontal_positions = [[(y, x) for x in range(3)] for y in range(3)]
    diagonal_positions = [[(i, i) for i in range(3)], [(2, 0), (1, 1), (0, 2)]]
    combinations = vertical_positions + diagonal_positions  + horizontal_positions
    
    for combination in combinations:
        if _is_winning_combination(board, combination, player):
            return player
    return None

# public interface
def start_new_game(player1, player2):
    """
    Creates and returns a new game configuration.
    
    """
    board = [["-" for _ in range(3)]for a in range(3)]
    return {
        'player1': player1,
        'player2': player2,
        'board': board,
        'next_turn': player1,
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
    
    if get_winner(game) or _board_is_full(game['board']):
       raise InvalidMovement("Game is over.")
    
    if not player == game['next_turn']:
        raise InvalidMovement('"{0}" moves next.'.format(game['next_turn']))
        
    if not _position_is_valid(position):
        raise InvalidMovement('Position out of range.')
        
    if not _position_is_empty_in_board(position, game['board']):
        raise InvalidMovement("Position already taken.")
        
        
    game['board'][position[0]][position[1]] = player
    
    if player == game['player1']:
        game['next_turn'] = game['player2']
    else:
        game['next_turn'] = game['player1']
    
    if _check_winning_combinations(game['board'], player):
        game['winner'] = player
        game['next_turn'] = None
        raise GameOver('"{0}" wins!'.format(game['winner']))
        
    if _board_is_full(game['board']):
        game['next_turn'] = None
        raise GameOver('Game is tied!')


def get_board_as_string(game):
    """
    Returns a string representation of the game board in the current state.
    """
    rows = ["{0}  |  {1}  |  {2}\n".format(row[0], row[1], row[2]) for row in game['board']]
    return '\n' + '--------------\n'.join(rows)



def get_next_turn(game):
    """
    Returns the player who plays next, or None if the game is already over.
    """

    return game['next_turn']
