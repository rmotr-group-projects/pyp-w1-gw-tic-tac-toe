# internal helpers
#class InvalidMovement(LookupError): "Error"
from exceptions import InvalidMovement
from exceptions import GameOver

def _position_is_empty_in_board(position, board):
    """
    Checks if given position is empty ("-") in the board.

    :param position: Two-elements tuple representing a
                     position in the board. Example: (0, 1)
    :param board: Game board.

    Returns True if given position is empty, False otherwise.
    """
    #class InvalidMovement(LookupError): "Error"
    if _position_is_valid(position):
        return '-' == board[position[0]][position[1]]
    #:
        #return True
        #raise InvalidMovement("Position already taken.")
    #else:
     #   return False




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
    if type(position)==tuple:
        a= position[0]
        b= position[1]
        if a in [0,1,2] and b in [0,1,2] and len(position)==2 and type(a)!=bool and type(b)!=bool:
            return True
        else:
            return False
    else: 
        return False
    

def _board_is_full(board):
    """
    Returns True if all positions in given board are occupied.

    :param board: Game board.
    """
    return '-' not in set([values for lists in board for values in lists])




def _is_winning_combination(board, combination, player):
    """
    Checks if all 3 positions in given combination are occupied by given player.

    :param board: Game board.
    :param combination: Tuple containing three position elements.
                        Example: ((0,0), (0,1), (0,2))

    Returns True of all three positions in the combination belongs to given
    player, False otherwise.
    """
    unique_values = set([board[x][y] for x, y in combination])
    return player in unique_values and len(unique_values)==1



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
    combo_list =[((0,0) , (0,1) , (0,2)),((1,0) , (1,1) , (1,2)),((2,0) , (2,1) , (2,2)),
    ((0,0),(1,0),(2,0)),
    ((0,1),(1,1),(2,1)),
    ((0,2),(1,2),(2,2)),
    ((2,0),(1,1),(0,2)),
    ((0,0),(1,1),(2,2))
    ]
    for combination in combo_list:
        if _is_winning_combination(board,combination,player):
            return player


# public interface
def start_new_game(player1, player2):
    """
    Creates and returns a new game configuration.
    """
    return { 'player1':player1, 'player2': player2, 'board':[                                                                      
         ["-", "-", "-"],                                                                                                           
         ["-", "-", "-"],                                                                                                           
         ["-", "-", "-"],], 'next_turn':player1, 'winner':None} 


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
    #class GameOver(LookupError): "Error"
    #class InvalidMovement(LookupError): "Error"
    if get_winner(game)!=None:
        raise InvalidMovement("Game is over")
    if _board_is_full(game['board']):
        raise InvalidMovement("Game is over")
    if player != game.get('next_turn'):
        raise InvalidMovement('"{}" moves next.'.format(game.get('next_turn')))
    if _position_is_valid(position)==False:
        raise InvalidMovement('Position out of range.')
    if _position_is_empty_in_board(position, game['board'])==False:
        raise InvalidMovement("Position already taken.")
    game['board'][position[0]][position[1]]=player
    if game['next_turn']==game['player1']:
        game['next_turn'] =  game['player2']
    else: 
        game['next_turn'] =  game['player1']
    if _check_winning_combinations(game['board'], player):
        game['winner']=player
        raise GameOver('"{}" wins!'.format(player))
    if _board_is_full(game['board']):
        raise GameOver("Game is tied!")




def get_board_as_string(game):
    """
    Returns a string representation of the game board in the current state.
    """
    return """\n{}""".format("  |  ".join(game['board'][0]))+\
"\n"+"-"*(1+len("""{}""".format("  |  ".join(game['board'][0]))))+"\n"+\
"""{}""".format("  |  ".join(game['board'][1]))+"\n"+\
"-"*(1+len("""{}""".format("  |  ".join(game['board'][1]))))+\
"\n"+"""{}\n""".format("  |  ".join(game['board'][2]))


def get_next_turn(game):
    """
    Returns the player who plays next, or None if the game is already over.
    """
    if get_winner(game)!=None:
        return None
    if _board_is_full(game['board']):
        return None
    else: 
        return game['next_turn']

