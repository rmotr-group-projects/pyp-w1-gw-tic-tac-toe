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
    if board[position[0]][position[1]] != '-':
        return False
    else:
        return True


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
    # check position is a valid tuple
    if not isinstance(position, tuple) or len(position) != 2:
        return False
    # check position is within range
    for p in position:
        if p < 0 or p > 2:
            return False
    
    return True


def _board_is_full(board):
    """
    Returns True if all positions in given board are occupied.

    :param board: Game board.
    """
    for row in board:
        if "-" in row:
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
    return set([board[combination[position][0]][combination[position][1]] for position in combination])==player


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
    for i,row in enumerate(board):
        # horizontals combinations
        if board[i][0] == board[i][1] == board[i][2] == player:
            return player
        # verticals combination
        if board[0][i] == board[1][i] == board[2][i] == player:
            return player
    
    # diagonals combination
    if board[0][0] == board[1][1] == board[2][2] == player:
        return player
    if board[0][2] == board[1][1] == board[2][0] == player:
        return player
            
    return None


# public interface
def start_new_game(player1, player2):
    """
    Creates and returns a new game configuration.
    """
    # create game
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
    if _check_winning_combinations(game['board'], game['player1']) != None:
        return game['player1']
    elif _check_winning_combinations(game['board'], game['player2']) != None:
        return game['player2']
    return None


def move(game, player, position):
    """
    Performs a player movement in the game. Must ensure all the pre requisites
    checks before the actual movement is done.
    After registering the movement it must check if the game is over.
    """
    row,col=position
    
    if _board_is_full(game['board']):
      raise InvalidMovement('Game is over.')
    if game['winner'] != None:
        raise InvalidMovement('Game is over.')
        
    if game['next_turn'] != player:
        raise InvalidMovement('"{}" moves next!'.format(game['next_turn']))
    
    if _position_is_valid(position):
        
        if game['board'][row][col] != "-":
            raise InvalidMovement('Position already taken.')
    
        game['board'][row][col] = player
        if _board_is_full(game['board']):
            raise GameOver('Game is tied!')
        result = _check_winning_combinations(game['board'],player)
    
        if result is not None:
            game['winner'] = player
            game['next_turn'] = None
            raise GameOver('"{}" wins!'.format(player))
        
        if player == game['player2']:
            game['next_turn'] = game['player1'] 
        else: 
            game['next_turn'] = game['player2']
        
    else:
        raise InvalidMovement("Position out of range.")
        
    return game


def get_board_as_string(game):
    """
    Returns a string representation of the game board in the current state.
    """
    str_ = '\n'
    str_ +=  str(game['board'][0])
    str_ += '\n--------------\n{}'.format(game['board'][1])
    str_ += '\n--------------\n{}\n'.format(game['board'][2])
    
    for ch in [',']:
        if ch in str_:
            str_=str_.replace(ch,"  | ")
    
    for ch in ['[',']','\'']:
        if ch in str_:
            str_=str_.replace(ch,"")
    return str_

def get_next_turn(game):
    """
    Returns the player who plays next, or None if the game is already over.
    """
    if game['winner'] is None:
        return game['next_turn']
    else:
        return None
        
