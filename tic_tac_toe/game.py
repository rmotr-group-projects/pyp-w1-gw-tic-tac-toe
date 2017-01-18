from tic_tac_toe.exceptions import *
#For AI
from random import randint

def _position_is_empty_in_board(position, board):
    if board[position[0]][position[1]] == "-":
        return True
    else:
        return False


def _position_is_valid(position):
    if not isinstance(position,tuple):
        return False
    if len(position) != 2:
        return False
    for p in position:
        if p not in [0,1,2]:
            return False
    return True
    


def _board_is_full(board):
    for i in range(3):
        for j in range(3):
            if board[i][j] == '-':
                return False
    return True
        

def _is_winning_combination(board, combination, player):
    for position in combination:
        if board[position[0]][position[1]] != player:
            return False
    return True


def _check_winning_combinations(board, player):
    combinations = (
                    ((0,0), (0,1), (0,2)),
                    ((1,0), (1,1), (1,2)),
                    ((2,0), (2,1), (2,2)),
                    ((0,0), (1,0), (2,0)),
                    ((0,1), (1,1), (2,1)),
                    ((0,2), (1,2), (2,2)),
                    ((0,0), (1,1), (2,2)),
                    ((0,2), (1,1), (2,0))
                    )
    for combination in combinations:
        if _is_winning_combination(board, combination,player):
            return player
            
    return None



# public interface
def start_new_game(player1, player2=None):
    if player2 is None:
        player2 = 'HAL'
    new_board = {
        'player1': player1,
        'player2': player2,
        'board': [
            ["-","-","-"],
            ["-","-","-"],
            ["-","-","-"]
        ],
        'next_turn': player1,
        'winner': None
    }
    
    return new_board


def get_winner(game):
    if _check_winning_combinations(game['board'],game['player1']):
        return game['player1']
    elif _check_winning_combinations(game['board'],game['player2']):
        return game['player2']
    return None


def move(game, player, position = None):
    if player == 'HAL':
         position = robot_turn(game)
    if game['winner']:
        raise InvalidMovement('Game is over')
    if player != game['next_turn']:
        if _board_is_full(game['board']):
            raise InvalidMovement('Game is over.')
        else:
            raise InvalidMovement("\"%s\" moves next." % (game['next_turn']))
    if not _position_is_valid(position):
        raise InvalidMovement('Position out of range.')
    if not _position_is_empty_in_board(position, game['board']):
        raise InvalidMovement('Position already taken.')


    game['board'][position[0]][position[1]] = player 
    winner = get_winner(game)
    if winner:
        game['winner'] = winner
        raise GameOver('\"%s\" wins!' % (winner)) 
        
    if _board_is_full(game['board']):   
        raise GameOver('Game is tied!')
    else:
        if game['next_turn'] == game['player1']:
            game['next_turn'] = game['player2']
        else:
            game['next_turn'] = game['player1']
            

    


def get_board_as_string(game):
    board = game['board']
    p1 = board[0][0]
    p2 = board[0][1]
    p3 = board[0][2]
    p4 = board[1][0]
    p5 = board[1][1]
    p6 = board[1][2]
    p7 = board[2][0]
    p8 = board[2][1]
    p9 = board[2][2]

    row1 = "\n%s  |  %s  |  %s" % (p1,p2,p3)
    row2 = "%s  |  %s  |  %s" % (p4,p5,p6)
    row3 = "%s  |  %s  |  %s\n" % (p7,p8,p9)
    divider = "\n--------------\n" 
    game_board = row1 + divider + row2 + divider + row3
    return game_board  
    

def get_next_turn(game):
    return game['next_turn']




"""
The following are for playing against an AI
"""
'''
This was option 1.  We did not have a chance to finish it, but wanted to leave the idea.

def AI_move(game):
    while game['next_turn'] == 'HAL':
        position = (randint(0,2),randint(0,2))
        try:
            move(game,'HAL',position)
        except:
            continue
'''
    
def robot_turn(game):
    position = (randint(0,2),randint(0,2))
    while not _position_is_empty_in_board(position, game['board']):
        position = (randint(0,2),randint(0,2))
    return position

