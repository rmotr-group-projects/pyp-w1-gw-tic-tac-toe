from tic_tac_toe.exceptions import InvalidMovement, GameOver

def _position_is_empty_in_board(position, board):
    """
    Checks if given position is empty ("-") in the board.

    :param position: Two-elements tuple representing a
                     position in the board. Example: (0, 1)
    :param board: Game board.

    Returns True if given position is empty, False otherwise.
    """
    x, y = position
    return board[x][y] == '-'


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
    if not isinstance(position, tuple):
        return False
    
    if len(position) != 2:
        return False
    
    x, y = position
    return 0 <= x <= 2 and 0 <= y <= 2


def _board_is_full(board):
    """
    Returns True if all positions in given board are occupied.

    :param board: Game board.
    """
    return '-' not in [y for x in board for y in x]


def _is_winning_combination(board, combination, player):
    """
    Checks if all 3 positions in given combination are occupied by given player.

    :param board: Game board.
    :param combination: Tuple containing three position elements.
                        Example: ((0,0), (0,1), (0,2))

    Returns True of all three positions in the combination belongs to given
    player, False otherwise.
    """
    a, b, c = combination
    (n1, n2), (n3, n4), (n5, n6) = a, b, c
    return board[n1][n2] == board[n3][n4] == board[n5][n6] == player
    


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
    winning_position = board[0][0] == board[0][1] == board[0][2] != '-' or \
        board[1][0] == board[1][1] == board[1][2] != '-' or \
        board[2][0] == board[2][1] == board[2][2] != '-' or \
        board[0][0] == board[1][0] == board[2][0] != '-' or \
        board[0][1] == board[1][1] == board[2][1] != '-' or \
        board[0][2] == board[1][2] == board[2][2] != '-' or \
        board[0][0] == board[1][1] == board[2][2] != '-' or \
        board[0][2] == board[1][1] == board[2][0] != '-'
        
    if winning_position:
        return player
    else:
        return None


# public interface
def start_new_game(player1, player2):
    """
    Creates and returns a new game configuration.
    """
    board = [
        ["-", "-", "-"],
        ["-", "-", "-"],
        ["-", "-", "-"],
    ]
    
    return {'player1': player1, 'player2': player2, 'board': board, 'next_turn': player1, 'winner': None}

def get_winner(game):
    """
    Returns the winner player if any, or None otherwise.
    """
    return game.get("winner", None)

def move(game, player, position):
    """
    Performs a player movement in the game. Must ensure all the pre requisites
    checks before the actual movement is done.
    After registering the movement it must check if the game is over.
    """
    if not _position_is_valid(position):
        raise InvalidMovement("Position out of range.")
    
    if not _position_is_empty_in_board(position, game['board']):
        if _board_is_full(game['board']):
            raise InvalidMovement("Game is over.")
        raise InvalidMovement("Position already taken.")
        
        
    if game['winner'] != None:
        raise InvalidMovement("Game is over.")
        
    if game['next_turn'] != player:
        raise InvalidMovement('"{}" moves next'.format(game['next_turn']))
        
    x, y = position
    game['board'][x][y] = player
    winner = _check_winning_combinations(game['board'], player)
    game['winner'] = winner
    if get_winner(game) != None:
        raise GameOver('"{}" wins!'.format(player))
    
    if _board_is_full(game['board']):
        raise GameOver("Game is tied!")
        
    if player == "X":
        game['next_turn'] = "O"
    else:
        game['next_turn'] = "X"

def get_board_as_string(game):
    """
    Returns a string representation of the game board in the current state.
    """
    p1, p2, p3 = game['board'][0]
    p4, p5, p6 = game['board'][1]
    p7, p8, p9 = game['board'][2]
    row1 = '\n' + '{}  |  {}  |  {}'.format(p1, p2, p3) + '\n'
    row2 = '{}  |  {}  |  {}'.format(p4, p5, p6) + '\n'
    row3 = '{}  |  {}  |  {}'.format(p7, p8, p9) + '\n'
    div = '-'*14 + '\n'
    str_board = row1 + div + row2 + div + row3
    return str_board

def get_next_turn(game):
    """
    Returns the player who plays next, or None if the game is already over.
    """
    return game['next_turn']
    