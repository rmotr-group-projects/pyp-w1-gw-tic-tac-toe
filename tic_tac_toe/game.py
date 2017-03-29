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
    i = position[0]
    j = position[1]
    return board[i][j] == "-"


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
    if not isinstance(position, tuple): return False
    elif not len(position) == 2: return False
    elif not all([x >= 0 and x <= 2 for x in position]): return False
    
    return True


def _board_is_full(board):
    """
    Returns True if all positions in given board are occupied.

    :param board: Game board.
    """
    empty_pos = all(["-" not in i for i in board])  # [ True if x < 1  else False for x in numbers ]
    return empty_pos

def _is_winning_combination(board, combination, player):
    """
    Checks if all 3 positions in given combination are occupied by given player.

    :param board: Game board.
    :param combination: Tuple containing three position elements.
                        Example: ((0,0), (0,1), (0,2))

    Returns True of all three positions in the combination belongs to given
    player, False otherwise.
    """
    # return all([ for position in combination])
    
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
    winners = [
        ((0,0), (0,1), (0,2)),
        ((1,0), (1,1), (1,2)),
        ((2,0), (2,1), (2,2)),
        ((0,0), (1,0), (2,0)),
        ((0,1), (1,1), (2,1)),
        ((0,2), (1,2), (2,2)),
        ((0,0), (1,1), (2,2)),
        ((2,0), (1,1), (0,2)),
    ]
    
    for winner in winners:
        if _is_winning_combination(board, winner, player):
            return player
            


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
    if not _position_is_valid(position): 
        raise InvalidMovement('Position out of range.')
    if game['winner'] or _board_is_full(game['board']): #game is over
        raise InvalidMovement('Game is over.')    
    if not _position_is_empty_in_board(position, game['board']):
        raise InvalidMovement('Position already taken.')
    if not player == game['next_turn']:
        raise InvalidMovement('"%s" moves next'%(game['next_turn']))
    
    
    i = position[0]
    j = position[1]
    game['board'][i][j] = player
    
    if player == game['player1']:
        game['next_turn'] = game['player2']
    else:
        game['next_turn'] = game['player1']
    
    if _check_winning_combinations(game['board'], player):
        game['winner'] = player
        raise GameOver('"%s" wins!'%(player))
    if _board_is_full(game['board']): #game is tied
        raise GameOver('Game is tied!')

def get_board_as_string(game):
    """
    Returns a string representation of the game board in the current state.
    """
    
    ret = []
    dashes = "--------------\n"
    for row in game['board']:
        first = row[0]
        second = row[1]
        third = row[2]
        row_str = "%(first)s  |  %(second)s  |  %(third)s\n"%{'first': first, 'second': second, 'third': third}
        ret.append(row_str)
    return "\n" + dashes.join(ret)


def get_next_turn(game):
    """
    Returns the player who plays next, or None if the game is already over.
    """
    return game['next_turn']
