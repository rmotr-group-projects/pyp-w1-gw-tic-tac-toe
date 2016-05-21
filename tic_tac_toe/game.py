from .exceptions import InvalidMovement, GameOver


# # temporary testing boards - delete when code is done.
# testboard1 = [
#     ["-", "-", "-"],
#     ["-", "-", "-"],
#     ["-", "-", "-"],
# ]


# testboard2 = [
#     ["O", "X", "-"],
#     ["O", "X", "-"],
#     ["O", "X", "-"],
# ]


# testboard3 = [
#     ["X", "X", "X"],
#     ["X", "X", "X"],
#     ["X", "X", "X"],
# ]

# combo1 = ((0,0),(0,1),(0,2)) # win on testboard3  for X
# combo2 = ((0,0),(1,1),(2,2)) # win on testboard2, 3 for X
# combo3 = ((2,0),(1,1),(0,2)) # win on testboard3 for X
# combo4 = ((0,0),(1,0),(2,0)) # win on testboard2 for O


# ------------------------
""" Internal functions:"""
# ------------------------

def _position_is_empty_in_board(position, board):                               # DONE
    """
    Checks if given position is empty ("-") in the board.

    :param position: Two-elements tuple representing a
                     position in the board. Example: (0, 1)
    :param board: Game board.

    Returns True if given position is empty, False otherwise.
    """
    # board as a list of 3 lists, with a char '-' in position if empty
    if not _position_is_valid(position):
        raise InvalidMovement('Position out of range.')
    if board[position[0]][position[1]] == '-':
        return True
    else:
        return False
        #raise InvalidMovement('Position already taken.')

#assert _position_is_empty_in_board((0,1), testboard1) == True
#assert _position_is_empty_in_board((0,1), testboard2) == False
#assert _position_is_empty_in_board((2,2), testboard3) == False


def _position_is_valid(position):                                               # DONE
    """
    Checks if given position is a valid. To consider a position as valid, it
    must be a two-elements tuple, containing values from 0 to 2.
    Examples of valid positions: (0,0), (1,0)
    Examples of invalid positions: (0,0,1), (9,8), False

    :param position: Two-elements tuple representing a
                     position in the board. Example: (0, 1)

    Returns True if given position is valid, False otherwise.
    """
    board_dim_x = 3
    board_dim_y = 3
    
    # Check if two element tuple:
    if not isinstance(position, tuple):
        return False
    if not len(position) == 2:
        return False
    
    # Check if tuple values are valid for board 
    if position[0] not in list(range(0,board_dim_x)):
        return False
    
    if position[1] not in list(range(0,board_dim_y)):
        return False
    
    # TODO: if the position is invalid, we need to raise
    # InvalidMovement('Position already taken.')
                                     
    return True

#assert _position_is_valid((0,0)) = True
#assert _position_is_valid((1,0)) = True
#assert _position_is_valid((2,0)) = True
#assert _position_is_valid((3,0)) = False
#assert _position_is_valid((0,1)) = True
#assert _position_is_valid((0,2)) = True
#assert _position_is_valid((0,3)) = False
#assert _position_is_valid((2,3)) = False


def _board_is_full(board): # nick                                               # TODO
    """
    Returns True if all positions in given board are occupied.
    :param board: Game board.
    """
    for row in board:
        if '-' in row:
            return False 
    return True

#assert _board_is_full(testboard1) == False
#assert _board_is_full(testboard3) == True


def _is_winning_combination(board, combination, player): # jon                  # DONE
    """
    Checks if all 3 positions in given combination are occupied by given player.

    :param board: Game board.
    :param combination: Tuple containing three position elements.
                        Example: ((0,0), (0,1), (0,2))

    Returns True of all three positions in the combination belongs to given
    player, False otherwise.
    """
    for x,y in combination:
      if board[x][y] != player:
        return False
    return True

#assert _is_winning_combination(testboard2, combo1, 'X') == False
#assert _is_winning_combination(testboard3, combo1, 'X') == True
#assert _is_winning_combination(testboard3, combo1, 'O') == False
#assert _is_winning_combination(testboard2, combo4, 'O') == True
#assert _is_winning_combination(testboard1, combo2, 'O') == False
#assert _is_winning_combination(testboard1, combo2, 'X') == False

def _check_winning_combinations(board, player):                                 # TO CLEAN UP
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
    
    #Check if player has all three along a horizonal:
    for row in board:
        if row[0] == row[1] and row[0] == row[2]:
            if row[0] == player:
                return player
    
    # Check if a player has all three along the vertical by checking 
    # if has all three horizonatal in transposed board
    for row in list(zip(*board)):
        if row[0] == row[1] and row[0] == row[2]:
            if row[0] == player:
                return player
            
    # Check if a player has either diagonal:
    if board[0][0] == board[1][1] and board[0][0] == board[2][2]:
        if board[0][0] == player:
            return player
    if board[0][2] == board[1][1] and board[0][2] == board[2][0]:
        if board[0][2] == player:
            return player
    
    return None

# public interface
def start_new_game(player1, player2):                                           # DONE
    """
    Creates and returns a new game configuration.
    """
    defaultgame = {
        'player1': player1,
        'player2': player2,
        'board': [
            ["-", "-", "-"],
            ["-", "-", "-"],
            ["-", "-", "-"],
        ],
        'next_turn': 'X',
        'winner': None
    }
    return defaultgame


def get_winner(game): # jon                                                     # DONE
    """
    Returns the winner player if any, or None otherwise.
    """
    return game['winner']


def move(game, player, position):                                               # TODO
    """
    Performs a player movement in the game. Must ensure all the pre requisites
    checks before the actual movement is done.
    After registering the movement it must check if the game is over.
    """
    
    
    #Is it that player's turn?
    if get_next_turn(game) != player:
        print('THE PLAYER IS', player, 'BUT THE NEXT TURN IS FOR', game['next_turn'])
        next_move = '"{}" moves next'.format(game['next_turn'])
        raise InvalidMovement(next_move)

    # Is board full
    if _board_is_full(game['board']):
        print "DEBUG: _is_board_full did execute."
        raise GameOver('Game is over.')

    if not _position_is_valid(position):
        raise InvalidMovement('Position out of range.')
        

    # Did player1 or player2 win the game already?
    if get_winner(game):
        raise InvalidMovement('Game is over.')
        
    if not _position_is_empty_in_board(position, game['board']):
        raise InvalidMovement('Position already taken. TEST')
        
    # Perform the move:
    row, column = position
    #import ipdb; ipdb.set_trace()
    game['board'][position[0]][position[1]] = player
    # condition_is_true if condition else condition_is_false

    #game['next_turn'] = game['player1'] if player == game['player2'] else game['player2']
    if player == game['player2']:
        game['next_turn'] = game['player1']
    else:
        game['next_turn'] = game['player2']

    # Is game now won?
    if _check_winning_combinations(game['board'], player):
        game['winner'] = _check_winning_combinations(game['board'], player)
#        raise GameOver(player wins!) 

    # Is game won?
    if get_winner(game):
        winner = get_winner(game)
        win_message = '"{}" wins!'.format(winner)
        raise GameOver(win_message)

    # Is board full?
    if _board_is_full(game['board']):
        raise GameOver('Game is tied!')
        
    

def get_board_as_string(game): # jon                                            # DONE
    """
    Returns a string representation of the game board in the current state.
    """
    board = game.get('board')
    row1 = '{}  |  {}  |  {}'.format(board[0][0], board[0][1], board[0][2])
    row2 = '{}  |  {}  |  {}'.format(board[1][0], board[1][1], board[1][2])
    row3 = '{}  |  {}  |  {}'.format(board[2][0], board[2][1], board[2][2])
    delimeter = '--------------'
    return '\n' + row1 + '\n' + delimeter + '\n' + row2 + '\n' + delimeter + '\n' + row3 + '\n'


def get_next_turn(game):                                                        # DONE
    """
    Returns the player who plays next, or None if the game is already over.
    """
    if not get_winner(game):
        return game.get('next_turn')
    else:
        return None