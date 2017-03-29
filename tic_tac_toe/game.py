import pdb
# internal helpers
from .exceptions import InvalidMovement, GameOver
# virtual-env: 'extensible-ttt'
def _position_is_empty_in_board(position, board):
    """
    Checks if given position is empty ("-") in the board.

    :param position: Two-elements tuple representing a
                     position in the board. Example: (0, 1)
    :param board: Game board.

    Returns True if given position is empty, False otherwise.
    """
    if board[position[0]][position[1]] == '-':
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
    if not isinstance(position, tuple):
        return False
    elif len(list(position)) > 2 or (position[0] < 0 or position[1] < 0 or position[1] > 2 or position[0] > 2):
        return False
    return True


def _board_is_full(board):
    """
    Returns True if all positions in given board are occupied.

    :param board: Game board.
    """
    for list in board:
        if '-' in list:
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
    char_list = []
    for position in combination:
        char_list.append(board[position[0]][position[1]])
    if len(set(char_list)) > 1 or player not in set(char_list):
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
    # pdb.set_trace()
    _in_a_row_to_win = len(board[0])
    vertical_combos = []
    diagonal_combos_1 = []
    diagonal_combos_2 = []
    list_index = 0
    flat_win_check = []
    flat_win_check += board

    for i in range(_in_a_row_to_win):
        vert_list = []
        for _list in board:
            vert_list.append(_list[i])
        vertical_combos.append(vert_list)
    flat_win_check += vertical_combos
    
    for i in range(_in_a_row_to_win):
        diagonal_combos_1 += [board[i][i]]
    #return diagonal_combos_1
    flat_win_check += [diagonal_combos_1]
    
    for i in reversed(range(_in_a_row_to_win)):
        diagonal_combos_2 += [board[list_index][i]]
        list_index += 1
    #return diagonal_combos_2
    flat_win_check += [diagonal_combos_2]
    #return flat_win_check

    for _list in flat_win_check:
        if _list[0] == player and len(set(_list)) == 1:
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
    # pdb.set_trace()
    if game['winner'] or _board_is_full(game['board']):
        raise InvalidMovement('Game is over.')
    
    if player != get_next_turn(game):
        raise InvalidMovement('"{}" moves next.'.format(game['next_turn']))
    
    if not _position_is_valid(position):
        raise InvalidMovement('Position out of range.')
    
    if not _position_is_empty_in_board(position, game['board']):
        raise InvalidMovement('Position already taken.')
    
    game['board'][position[0]][position[1]] = player
    
    game['next_turn'] = game['player1'] if game['next_turn'] == game['player2'] else game['player2']
    
    winner = _check_winning_combinations(game['board'], player)
    
    # pdb.set_trace()
#check winner combination and update if there is a winner
    if winner:
        game['winner'] = player
        game['next_turn'] = None
        raise GameOver('"{}" wins!'.format(player))

     #no winner game is tied if board full
    if _board_is_full(game['board']):
        game['next_turn'] = None
        raise GameOver('Game is tied!')
 
    player1 = game['player1']
    player2 = game['player2']
    game['next_turn'] = player1 if player == player2 else player2
   
    
        

        


def get_board_as_string(game):
    """
    Returns a string representation of the game board in the current state.
    """
#standard board config, must be created anew for any customizable board-making functions (variable columns, rows, etc)    
    str_board = "\n{}  |  {}  |  {}\n--------------\n{}  |  {}  |  {}\n--------------\n{}  |  {}  |  {}\n"


    flattened_board = []

    for list in game['board']:
        sub_list = [character for character in list]
        flattened_board += sub_list
    str_board = str_board.format(*flattened_board)
    
    return str_board


def get_next_turn(game):
    """
    Returns the player who plays next, or None if the game is already over.
    """
    return game['next_turn']
