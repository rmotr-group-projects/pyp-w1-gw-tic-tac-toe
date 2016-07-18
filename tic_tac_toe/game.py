from .exceptions import *

# internal helpers
def _position_is_empty_in_board(position, board):
    x, y = position    
    return board[x][y] == '-'


def _position_is_valid(position):
    if not isinstance(position, tuple):
        return False
    
    valid_pos = [(x,y) for x in range(3) for y in range(3)]
    
    return position in valid_pos


def _board_is_full(board):
    return not any('-' in row for row in board)


def _is_winning_combination(board, combination, player):
    line_comb = [board[x][y] for (x,y) in combination]
    return [player] * len(line_comb) == line_comb


def _check_winning_combinations(board, player):
    
    length = len(board)
    winner = [player] * length
    # transposes the board (the rows become the columns and viceversa):
    # [[a,b],[c,d]] --> [(a,c),(b,d)] --> [[a,c],[b,d]]   
    # now we don't have to worry about vertical checks
    transposed = list(map(list, zip(*board)))
            
    #Check diagonals
    diag_1 = [board[i][i] for i in range(length)] # top-left to bottom right
    diag_2 = [board[i][-i-1] for i in range(length)] # top-right to bottom left
    
    if winner in [diag_1,diag_2]:
        return player
    
    for board_state in [board,transposed]:
        if winner in board_state:
            return player
    return None

# public interface
def start_new_game(player1="X", player2="O"):
    #initializes a new game, with player1 as the starting player
    
    return {
        'player1': player1,
        'player2': player2,
        'board': [
                ['-','-','-'],
                ['-','-','-'],
                ['-','-','-']
            ],
        'next_turn': player1,
        'winner': None    
    }

def get_winner(game):
    return game['winner']


def update_game(game,position):

    # update the board
    row, col = position
    player = game['next_turn']
    game['board'][row][col] = player
    
    # update the next player
    if player == game['player1']:
        game['next_turn'] = game['player2']
    else:
        game['next_turn'] = game['player1']    

def move(game, player, position):
    
    # check if the game is over and if the player should move
    
    if not get_next_turn(game): # if it's no player's next turn, game's over
        raise InvalidMovement("Game is over.")
    elif get_next_turn(game) != player:
        raise InvalidMovement('\"'+get_next_turn(game)+'\"' + " moves next")

    #check if the position is valid
    if not _position_is_valid(position):
        raise InvalidMovement('Position out of range.')
    
    #check if the position is already taken
    if not _position_is_empty_in_board(position,game['board']):
        raise InvalidMovement('Position already taken.')
    
    update_game(game,position)
    
    # check if the player won
    if _check_winning_combinations(game['board'],player):
        game['winner'] = player
        game['next_turn'] = None
        raise GameOver('\"'+player+'\"'+' wins!')
    
    # or if they tied
    elif _board_is_full(game['board']):
        game['next_turn'] = None
        raise GameOver("Game is tied!")


def get_board_as_string(game):
    as_string = "\n"
    for i, line in enumerate(game['board']):
        for j,element in enumerate(line):
            as_string += element 
            if j < 2:
                as_string += "  |  "
        if i < 2:
            as_string += "\n--------------\n"
    as_string += "\n"
    
    return as_string


def get_next_turn(game):
    # returns the player for next turn if there hasn't been a winner yet
    if get_winner(game):
        return None
    else:
        return game['next_turn']
