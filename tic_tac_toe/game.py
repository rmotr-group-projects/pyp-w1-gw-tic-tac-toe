
from .exceptions import *

def _position_is_empty_in_board(position, board):


    if not _position_is_valid(position):
        raise InvalidMovement('Position out of range.')
    if board[position[0]][position[1]] == "-":
       return True
    else:
       return False


def _position_is_valid(position):
   
    #check if tuple
    if not isinstance(position, tuple):
        return False
    #check if tuple only has two elements
    if len(position) != 2:
        return False
    #check if elements are integers
    for x in position:
        if not isinstance(x, int):
            return False
    #check if each the tuple elements are in range(0,2)
        if x not in range(0,3):
            return False
    else:
        return True

def _board_is_full(board):
  
    for x in board:
        for y in x:
            if y == "-":
                return False
    
    return True


def _is_winning_combination(board, combination, player):
   
    print(combination)
    for x in combination:
        if board[x[0]][x[1]] != player:
            return False
            
    return True

def _check_winning_combinations(board, player):
    
    
    #check if each row is a winning combination
    rows = [[], [], []]
    for x in range(0, len(board)):
        for y in range(0, len(board)):
            rows[x].append((y, x))
    for i in rows:
        test_row = tuple(i)
        if _is_winning_combination(board, test_row, player):
            return player

    #check if each column is a winning combination
    columns = [[], [], []]
    for y in range(0, len(board)):
        for x in range(0, len(board)):
            columns[y].append((y, x))
    for i in columns:
        test_column = tuple(i)
        if _is_winning_combination(board, test_column, player):
            return player

    #for diagonals
    first_diagonal = []
    second_diagonal = []

    #for the first diagonal
    for i in range(0, len(board)):
        first_diagonal.append((i,i))
    test_first_diagonal = tuple(first_diagonal)    
    if _is_winning_combination(board, test_first_diagonal, player):
        return player

    #for second diagonal
    for i in range(0, len(board)):
        second_diagonal.append((i,(len(board) - 1) - i))
    test_second_diagonal = tuple(second_diagonal)
    if _is_winning_combination(board, test_second_diagonal, player):
        return player

    return None
    
# public interface
def start_new_game(player1, player2):
    return {'player1' : "X", 'player2' : "O", 'board' : [["-","-","-"],["-","-","-"],["-","-","-"]]
     , 'next_turn' : "X", 'winner' : None}
    

def get_winner(game):
    return game['winner']


def move(game, player, position):
   
    #errors:
    #game over exception
    if _board_is_full(game['board']):
        raise InvalidMovement('Game is over.')
    #board not full but someone else won
    if get_winner(game) is not None:
        raise InvalidMovement('Game is over.')
    #wrong turn error
    if game['next_turn'] != player:
        raise InvalidMovement('"%s" moves next.' % game['next_turn'])
    
    #position already taken error
    if not _position_is_empty_in_board(position, game['board']):
        raise InvalidMovement('Position already taken.')
    
    #position out of range error
    if not _position_is_valid(position):
        raise InvalidMovement('Position out of range')
        
    #actual move function
    game['board'][position[0]][position[1]] = player
    
    if player=="X":
        game['next_turn'] = "O"
    else:
        game['next_turn'] = "X"
    
    #check who winner is
    #if board is full:
    if (_check_winning_combinations(game['board'], player)):
        game['winner'] = player
        raise GameOver('"%s" wins!' % game['winner'])
    elif _board_is_full(game['board']):
        raise GameOver('Game is tied!')
            

def get_board_as_string(game):
    pipe = '  |  '
    dashes = '-'*14
    #new_list = [y for x in game['board'] for y in x]
    return '\n{}{}{}{}{}\n{}\n{}{}{}{}{}\n{}\n{}{}{}{}{}\n'.format(
        game['board'][0][0], pipe, game['board'][0][1], pipe, game['board'][0][2], 
        dashes, 
        game['board'][1][0], pipe, game['board'][1][1], pipe, game['board'][1][2], 
        dashes, 
        game['board'][2][0], pipe, game['board'][2][1], pipe, game['board'][2][2])

def get_next_turn(game):
    if _board_is_full(game['board']):
        return None
    else:
        return game['next_turn']

