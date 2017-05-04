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
        
    if board[position[0]][position[1]] == '-':
        return True
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
    
    if isinstance(position, tuple):
        if len(position) == 2:
            if position[0] >= 0 and position[1] >= 0:
                if position[0] <= 2 and position[1] <= 2:
                    return True
    return False


def _board_is_full(board):
    """
    Returns True if all positions in given board are occupied.

    :param board: Game board.
    """
    for row in board:
        for pos in row:
            if pos == '-':
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
    """
    #return [player == board[x][y] for all(lambda x, y: x, y for combo in combination)]
    # return [lambda x, y: x, y for combo in combination if board[x][y] == player]
    # return [num for num in a_list if all(num % term == 0 for term in a_list_of_terms)]
    # values = list(map(lambda x,y : board[x][y], combination))
    
    # '''try:
    #     if all(value in values == player):
    #         return True
    # except InvalidMovement():
    #     return False'''
    # if all(value in values == player):
    #     return True
    # return False
    # for x, y in combination:
    #     if all(board[x][y] == player):
    #         return True
    for combo in combination:
        for x, y in combo:
            return all(board[x][y] == player)
    """
    for pos in combination:
        if board[pos[0]][pos[1]] != player:
            return False
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
    '''
    
    '''
    # (0,0)(0,1)(0,2) Horizontal
    # (1,0)(1,1)(1,2) Horizontal
    # (2,0)(2,1)(2,2) Horizontal
    # (0,0)(1,1)(2,2) Diagonals
    # (0,2)(0,1)(0,0) Diagonals
    # (0,0)(1,0)(2,0) Vertical
    # (0,1)(1,1)(2,1) Vertical
    # (0,2)(1,2)(2,2) Vertical
    """ 
    player_combo = [player, player, player]
    
    #column0 = []
    #column1 = []
    #column2 = []
    horizontals = [((0,0), (0,1), (0,2)), ((1,0), (1,1), (1,2)), # THESE ARE OUR
                   ((2,0), (2,1), (2,2))]                        # LISTS OF TUPLES
    diagonals = [((0,0), (1,1), (2,2)), ((0,2), (1,1), (2,0))]   #  OF TUPLES FOR 
    verticals = []                                               # _is_winning_commbination
    for i in range(3):
        verticals.append(((0,i), (1,i), (2,i)))
        print(verticals)
        #column0.append(board[num][0])
        #column1.append(board[num][1])
        #column2.append(board[num][2])
        
    all_columns = horizontals + verticals + diagonals
    
    # NEED TO ITERATE THROUGH all_columns AND CALL _is_winning_commbination
    # TO SEE IF ANY OF THEM ARE WINNERS
    
    '''if player_combo in board:
        return player
    elif player_combo in all_columns:
        return player
    elif player_combo in diagonals:
        return player
    return None'''
    """
    combinations = (
        # horizontals
        ((0, 0), (0, 1), (0, 2)),
        ((1, 0), (1, 1), (1, 2)),
        ((2, 0), (2, 1), (2, 2)),

        # verticals
        ((0, 0), (1, 0), (2, 0)),
        ((0, 1), (1, 1), (2, 1)),
        ((0, 2), (1, 2), (2, 2)),

        # diagonals
        ((0, 0), (1, 1), (2, 2)),
        ((2, 0), (1, 1), (0, 2)),
    )
    for combo in combinations:
        if _is_winning_combination(board, combo, player):
            return player
    return None



# public interface
def start_new_game(player1, player2):
    """
    Creates and returns a new game configuration.
    """
    return {
            'player1': player1,
            'player2': player2,
            'board': [
                ['-', '-', '-'],
                ['-', '-', '-'],
                ['-', '-', '-'],
            ],
            'next_turn': player1,
            'winner': None,
           }
    


def get_winner(game):
    """
    Returns the winner player if any, or None otherwise.
    """
    return game['winner'] # NEEDS TO CALL _check_winnning_combinations TO FIND
                          # IF THERE IS A WINNER


def move(game, player, position):
    """
    Performs a player movement in the game. Must ensure all the pre requisites
    checks before the actual movement is done.
    After registering the movement it must check if the game is over.
    """
    """
    if game['board'][position[0]][position[1]] != '-':
        raise InvalidMovement('Position already taken.') # CHANGED FROM RETURN
    else:                                                # TO RAISE
        game['board'][position[0]][position[1]] = player
    """
    '''
    if game['winner']:
        raise InvalidMovement('Game is over.')
    if player != game['next_turn']:
        raise InvalidMovement('"{}" moves next'.format(game['next_turn']))
    if not _position_is_valid(position):
        raise InvalidMovement('Position out of range.')
    if not _position_is_empty_in_board(position, game['board']):
        raise InvalidMovement('Position is already taken.')

    game['board'][position[0]][position[1]] = player
    if _check_winning_combinations(game['board'], player):
        game['winner'] = player
        game['next_turn'] = None
        raise GameOver('"{}" wins!'.format(player))
        
    if game['next_turn'] == game['player1']:
        game['next_turn'] == game['player2']
    else:
        game['next_turn'] == game['player1']
    
    
    '''
    board = game['board']
    if game['winner'] or _board_is_full(board):
        raise InvalidMovement('Game is over.')
    if player != game['next_turn']:
        raise InvalidMovement('"{}" moves next.'.format(game['next_turn']))
    if not _position_is_valid(position):
        raise InvalidMovement('Position out of range.')
    if not _position_is_empty_in_board(position, board):
        raise InvalidMovement('Position already taken.')
    board[position[0]][position[1]] = player
    winner = _check_winning_combinations(board, player)
    if winner:
        game['winner'] = winner
        game['next_turn'] = None
        raise GameOver('"{}" wins!'.format(winner))
    elif _board_is_full(board):
        game['next_turn'] = None
        raise GameOver('Game is tied!'.format(winner))
    else:
        game['next_turn'] = game['player1'] if game['next_turn'] == game['player2'] else game['player2']
   
   
   
   
   

def get_board_as_string(game):
    """
    Returns a string representation of the game board in the current state.
    """
    board_string = """
{}  |  {}  |  {}
--------------
{}  |  {}  |  {}
--------------
{}  |  {}  |  {}
""".format(*[mark for val in game['board'] for mark in val])
    return board_string


def get_next_turn(game):
    """
    Returns the player who plays next, or None if the game is already over.
    """
    if game['winner']:
        return None
    return game['next_turn']
