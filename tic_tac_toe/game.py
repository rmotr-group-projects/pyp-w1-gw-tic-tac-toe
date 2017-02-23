from .exceptions import InvalidMovement, GameOver
import string

# internal helpers
def _position_is_empty_in_board(position, board):
    """
    Checks if given position is empty ("-") in the board.

    :param position: Two-elements tuple representing a
                     position in the board. Example: (0, 1)
    :param board: Game board.

    Returns True if given position is empty, False otherwise.
    """
    whats_there = board[position[0]][position[1]]
    
    return whats_there == "-"
    

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
    if isinstance(position, int):
        return False
    elif len(position) > 2:
        return False
    if position[0] > 2 or position[0] < 0:
        return False
    if position[1] > 2 or position[1] < 0:
        return False
    
    return True


def _board_is_full(board):
    """
    Returns True if all positions in given board are occupied.

    :param board: Game board.
    """
    for row in board:
        for place in row:
            if place == '-':
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
        if board['board'][position[0]][position[1]] != player:
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
    horizontal = True
    vertical = True
    diagonal = True
    
    for row in board:
        for spot in row:
            if spot != player:
                horizontal = False
        if horizontal:
            return player
        horizontal = True
    
    for i in range(len(board)):
        for row in board:
            if row[i] != player:
                vertical = False
        if vertical:
            return player
        vertical = True
        
    for i in range(len(board)):
        piece = board[i][i]
        if piece != player:
            diagonal = False
    if diagonal:
        return player
        
    diagonal = True
    
    for i in range(len(board)):
        piece = board[i][len(board) - 1 - i]
        if piece != player:
            diagonal = False
    if diagonal:
        return player
        

# public interface
def start_new_game(player1, player2):
    """
    Creates and returns a new game configuration.
    """
    #size = 3
    
    game = {}
    game['player1'] = player1
    game['player2'] = player2
    game['board'] = [['-'] * 3 for i in range(3)]
    game['next_turn'] = player1
    game['winner'] = None
    
    return game



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
    if game['winner'] == None and _board_is_full(game['board']):
        raise InvalidMovement("Game is over.")
    elif game['winner'] != None:
        raise InvalidMovement("Game is over.")
    elif game['next_turn'] != player:
        raise InvalidMovement('"{}" moves next.'.format(game['next_turn'])) #issue formatting the error message
    elif _position_is_valid(position) == False:
        raise InvalidMovement('Position out of range.')
        
    elif _position_is_empty_in_board(position, game['board']) == False:
        raise InvalidMovement('Position already taken.')
    else:
        game['board'][position[0]][position[1]] = player #since we receive the player as 'X' or 'O' i changed this from game[player]
        if _check_winning_combinations(game['board'], player):
            game['winner'] = player
            raise GameOver('"{}" wins!'.format(player))
        elif _board_is_full(game['board']):
            game['winner'] = None
            raise GameOver('Game is tied!')
        else:    
            if game['next_turn'] == game['player2']:
                game['next_turn'] = game['player1']
            else:
                game['next_turn'] = game['player2']
        


def get_board_as_string(game):
    """
    Returns a string representation of the game board in the current state.
    """
    
    game_string = '\n'
    
    horizontal_lines = len(game['board']) - 1
    
    for row in game['board']:
        game_string += ('%s  |  %s  |  %s\n' % (row[0], row[1], row[2]))
        if horizontal_lines > 0:
            game_string += '--------------\n'
            horizontal_lines -= 1
    return game_string


def get_next_turn(game):
    """
    Returns the player who plays next, or None if the game is already over.
    """
    if game['winner']:
        return None
    
    return game['next_turn']