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
    return True if board[int(position[0])][int(position[1])] == "-" else False

def _position_is_valid(position):
    """
    Checks if given position is a valid. To consider a position as valid, it
    must be a two-elements tuple, containing values from 0 to 2.
    Examples of valid positions: (0,0), (1,0)
    Examples of invalid positions: (0,0,1), (9,8), False

    :param position: Two-elements tuple representing a
                     position in the board. Example: (2, 2)

    Returns True if given position is valid, False otherwiseself.
    """
    return (True if isinstance(position, tuple) and
            #check length of tuple
            len(position) == 2 and 
            #check height
            position[0] in range(3) and 
            #check width
            position[1] in range(3)
            else False)


def _board_is_full(board):
    """
    Returns True if all positions in given board are occupied.

    :param board: Game board.
    """
    for row in board:
        for space in row:
            if space == "-": 
                return False 
            else:
                continue 

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
        # check if mark is not associated with player, if true return false
        if board[int(position[0])][int(position[1])] != player:
            return False
    return True


def _check_winning_combinations(board, player):
    
    """
    There are 8 possible combinations (3 horizontals, 3, verticals and 2 diagonals)
    to win the Tic-tac-toe game.
    This helper loops through all these combinations and checks if any of them
    belongs to the given player.

    :param board: Game board.
    :param player: One of the two playing players.

    Returns the player (winner) of any of the winning combinations is completed
    by given player, or None otherwise.
    """
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
        ((2,0), (1,1), (0,2))
    )
    for combo in combinations:
        if _is_winning_combination(board, combo, player):
            return player
    return None
    


# public interface
def start_new_game(player1, player2):
    
    return {
        'player1': player1,
        'player2': player2 ,
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
    return game["winner"]


def move(game, player, position):
    
    board = game['board']
    # If the game already has a winner of the board is full
    # there's nothing else to see. We raise an InvalidMovement exception
    # We rely on _board_is_full here.
    if game['winner'] or _board_is_full(board):
        raise InvalidMovement('Game is over.')
    
    # If the player attempting to make the move is not
    # the allowed one, we raise another exception.
    # We use get_next_turn here.
    if player != get_next_turn(game):
        raise InvalidMovement('"{}" moves next.'.format(game['next_turn']))
    
    # If the position that the user is trying to move is not valid
    # we raise another exception.
    # We rely on the _position_is_valid function
    if not _position_is_valid(position):
        raise InvalidMovement('Position out of range.')
    
    # If the position is already full (someone perform a previous
    # move on that position) we raise another exception.
    # We use the _position_is_empty_in_board function.
    if not _position_is_empty_in_board(position, board):
        raise InvalidMovement('Position already taken.')
        
    # IMPORTANT POINT
    # Up to this point we've checked all the ILLEGAL moves.
    # From now on everything else is valid.
    
    # The first thing we do is we make the actual move.
    # We mark the position with the player.
    board[position[0]][position[1]] = player
    
    # We then check to see if that last move, made
    # some player to win.
    winner = _check_winning_combinations(board, player)
    
    # If the movement resulted in a winner we do some
    # bookeeping tasks.
    # If we didn't produce a winner, but we filled the whole board
    #we raise the GameOver exception with a "tied game".
    # Or in any other case (final _else_), we just
    #swap the next player to keep the game going.
    if winner:
        game['winner'] = winner
        game['next_turn'] = None
        raise GameOver('"{}" wins!'.format(winner))
    elif _board_is_full(board):
        game['next_turn'] = None
        raise GameOver('Game is tied!'.format(winner))
    else:
        game['next_turn'] = game['player1'] if game['next_turn'] == game['player2'] else game['player2']  
    
    """
    Performs a player movement in the game. Must ensure all the pre requisites
    checks before the actual movement is done.
    After registering the movement it must check if the game is over.
    """
    pass


def get_board_as_string(game):
    """
    Returns a string representation of the game board in the current state.
    """
    board_str =  """
{}  |  {}  |  {}
--------------
{}  |  {}  |  {}
--------------
{}  |  {}  |  {}
"""
    return board_str.format(game["board"][0][0], game["board"][0][1],game["board"][0][2],game["board"][1][0],game["board"][1][1],game["board"][1][2],game["board"][2][0],game["board"][2][1],game["board"][2][2])
    # "{name} is being {emotion}"".format(d) d = {'name': 'Yatri', 'emotion': 'funny'}


def get_next_turn(game):
    """
    Returns the player who plays next, or None if the game is already over.
    """
    return game["next_turn"]