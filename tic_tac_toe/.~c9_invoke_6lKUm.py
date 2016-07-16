# internal helpers
def _position_is_empty_in_board(position, board):
    """
    Checks if given position is empty ("-") in the board.

    :param position: Two-elements tuple representing a
                     position in the board. Example: (0, 1)
    :param board: Game board.

    Returns True if given position is empty, False otherwise.
    """
    if board[position[0]][position[1]] == "-":
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
    valid_numbers = [0,1,2]
    if isinstance(position,tuple) and len(position) == 2 and position[0] in valid_numbers and position[1] in valid_numbers:
        return True
    else:
        return False
    

def _board_is_full(board):
    """
    Returns True if all positions in given board are occupied.

    :param board: Game board.
    """
    flattened_board = [position_on_board for row_on_board in board for position_on_board in row_on_board]
    
    for item in flattened_board:
        if item == '-':
            return False
    return True

def _is_winning_combination(board, combination, player):
    """
    Checks if all 3 positions in given combination are occupied by given player.

    :param board: Game board.
    :param combination: Tuple containing three position elements.
                        Example: ((0,0), (0,1), (0,2))

    Returns True if all three positions in the combination belongs to given
    player, False otherwise.
    """
    if isinstance(combination,tuple) and len(combination) == 3:
        for (x,y) in combination:
            if _position_is_valid((x,y)):
        	    if board[x][y] != player:
        	        return False
    	else:
    	    return True


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
    possible_combinations = (
                            ((0,0), (0,1), (0,2)) # first row
                            ((1,0), (1,1), (1,2)), # second row
                            ((2,0), (2,1), (2,2)), # third row
                            ((0,0), (1,0), (2,0)), # first column
                            ((0,1), (1,1), (2,1)), # second column
                            ((0,2), (1,2), (2,2)), # third column
                            ((0,0), (1,1), (2,2)), #right to left diagonal
                            ((0,2), (1,1), (2,0))  #left to right diagonal
                            )
    for each_combination in possible_combinations:
        if _is_winning_combination(board, each_combination, player):
            return player
    return None

# public interface
player1 = "X"
player2 = "O"
def start_new_game(player1, player2):
    """
    Creates and returns a new game configuration.
    """
    initial_game_details = {
    'player1': player1,
    'player2': player2,
    'board': [
        ["-", "-", "-"],
        ["-", "-", "-"],
        ["-", "-", "-"],
    ],
    'next_turn': "X",
    'winner': None
    }
    return initial_game_details



def get_winner(game):
    """
    Returns the winner player if any, or None otherwise.
    """
    return game['winner']


def move(game, player, position):
    """
    Performs a player movement in the game. Must ensure all the prerequisites
    checks before the actual movement is done.
    After registering the movement it must check if the game is over.
    """
    if not _board_is_full(game['board']) and _position_is_valid(position) and _position_is_empty_in_board(position,game['board']):
        game['board'][position[0]][position[1]] = player
        # Check to see if player won or if game is over \/ down here
        if _check_winning_combinations(game['board'],player):
            pass
            game['winner'] = player
            # set player as winner
            #raise gameover excpetion
    else:
        pass
        ## raise exceptions


def get_board_as_string(game):
    """
    Returns a string representation of the game board in the current state.
    """
    return str('\n' + game['board'][0][0] + '  |  ' + game['board'][0][1] + '  |  ' + game['board'][0][2] + '\n--------------\n' + game['board'][1][0] + '  |  ' + game['board'][1][1] + '  |  ' + game['board'][1][2] + '\n--------------\n' + game['board'][2][0] + '  |  ' + game['board'][2][1] + '  |  ' + game['board'][2][2] + '\n')
        


def get_next_turn(game):
    """
    Returns the player who plays next, or None if the game is already over.
    """
    if get_winner(game) == None and not _board_is_full(game['board']):
        return game['next_turn'] # need to see test_main.py to see what to return otherwise we can use this text: "Next person to plays is " + " " + 
    else:
        return None
