# internal helpers
#test3
from .exceptions import (GameOver, InvalidMovement)
#8 hours later
def _position_is_empty_in_board(position, board):
    """
    Checks if given position is empty ("-") in the board.

    :param position: Two-elements tuple representing a
                     position in the board. Example: (0, 1)
    :param board: Game board.

    Returns True if given position is empty, False otherwise.
    """
    #placement = list(position)
    position_1 = position[0]
    position_2 = position[1]
    if board[position_1][position_2] == "-":
        return True
    else:
        print(board[position_1][position_2])
        return False
    # valid_positions = [(0,0), (1,1), (2,2), 
    #                   (0,0), (1,1), (2,2),
    #                   (0,0), (1,1), (2,2),]

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
        if len(position)==2 and position[0] < 3 and position[0] > -1 and position[1] < 3 and position[1] > -1:
            return True
    return False


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
     # Diagonals
    #tuple looks like: ((0,0), (0,1), (0,2))
    #the tuple used as a position will look like: [combination(0)(0)][combination(0)(1)]
    #board position looks like board[0]board[1]
    #win_combination_list = [[hwin1], [hwin2], [hwin3], [vwin1], [vwin2], [vwin3], [dwin1], [dwin2]]
    win_combination_list = [ 
        ((0,0), (1,1), (2,2)), #diagonal win left to right
        ((0,2), (1,1), (2,0)), #diagonal win right to left
        ((0,0), (0,1), (0,2)), #horizontal win top
        ((1,0), (1,1), (1,2)), #horizontal win mid
        ((2,0), (2,1), (2,2)), #horizontal win bot
        ((0,1), (1,1), (2,1)), #vertical win middle
        ((0,2), (1,2), (2,2)), #vertical win  right
        ((0,0), (1,0), (2,0))  #vertical win left
                            ]
    if combination in win_combination_list:
        #check if all the positions in combination belong to player
        if \
        board [combination[0][0]] [combination[0][1]] == player and \
        board [combination[1][0]] [combination[1][1]] == player and \
        board [combination[2][0]] [combination[2][1]] == player:
            return (True)
    return False
        
    # if _check_winning_combinations(board, player) != None:
    #     return True
    # return False
    


def _check_winning_combinations(board, player):
    """
    There are 8 possible combinations (3 horizontals, 3 verticals and 2 diagonals)
    to win the Tic-tac-toe game.
    This helper loops through all these combinations and checks if any of them
    belongs to the given player.

    :param board: Game board.
    :param player: One of the two playing players.

    Returns the player (winner) of any of the winning combinations is completed
    by given player, or None otherwise.
    """
    #need to make tuple
    win_combination_list = ( 
        ((0,0), (1,1), (2,2)), #diagonal win left to right
        ((0,2), (1,1), (2,0)), #diagonal win right to left
        ((0,0), (0,1), (0,2)), #horizontal win top
        ((1,0), (1,1), (1,2)), #horizontal win mid
        ((2,0), (2,1), (2,2)), #horizontal win bot
        ((0,1), (1,1), (2,1)), #vertical win middle
        ((0,2), (1,2), (2,2)), #vertical win  right
        ((0,0), (1,0), (2,0))  #vertical win left
                            )
    for winner in win_combination_list:
        if _is_winning_combination(board, winner, player) == True:
            print winner
            print player
            return player
    else:
        return None
    

# public interface
def start_new_game(player1, player2):
    new_game = {}
    new_game['player1'] = player1 
    new_game['player2'] = player2
    new_game['board'] = [
        ["-", "-", "-"],
        ["-", "-", "-"],
        ["-", "-", "-"],
        ]
    new_game['next_turn'] = player1
    new_game['winner'] = None
    print "new game"
    return new_game

    
        


def get_winner(game):
    #call winner
    if _check_winning_combinations(game['board'], game['player1']) == game['player1']:
        return game['player1']
    if _check_winning_combinations(game['board'], game['player2']) == game['player2']:
        return game['player2']
    return None
    

#Returns the winner player if any, or None otherwise.


def move(game, player, position):

    if _position_is_valid(position) is False:
        raise InvalidMovement('Position out of range.')
    if get_next_turn(game) == None:
        raise InvalidMovement('Game is over.')
        ##not sure if need below
        
    #if _board_is_full(game['board']):
    #    raise GameOver('Game is tied!')
    #if player != get_next_turn:
    #    raise InvalidMovement('not your turn!')
    
    #player can make move if pass above
    #is it their turn?
    if get_next_turn(game) is not player:  # not correct player
        raise InvalidMovement('"{}" moves next'.format(get_next_turn(game)))
        
    game['board'] [position[0]] [position[1]] = game['next_turn']
    
    if game['next_turn'] == game['player1']:
        game['next_turn'] = game['player2']
    
    elif game['next_turn'] == game['player2']:
        game['next_turn'] = game['player1']

    game['next_turn'] = get_next_turn(game)
    
    
    if get_winner(game) != None:
        game['next_turn'] = None
        raise GameOver('"{}" wins!'.format(get_winner(game)) )
    if _board_is_full(game['board']):
        raise GameOver('Game is tied!')
    
        #raise GameOver('\"{}\" wins!'.format(game['winner']))
    
    
        
    """
    Performs a player movement in the game. Must ensure all the pre requisites
    checks before the actual movement is done.
    After registering the movement it must check if the game is over.
    """


def get_board_as_string(game):
    print("""
{0}  |  {1}  |  {2}
--------------
{3}  |  {4}  |  {5}
--------------
{6}  |  {7}  |  {8} """.format(
                        game['board'][0][0],game['board'][0][1],game['board'][0][2],
                        game['board'][1][0],game['board'][1][1],game['board'][1][2],
                        game['board'][2][0],game['board'][2][1],game['board'][2][2]))    
    #Returns a string representation of the game board in the current state.
    



def get_next_turn(game):
    if _board_is_full(game['board']):
        return None
    return game['next_turn']    
    
#ONLY Returns the player who plays next, or None if the game is already over.
