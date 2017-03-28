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
    import ipdb
    if board[position[0]][position[1]] == "-":
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
    
    # Make sure position is a tuple
    if not type(position) == tuple:
        return False
    
    # Ensure length = 2 and each entry is between 0 and 2
    elif len(list(position)) != 2:
        return False
        
    elif position[0] < 0 or position[0] > 2 or position[1] < 0 or position[1] > 2:
        return False
        
    else:
        return True

def _board_is_full(board):
    """
    Returns True if all positions in given board are occupied.

    :param board: Game board.
    """
    board_full = all([True if (c != '-') else False for r in board for c in r])
    if board_full:
        return True
    else:
        return False

def _is_winning_combination(board, combination, player):
    """
    Checks if all 3 positions in given combination are occupied by given player.

    :param board: Game board.
    :param combination: Tuple containing three position elements.
                        Example: ((0,0), (0,1), (0,2))

    Returns True of all three positions in the combination belongs to given
    player, False otherwise.
    """
    win_check = lambda combo, board: True if board[combo[0]][combo[1]] == player else False
    return all([win_check(combo, board) for combo in combination])    # return [lamba combo, board: True if board[combo[0]][combo[1]] == player else False]

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
            #Three horizontals (first index all equal)
            ((0, 0), (0, 1), (0, 2)),
            ((1, 0), (1, 1), (1, 2)),
            ((2, 0), (2, 1), (2, 2)),
            #Three verticals (second index all equal)
            ((0, 0), (1, 0), (2, 0)),
            ((0, 1), (1, 1), (2, 1)),
            ((0, 2), (1, 2), (2, 2)),
            #Two diagonals
            ((0, 0), (1, 1), (2, 2)),
            ((0, 2), (1, 1), (2, 0))
        )
    
    for combination in winning_combinations:
        if _is_winning_combination(board, combination, player):
            return player
    
    return None
    
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
        'next_turn': player1,
        'winner': None
    }
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
    # Do validity checks first---------------------
    
    # If there is a winner or tie(board=full), raise error
    if get_winner(game) or _board_is_full(game['board']):
        raise InvalidMovement('Game is over.')
    
    # Check if position is valid
    if not _position_is_valid(position):
        raise InvalidMovement("Position out of range.")
    
    # Check if position is taken
    if not  _position_is_empty_in_board(position, game['board']):
        raise InvalidMovement("Position already taken.")
        
    # Check if correct player made move
    if game['next_turn'] != player:
        raise InvalidMovement('"{}" moves next'.format(game['next_turn']))
    
    # Make Move---------------------
    game['board'][position[0]][position[1]] = player
    
    #Update Winner status
    game['winner'] = _check_winning_combinations(game['board'], player)
    
    # Do post-move checks ---------------------
    # Check if there is a winner
    winner = get_winner(game)
    if winner:
        raise GameOver('"{}" wins!'.format(winner))
    
    # Check if game is tied
    if _board_is_full(game['board']):
        raise GameOver("GameOver: Game is tied!")
    
    # Update next_turn
    if player == game['player1']:
        game['next_turn'] = game['player2']
    else:
        game['next_turn'] = game['player1']
    

def get_board_as_string(game):
    """
    Returns a string representation of the game board in the current state.
    """
    #pass
    board = game['board']
    
    board_str = '\n'
    for row in board:
    		board_str += row[0] + '  |  ' + row[1] + '  |  ' + row[2] + '\n--------------\n'
    
    return board_str[:-15]

def get_next_turn(game):
    """
    Returns the player who plays next, or None if the game is already over.
    """
    return game['next_turn']
