from .exceptions import GameOver, InvalidMovement

#internal helpers
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
    """
    Checks if given position is a valid. To consider a position as valid, it
    must be a two-elements tuple, containing values from 0 to 2.
    Examples of valid positions: (0,0), (1,0)
    Examples of invalid positions: (0,0,1), (9,8), False

    :param position: Two-elements tuple representing a
                     position in the board. Example: (0, 1)

    Returns True if given position is valid, False otherwise.
    """
    if not isinstance(position, tuple):
        return False
    if len(position) != 2:
        return False
    if position[0] not in [0,1,2]:
        return False
    if position[1] not in [0,1,2]:
        return False
    return True

def _board_is_full(board):
    """
    Returns True if all positions in given board are occupied.

    :param board: Game board.
    """
    for x in range(2):
        for y in range(2):
            if(_position_is_empty_in_board((x,y), board)):
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
    for pos in combination:
        if board[pos[0]][pos[1]] != player:
            return False
    return True

def _check_winning_combinations(board, player):
    """
    There are 8 possible combinations (3 horizontals, 3, verticals and 2 diagonals)
    to win the Tic-tac-toe game.
    This helper loops through all these combinations and checks if any of them
    belongs to the given player.

    :param board: Game board.
    :param player: One of the two playing players.

    Returns the player (winner) of any of the winning combinations is completed
    by given player, or None otherwise.
    """
    
    set_of_combos = ( #row wins
            ((0,0), (0,1), (0,2)),    
            ((1,0), (1,1), (1,2)),    
            ((2,0), (2,1), (2,2)),
            #column wins
            ((0,0), (1,0), (2,0)),
            ((0,1), (1,1), (2,1)),
            ((0,2), (1,2), (2,2)),
            #diagonal wins
            ((0,0), (1,1), (2,2)),
            ((2,0), (1,1), (0,2))
            )
    
    for combo in set_of_combos:
        if _is_winning_combination(board, combo, player):
            return player
    return None

# public interface
def start_new_game(player1, player2):
    """
    Creates and returns a new game configuration.
    """
    game = {
        'player1': player1,
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
    board = game['board']
    #check to see if the right player is the one making the move    
    if player != game['next_turn']:
        raise InvalidMovement("\""+ game['next_turn'] + "\"" +" moves next.")
    #position is valid
    if not _position_is_valid(position):
        raise InvalidMovement("Position out of range.")
    # position already taken
    if not _position_is_empty_in_board(position, board):
        raise InvalidMovement("Position already taken.")
    # check if game has ended
    if game['winner'] != None or _board_is_full(board):
        raise GameOver("Game is over")
        
    # if tests are true, then move
    board[position[0]][position[1]] = player
    
    # after new move check to see if anyone has won by checking combinations
    if _check_winning_combinations(board, player):
        game['winner'] = player
        game['next_turn'] = None
        raise GameOver("\""+ game['winner'] + "\"" + " wins!") 
    # or game over if is board full 
    elif _board_is_full(board):
        game['next_turn'] = None
        raise GameOver("Game is tied!")
    # set next turn to other player
    else:
        if game['next_turn'] == game['player1']:
            game['next_turn'] = game['player2']
        else: 
            game['next_turn'] = game['player1']

def get_board_as_string(game):
    """
    Returns a string representation of the game board in the current state.
    """
    board_as_string = ''
    rows_as_strings = []
    row_divider = "\n--------------\n"
    #iterate through each row
    for row in game['board']:
        row_as_string = ' | '.join(row)
        #add each row to the list of rows with newly formatted elements    
        rows_as_strings.append(row_as_string)
    board_as_string = row_divider.join(rows_as_strings) 
    #return list of 3 formatted strings 
    return board_as_string 

def get_next_turn(game):
    """
    Returns the player who plays next, or None if the game is already over.
    """
    return game['next_turn']