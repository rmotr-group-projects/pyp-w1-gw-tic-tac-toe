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
    x = int(position[0])
    y = int(position[1])
    
    if board[x][y] == '-':
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
    valid_positions = [(0,0), (0,1), (0,2),
                       (1,0), (1,1), (1,2),
                       (2,0), (2,1), (2,2)]
                       
    if isinstance(position, tuple) and len(position) == 2 and (position[0], position[1]) in valid_positions:
        return True
    return False


def _board_is_full(board):
    """
    Returns True if all positions in given board are occupied.

    :param board: Game board.
    """
    for item in board:
        for elem in item: 
            if elem == '-':
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
    for coord in combination:
        if board[coord[0]] [coord[1]] != player:
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
    if board[0][0] == player and board[0][1] == player and board[0][2] == player:
        return player
    elif board[1][0] == player and board[1][1] == player and board[1][2] == player:
        return player
    elif board[2][0] == player and board[2][1] == player and board[2][2] == player:
        return player
    elif board[0][0] == player and board[1][0] == player and board[2][0] == player:
        return player
    elif board[0][1] == player and board[1][1] == player and board[2][1] == player:
        return player
    elif board[0][2] == player and board[1][2] == player and board[2][2] == player:
        return player
    elif board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return player
    elif board[2][0] == player and board[1][1] == player and board[0][2] == player:
        return player
        
    return None


# public interface
def start_new_game(player1, player2):
    
    """
    Creates and returns a new game configuration.
    """
    return {
        'player1': player1,
        'player2': player2,
        'board': [
            ["-", "-", "-"],
            ["-", "-", "-"],
            ["-", "-", "-"],
        ],
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
    
    x = position[0]
    y = position[1]
    if player != game['next_turn']:
        raise InvalidMovement('"{}" moves next'.format(game['next_turn']))
    if _board_is_full(game['board']) or game['winner'] is not None:
        raise InvalidMovement('Game is over.')
    if player != game['next_turn']:
        raise InvalidMovement('Position already taken.')
    if not _position_is_valid(position):
        raise InvalidMovement('Position out of range.')
    if not _position_is_empty_in_board(position, game['board']):
        raise InvalidMovement('Position already taken.')
    if _board_is_full(game['board']):
        raise InvalidMovement('board is full')
    game['board'][x][y] = player
    game['next_turn'] = game['player1'] if game['next_turn'] == game['player2'] else game['player2']
    if _check_winning_combinations(game['board'], player):
        game['winner'] = player
        raise GameOver('"{}" wins!'.format(player))
    if _board_is_full(game['board']):
        raise GameOver('Game is tied!')
    
    
def get_board_as_string(game):
    """
    Returns a string representation of the game board in the current state.
    """
    # print (' | ').join(game['board'][0])
    # print    '---------'
    # print (' | ').join(game['board'][1])
    # print    '---------'
    # print (' | ').join(game['board'][2])
    
    game_str = ''
    game_str += '\n' + ('  |  ').join(game['board'][0]) + '\n--------------\n' + ('  |  ').join(game['board'][1]) + '\n--------------\n' + ('  |  ').join(game['board'][2]) + '\n'
    return game_str

def get_next_turn(game):
    """
    Returns the player who plays next, or None if the game is already over.
    """
    return game['next_turn']
