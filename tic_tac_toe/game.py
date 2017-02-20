# internal helpers
from exceptions import *
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
    valid = [
            (0,0), (0,1), (0,2),
            (1,0), (1,1), (1,2),
            (2,0), (2,1), (2,2),
            ] 
    return position in valid

    
def _board_is_full(board):
    """
    Returns True if all positions in given board are occupied.

    :param board: Game board.
    """
    for pos in board:
        if '-' in pos:
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
    for pos in combination:
        if pos != player:
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
    def horizontals():
        return [row for row in board]
    
    def verticals():
        col = 0
        vert = []
        while col != 3:
            for row in board:
                vert.extend([row[col]]) 
            col += 1
        return [vert[x:x+3] for x in range(0, len(vert),3)]
    
    def diagonals():
      num = 0
      diag = []
      for row in board:
          diag.extend(row[num])
          num += 1
      num = 2
      for row in board:
          diag.extend(row[num])
          num -= 1
      return [diag[x:x+3] for x in range(0, len(diag),3)]
          
    combinations = horizontals() + verticals() + diagonals()

    for combination in combinations:
        if _is_winning_combination(board, combination,player):
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
    """
    Performs a player movement in the game. Must ensure all the pre requisites
    checks before the actual movement is done.
    After registering the movement it must check if the game is over.
    """
    
    if get_next_turn(game) != player:
        raise InvalidMovement('"{}" moves next'.format(get_next_turn(game)))
        
    if game['winner'] or _board_is_full(game['board']):
        raise InvalidMovement("Game is over.")
    
    if _position_is_valid(position):
        if not _position_is_empty_in_board(position,game['board']):
            raise InvalidMovement("Position already taken.")
        game['board'][position[0]][position[1]] = player
        game['next_turn'] = (game['player1'] if player == game['player2'] 
                            else game['player2'])  
    else:
        raise InvalidMovement("Position out of range.")
    
    if _check_winning_combinations(game['board'], player):
        game['winner'] = player
        raise GameOver('"{}" wins!'.format(player))
    
    if _board_is_full(game['board']):
        raise GameOver("Game is tied!")
        

def get_board_as_string(game):
    """
    Returns a string representation of the game board in the current state.
    """
    return '''
{}  |  {}  |  {}
--------------
{}  |  {}  |  {}
--------------
{}  |  {}  |  {}
'''.format(*[y for x in game['board'] for y in x])


def get_next_turn(game):
    """
    Returns the player who plays next, or None if the game is already over.
    """
    return game['next_turn']
