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
    x, y = position
    if board[x][y] == '-':
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
    if  not isinstance(position,tuple) or \
        not all([isinstance(value,(int,float)) for value in position]):
        return False
    elif not len(position)==2:
        return False
        
    x, y = position
    if x not in range(0,3)  or y not in range(0,3):
        return False
    else:
        return True


def _board_is_full(board):
    """
    Returns True if all positions in given board are occupied.

    :param board: Game board.
    """
    board_string = []

    for row in board:
        board_string += row
    
    if '-' not in board_string:
        return True
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
    for combo in combination:
        x,y= combo
        if board[x][y]!=player:
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
    winner = [player, player, player]
    
    horizon = board[0], board[1], board[2]
    vert = [board[x][0] for x in range(3)], [board[x][1] for x in range(3)], [board[x][2] for x in range(3)]
    diag = [board[x][x] for x in range(3)], [board[2][0], board[1][1], board[0][2]]
    
    combos = horizon + vert + diag
    
    if winner in combos:
        return player
    
    
# public interface
def start_new_game(player1, player2):
    """
    Creates and returns a new game configuration.
    """
    game_dict={}
    game_dict["player1"]=player1
    game_dict["player2"]=player2
    board=[]
    for x in range(3):
        board.append(["-"]*3)
    game_dict["board"]=board
    game_dict["next_turn"]=player1
    game_dict["winner"]=None
    return game_dict

def get_winner(game):
    """
    Returns the winner player if any, or None otherwise.
    """
    if _check_winning_combinations(game['board'], game['player1']) ==  game['player1']:
        return game['player1']
    if _check_winning_combinations(game['board'], game['player2']) ==  game['player2']:
        return game['player2']


def move(game, player, position):
    """
    Performs a player movement in the game. Must ensure all the pre requisites
    checks before the actual movement is done.
    After registering the movement it must check if the game is over.
    """
    if game["winner"]:
        raise InvalidMovement("Game is over.")
    if _board_is_full(game['board']):
        raise InvalidMovement('Game is over.')
    if _position_is_valid(position) is False:
        raise InvalidMovement('Position out of range.')
    if _position_is_empty_in_board(position, game['board']) is False:
        raise InvalidMovement('Position already taken.')
    if game["next_turn"] != player:
        raise InvalidMovement('"{}" moves next'.format(game["next_turn"]))
        
    x, y = position
    game['board'][x][y] = player
    
    if _check_winning_combinations(game['board'], player) == player:
        game["winner"]=player
        raise GameOver('"{}" wins!'.format(player))
    
    if _board_is_full(game['board']):
        raise GameOver('Game is tied!')

    if game["next_turn"] == game["player1"]:
        game["next_turn"] = game["player2"]
    else:
        game["next_turn"] = game["player1"]

def get_board_as_string(game):
    """
    Returns a string representation of the game board in the current state.
    """
    board=game['board']
    str_board=[]
    for row in board:
        str_board.append("  |  ".join(row))
    return "\n"+"\n--------------\n".join(str_board)+"\n"

def get_next_turn(game):
    """
    Returns the player who plays next, or None if the game is already over.
    """
    if _board_is_full(game['board']):
        return None
    
    if get_winner(game):
        return None
    
    return game['next_turn']