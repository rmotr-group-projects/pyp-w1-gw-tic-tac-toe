from exceptions import InvalidMovement, GameOver


# internal helpers
def _position_is_empty_in_board(position, board):
    """
    Checks if given position is empty ("-") in the board.

    :param position: Two-elements tuple representing a
                     position in the board. Example: (0, 1)
    :param board: Game board.

    Returns True if given position is empty, False otherwise.
    """
    if (board[position[0]][position[1]] == '-'):
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
    if (type(position) is not tuple or len(position) != 2 or 
        not 0 <= position[0] <= 2 or not 0 <= position[1] <= 2):
        return False
    else:
        return True


def _board_is_full(board):
    """
    Returns True if all positions in given board are occupied.

    :param board: Game board.
    """
    for row in board:
        for cell in row:
            if cell == '-':
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
    if False in [board[i][j] == player for i,j in combination]:
        return False
    else:
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
    for x in range(3):
        if _is_winning_combination(board, [(x,0), (x,1), (x,2)], player):
            return player
        if _is_winning_combination(board, [(0,x), (1,x), (2,x)], player):
            return player
    if _is_winning_combination(board, [(0,0), (1,1), (2,2)], player):
        return player
    if _is_winning_combination(board, [(2,0), (1,1), (0,2)], player):
        return player


# public interface
def start_new_game(player1, player2):
    """
    Creates and returns a new game configuration.
    """
    # p1 = input("player1 = ")
    # p2 = input("player2 = ")
    game_configuration = {
        'player1' : player1,
        'player2' : player2,
        'board' : [
            ["-", "-", "-"],
            ["-", "-", "-"],
            ["-", "-", "-"]
        ],
        'next_turn' : player1,
        'winner' : None
    }
    return game_configuration


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
    current_player = get_next_turn(game)
    board = game['board']
    
    if (game['winner'] != None or _board_is_full(board)):
        raise InvalidMovement('Game is over.')
    if (player != current_player): 
        raise InvalidMovement('"' + current_player + '" moves next.')
    if not _position_is_valid(position):
        raise InvalidMovement('Position out of range.')
    if not _position_is_empty_in_board(position, board):
        raise InvalidMovement('Position already taken.')
    board[position[0]][position[1]] = current_player
    game['winner'] = _check_winning_combinations(board, player)
    if game['winner']:
        raise GameOver('"' + current_player + '" wins!')
    elif _board_is_full(board):
        raise GameOver('Game is tied!')
    switch_turn(game)
    
    

def get_board_as_string(game):
    """
    Returns a string representation of the game board in the current state.
    """
    board = game['board']
    board_string = '\n'
    for i, row in enumerate(board):
        if i > 0:
            board_string += '\n--------------\n'
        for j, cell in enumerate(row):
            if j > 0:
                board_string += '  |  ' 
            board_string += board[i][j]
    board_string += '\n'
    return board_string
        

def get_next_turn(game):
    """
    Returns the player who plays next, or None if the game is already over.
    """
    return game['next_turn']
    
    
def switch_turn(game):
    if game['next_turn'] is game['player1']:
        game['next_turn'] = game['player2']
    else:
        game['next_turn'] = game['player1']
    
