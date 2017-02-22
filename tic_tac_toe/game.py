from exceptions import *

# internal helpers
def _position_is_empty_in_board(position, board):
    """
    Checks if given position is empty ("-") in the board.

    :param position: Two-elements tuple representing a
                     position in the board. Example: (0, 1)
    :param board: Game board.

    Returns True if given position is empty, False otherwise.
    """
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
    if isinstance(position, tuple) and len(position) == 2 and 0 <= position[0] <= 2 and 0 <= position[1] <= 2:
        return True
    else:
        return False

def _board_is_full(board):
    """
    Returns True if all positions in given board are occupied.

    :param board: Game board.
    """
    for row in board:
        for space in row:
            if space == "-":
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
    # horizontal_combs = ()
    # for r in range(len(board)):
    #     for c in range(len(r)):
    #         horizontal_combs.append((r, c))
    
    combinations = (
        # horizontals
        ((0,0), (0,1), (0,2)),
        ((1,0), (1,1), (1,2)),
        ((2,0), (2,1), (2,2)),
        # verticals
        ((0,0), (1,0), (2,0)),
        ((0,1), (1,1), (2,1)),
        ((0,2), (1,2), (2,2)),
        # diagonals
        ((0,0), (1,1), (2,2)),
        ((2,0), (1,1), (0,2)),
    )
    
    for comb in combinations:
        if _is_winning_combination(board, comb, player):
            #game['winner'] = player
            return player
    
    return None

# public interface
def start_new_game(player1, player2):
    """
    Creates and returns a new game configuration.
    """
    return {
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
    if game['winner'] or _board_is_full(game['board']):
        raise InvalidMovement('Game is over.')
    if not _position_is_valid(position):
        raise InvalidMovement('Position out of range.')
    if not _position_is_empty_in_board(position, game['board']):
        raise InvalidMovement("Position already taken.")
    if player != get_next_turn(game):
        raise InvalidMovement('"' + game['next_turn'] + '"' + ' moves next.')
    
    game['board'][position[0]][position[1]] = player
    
    if _check_winning_combinations(game['board'], player):
        game['winner'] = player
        game['next_turn'] = None
        raise GameOver('"' + player +'"'+ ' wins!')
    elif _board_is_full(game['board']):
        game['next_turn'] = None
        raise GameOver('Game is tied!')
    else:
        if game['next_turn'] == game['player1']:
            game['next_turn'] = game['player2']
        else:
            game['next_turn'] = game['player1']


def get_board_as_string(game):
    """
    Returns a string representation of the game board in the current state.
    """
    
    row_1 = "\n{}  |  {}  |  {}\n".format(game['board'][0][0], game['board'][0][1], game['board'][0][2])
    row_2 = "--------------\n"
    row_3 = "{}  |  {}  |  {}\n".format(game['board'][1][0], game['board'][1][1], game['board'][1][2])
    row_4 = "--------------\n"
    row_5 = "{}  |  {}  |  {}\n".format(game['board'][2][0], game['board'][2][1], game['board'][2][2])
    
    board_string = (row_1+row_2+row_3+row_4+row_5)
    """
    {}  |  {}  |  {} \n
    -------------- \n
    {}  |  {}  |  {} \n
    -------------- \n
    {}  |  {}  |  {} \n
   .format(game['board'][0][0], game['board'][0][1], game['board'][0][2], game['board'][1][0], game['board'][1][1], game['board'][1][2], game['board'][2][0], game['board'][2][1], game['board'][2][2]  )
    """
    
    return board_string
    

    

def get_next_turn(game):
    """
    Returns the player who plays next, or None if the game is already over.
    """
    return game['next_turn']
   
    
