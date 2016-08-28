from tic_tac_toe.exceptions import *

# internal helpers
def _position_is_empty_in_board(position, board):
    """
    Checks if given position is empty ("-") in the board.

    :param position: Two-elements tuple representing a
                     position in the board. Example: (0, 1)
    :param board: Game board.

    Returns True if given position is empty, False otherwise.
    """
    return board[position[0]][position[1]] == "-"

def _position_is_valid(position):

    if not isinstance(position, tuple):
        return False
    if len(position) != 2:
        return False
    if position[0] not in (0,1,2):
        return False
    if position[1] not in (0,1,2):
        return False
    return True
    # try:
    #     assert isinstance(position, tuple)
    #     assert all([isinstance(x,int) for x in position])
    #     assert [len(position) == 2]
    #     assert (position[0] <= 2 and position[0] >= 0)
    #     assert (position[1] <= 2 and position[1] >= 0)
    # except:
    #     raise InvalidMovement("Position out of range.")
    # return True


def _board_is_full(board):
    """
    Returns True if all positions in given board are occupied.

    :param board: Game board.
    """
    # for row in board:
    #     for spot in row:
    #         if spot == "-":
    #             return False
    #         else:
    #             continue
    #     return True
    return "-" not in [item for x in board for item in x]

def _is_winning_combination(board, combination, player):
    """
    Checks if all 3 positions in given combination are occupied by given player.

    :param board: Game board.
    :param combination: Tuple containing three position elements.
                        Example: ((0,0), (0,1), (0,2))

    Returns True of all three positions in the combination belongs to given
    player, False otherwise.
 
    """
    return all([board[combo[0]][combo[1]] == player for combo in combination])

def _check_winning_combinations(board, player):
    """
    Returns the player (winner) of any of the winning combinations is completed
    by given player, or None otherwise.
    """
    
    # These are the possible winning combinations. An improvement for us would be
    # creating a loop rather than hard-coding these.
    possible_combos = (
        #horizontal
        ((0,0),(0,1),(0,2)),
        ((1,0),(1,1),(1,2)),
        ((2,0),(2,1),(2,2)),
        
        #vertical
        ((0,0),(1,0),(2,0)),
        ((0,1),(1,1),(2,1)),
        ((0,2),(1,2),(2,2)),
        
        #diagonals
        ((0,0),(1,1),(2,2)),
        ((0,2),(1,1),(2,0))
    )
        
    for combo in possible_combos:
        if _is_winning_combination(board, combo, player):
            return player
    
    return None

def start_new_game(player1, player2):
    """
    Creates and returns a new game configuration.
    """
    
    game =  {
    'player1': player1,     # Might need to be 'X/O' ???? or not?
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
    return game['winner']


def move(game, player, position):
    """
    Performs a player movement in the game. Must ensure all the pre requisites
    checks before the actual movement is done.
    After registering the movement it must check if the game is over.
    """
    x, y = position
    board = game['board']
    
    #checks to see if Winner or the Game Board are True. If either are True, the game should be over.
    if game['winner']:
        raise InvalidMovement('Game is over.')
    if _board_is_full(game['board']):
        raise InvalidMovement('Game is over.')
    
    
    # Runs the helper function _position_is_valid with the position as argument. That function will raise an Exception if the position is
    # invalid and will allow for this function to continue if the position is valid. 
    if not _position_is_valid(position):
        raise InvalidMovement("Position out of range.")
    
    if not _position_is_empty_in_board(position, board):
        raise InvalidMovement("Position already taken.")
    
    # This if statement ensures that the next turn value matches that of the player who inputed a move here. If those players are the same
    # it applies the players name to the position on the board, otherwise an InvalidMovement exception will raise. 
    if game['next_turn'] ==  player:
        game['board'][x][y] = player
    else:
        raise InvalidMovement('"%s" moves next.' % game['next_turn'])
        
    if _check_winning_combinations(board, player):
        game['winner'] = player
        game['next_turn'] = None
        raise GameOver('"{}" wins!'.format(player))
    elif _board_is_full(board):
        game['winner'] = None
        game['next_turn'] = None
        raise GameOver('Game is tied!')
    #If the player who envoked the move was 'player1', then the next_turn will be set to player 2. If it was player 2, next turn will be set to player 1
    else:
        game['winner'] = None
        if player == game['player1']:
            game['next_turn'] = game['player2']
        else:
            game['next_turn'] = game['player1'] 
    
    
def get_board_as_string(game):
    """
    Returns a string representation of the game board in the current state.
    """
    # top_row_is = "\n {}  |  {}  |  {}\n".format(game['board'][0][0],game['board'][0][1],game['board'][0][2])
    # second_row_is = " {}  |  {}  |  {}\n".format(game['board'][1][0],game['board'][1][1],game['board'][1][2])
    # third_row_is = "  {}  |  {}  |  {}\n".format(game['board'][2][0],game['board'][2][1],game['board'][2][2])
    # divider = "--------------\n"
    #return (top_row_is, divider,second_row_is,divider,third_row_is)
    #return str(game['board'])
    
    return "\n{}  |  {}  |  {}\n--------------\n{}  |  {}  |  {}\n--------------\n{}  |  {}  |  {}\n".format(game['board'][0][0],game['board'][0][1],game['board'][0][2], game['board'][1][0],game['board'][1][1],game['board'][1][2], game['board'][2][0],game['board'][2][1],game['board'][2][2])
    
    
def get_next_turn(game):
    """
    Returns the player who plays next, or None if the game is already over.
    """
    # The start_new_game function will set player 1 as the 'next turn' to start. 
    # Then the move function will alternate between player 1 and player 2
    # based on the last use of the move function. 
    return game['next_turn']
    