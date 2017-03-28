from .exceptions import *


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
    if isinstance(position, tuple):
        check_pos = [isinstance(pos, int) for pos in position]
        if len(position) == 2 and check_pos[0] and check_pos[1] and position[0] in range(3) and position[1] in range(3):
            return True
        return False
    return False


def _board_is_full(board):
    """
    Returns True if all positions in given board are occupied.

    :param board: Game board.
    """
    for i in range(3):
        for j in range(3):
            if board[i][j] == "-":
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
    if board[combination[0]] == player and board[combination[1]] == player and board[combination[2]] == player:
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
    
    def check_diags(board, player):
        diag1=[board[i][i] for i in range(3)]
        diag2 = []
        diag2.append(board[0][2])
        diag2.append(board[1][1])
        diag2.append(board[2][0])
        if diag1.count(player) == 3 or diag2.count(player) == 3:
            return player
        return None
    
    
    def check_rows(board, player):
        rows = [board[i][j] for i in range(3) for j in range(3)]
        if rows[:3].count(player) == 3 or rows[3:6].count(player) == 3 or rows[6:9].count(player) == 3:
            return player
        return None
        
    def check_columns(board, player):
        cols = [board[j][i] for i in range(3) for j in range(3)]
        if cols[:3].count(player) == 3 or cols[3:6].count(player) == 3 or cols[6:9].count(player) == 3:
            return player
        return None
    
    if check_diags(board, player):
        return player
    elif check_rows(board, player):
        return player
    elif check_columns(board, player):
        return player
    else:
        return None
    
# public interface
def start_new_game(player1, player2):
    """
    Creates and returns a new game configuration.
    """
    
    return {
        'player1':player1,
        'player2':player2,
        'board': [
            ["-", "-", "-"],
            ["-", "-", "-"],
            ["-", "-", "-"]
        ],
        'next_turn': "X",
        'winner': None
        }


def get_winner(game):
    """
    Returns the winner player if any, or None otherwise.
    """
    if _check_winning_combinations(game['board'], game['player1']):
        return game['player1']
    elif _check_winning_combinations(game['board'], game['player2']):
        return game['player2']
    else:
        return None


def move(game, player, position):
    """
    Performs a player movement in the game. Must ensure all the pre requisites
    checks before the actual movement is done.
    After registering the movement it must check if the game is over.
    """
    def game_tied(game, player):
        if _board_is_full(game['board']) and get_winner(game) is None:
            return True
        return False
    
    def game_over(game, player):
        if game_tied(game, player) or get_winner(game):
            return True
        return False
    
    if game_over(game, player):
        raise InvalidMovement("Game is over.")
    if _position_is_valid(position) is False:
        raise InvalidMovement("Position out of range.")
    if player is not game['next_turn']:
        raise InvalidMovement("\"{}\" moves next.".format(game['next_turn']))
    elif game['board'][position[0]][position[1]] != "-":
        raise InvalidMovement("Position already taken.")
    
    game['board'][position[0]][position[1]] = player
    
    if get_winner(game):
        raise GameOver("\"{}\" wins!".format(get_winner(game)))
    elif game_tied(game, player):
        raise GameOver("Game is tied!")
        
    
    if player == "X":
        game['next_turn'] = "O"
    elif player == "O":
        game['next_turn'] = "X"
    

def get_board_as_string(game):
    """
    Returns a string representation of the game board in the current state.
    """
    board_form = '\n{}  |  {}  |  {}\n--------------\n{}  |  {}  |  {}\n--------------\n{}  |  {}  |  {}\n'.format(game['board'][0][0], game['board'][0][1], game['board'][0][2], game['board'][1][0],
    game['board'][1][1], game['board'][1][2], game['board'][2][0], game['board'][2][1], game['board'][2][2])
    return board_form


def get_next_turn(game):
    """
    Returns the player who plays next, or None if the game is already over.
    """
    if get_winner(game) is None:
        return game['next_turn']
    return None
