#from exceptions import *

# internal helpers
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
    if len(position) == 2 and position[0] in range(3) and position[1] in range(3):
        return True
    else:
        raise InvalidMovement


def _board_is_full(board):
    """
    Returns True if all positions in given board are occupied.

    :param board: Game board.
    """
    if '-' in [square for row in board for square in row]:
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
    #if all tuples == player return True 

    for c in combination:
        if player != board[c[0]][c[1]]:
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
    possible_winning_combinations = [
                          [(0,0), (0,1), (0,2)], #row1
                          [(1,0), (1,1), (2,1)], #row2
                          [(2,0), (2,1), (2,2)], #row3
                          [(0,0), (1,0), (2,0)], #col1
                          [(0,1), (1,1), (2,1)], #col2
                          [(0,2), (1,2), (2,2)], #col3
                          [(0,0), (1,1), (2,2)], #diagonal1
                          [(0,2), (1,1), (2,0)]  #diagonal2
                          ]
                          
    for combination in possible_winning_combinations:
        if _is_winning_combination(board, combination, player):
            return player
    return None

# public interface
def start_new_game(player1, player2):
    game_board = [["-" for row in range(3)] for col in range(3)]
    
    game = {
        'Player1': player1,
        'Player2': player2,
        'board': game_board,
        'next_turn': player1,
        'winner': None
    }
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
    if _position_is_valid(position) and _position_is_empty_in_board(position, game['board']):
        game['board'][position[0]][position[1]] = player
        game['next_turn'] = get_next_turn(game)
        if _check_winning_combinations(game['board'], player):
            game['winner'] = player
            #raise GameOver()
            
        elif _board_is_full(game['board']):
            raise GameOver("Board is full")
            
        else:
            print ('made it')
            game['next_turn'] = get_next_turn(game)
    
    #else: position not valid?

def get_board_as_string(game):
    """
    Returns a string representation of the game board in the current state.
    
    X  |  O  |  X
    --------------
    O  |  O  |  X
    --------------
    X  |  -  |  -
    """
    print(game['board'][0][0], ' | ', game['board'][0][1], ' | ', game['board'][0][2])
    print('--------------')
    print(game['board'][1][0], ' | ', game['board'][1][1], ' | ', game['board'][1][2])
    print('--------------')
    print(game['board'][2][0], ' | ', game['board'][2][1], ' | ', game['board'][2][2])

def get_next_turn(game):
    """
    Returns the player who plays next, or None if the game is already over.
    """
    #if game over:
    return 'X' if game['next_turn'] == 'O' else 'O' 
    # else: return None
    
#g = (start_new_game('x', 'o'))
#move(g, 'X', (0,0))
#get_board_as_string(g)
