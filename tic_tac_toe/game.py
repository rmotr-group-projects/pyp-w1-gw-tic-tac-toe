from .exceptions import InvalidMovement, GameOver

# internal helpers
def _position_is_empty_in_board(position, board):
    """
    Checks if given position is empty ("-") in the board.

    :param position: Two-elements tuple representing a
                     position in the board. Example: (0, 1)
    :param board: Game board.

    Returns True if given position is empty, False otherwise.
    """
    query_row = position[0]
    query_col = position[1]
    if board[query_row][query_col] == '-' :
        return True
    else :
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
    valid_pos = []
    for row in range(3) :
        for column in range(3) :
            curr_pos = tuple([row,column])
            valid_pos.append(curr_pos)
    
    if position in valid_pos :
        return True
    else :
        return False


def _board_is_full(board):
    """
    Returns True if all positions in given board are occupied.

    :param board: Game board.
    """
    for row in board :
        for cell in row :
            if cell == '-' :
                return False
    else :
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
    # Might need to handle exceptions here ?
    for pair in combination :
        row = pair[0]
        column = pair[1]
        if board[row][column] != player :
            return False 
    else :
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
    winning_combinations = []
    # vertical win
    for col in range (3) :
        combination_tuple = (0,col),(1,col),(2,col)
        winning_combinations.append(combination_tuple)
    
    # horizontal win
    for row in range (3) :
        combination_tuple = (row,0),(row,1),(row,2)
        winning_combinations.append(combination_tuple)
     
    # diagonal win 
        diag_tuple_1 = (0,0), (1,1), (2,2)
        diag_tuple_2 = (2,0), (1,1), (0,2)
        winning_combinations.append(diag_tuple_1)
        winning_combinations.append(diag_tuple_2)
        
    
    # use the private _is_winning_combination function here 
    for win_combination in winning_combinations : 
        if _is_winning_combination(board, win_combination, player) :
            return player

    else :
        return None


# public interface
def start_new_game(player1, player2):
    """
    Creates and returns a new game configuration.
    """
    return {
        'player1' : player1,
        'player2' : player2,
        'board' : [
            ["-", "-", "-"],
            ["-", "-", "-"],
            ["-", "-", "-"]
        ],
        'next_turn' : player1,
        'winner' : None
    }
    # We need to draw the board as expected.

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
    current_board = game['board']
    
    # is game over ? 
    if game['winner'] :
        raise InvalidMovement('Game is over.')
    
    if _board_is_full(current_board) :
        raise InvalidMovement('Game is over.')
    
    # is position invalid ?
    if not _position_is_valid(position) :
        raise InvalidMovement('Position out of range.')
    
    # is position already taken ?
    if not _position_is_empty_in_board(position,current_board): 
        raise InvalidMovement('Position already taken.')
    
    # is wrong player moving ?
    to_play = get_next_turn(game)
    if (player != to_play): 
        raise InvalidMovement('"'+ to_play + '"' + ' moves next.')
    
    
        
  
        
    # all checks passed, now you can make the move
    row = position[0]
    col = position[1]
    current_board[row][col] = player
    
    # is there a winner ?
    possible_winner = _check_winning_combinations(current_board,player)
    if possible_winner :
        # update the game
        game['winner'] = player
        game['next_turn'] = None
        raise GameOver('"'+player+'"'+' wins!')
 
    # is it a tie ? 
    if _board_is_full(current_board):
        game['next_turn'] = None
        raise GameOver("Game is tied!")
   
    
    # make sure to switch players after turn
    temp_player1 = game['player1']
    temp_player2 = game['player2']
    
    if game['next_turn'] == temp_player1 :
        game['next_turn'] = temp_player2
    else :
        game['next_turn'] = temp_player1
        


def get_board_as_string(game):
    """
    Returns a string representation of the game board in the current state.
    """
    board_to_print = game['board']
    cell_contents = []
    # store the contents of every cell in a list 
    for row in range(3) :
        for col in range(3) :
            cell_contents.append(board_to_print[row][col])
    
    line_separator = "--------------\n"
     
    board_as_string = "\n"    
    for index, item in enumerate(cell_contents) :
        # if third, then no '|'
        board_as_string += item
        pos_index = index + 1 
        if pos_index % 3 != 0 :
            board_as_string += '  |  '
        else :
            board_as_string += "\n"
            if pos_index != 9 :
                board_as_string += line_separator
    
    return board_as_string


def get_next_turn(game):
    """
    Returns the player who plays next, or None if the game is already over.
    """
    curr_board = game['board']
    if _board_is_full(curr_board) :
        return None
    else :
        return game['next_turn']
