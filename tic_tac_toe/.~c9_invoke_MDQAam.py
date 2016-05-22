# internal helpers
def _position_is_empty_in_board(position, board):
    """
    Checks if given position is empty ("-") in the board.

    :param position: Two-elements tuple representing a
                     position in the board. Example: (0, 1)
    :param board: Game board.

    Returns True if given position is empty, False otherwise.
    """
    #need to verify this is the right order
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
    # run through tuple and check against set of 0,1,2
    for i in position:
        if i not in {0,1,2}:
            return False
    return True


def _board_is_full(board):
    """
    Returns True if all positions in given board are occupied.

    :param board: Game board.
    """
    #iterate through row and then column looking for a '-' else return True (board full)
    for row in board:
        for column in row:
            if column == '-':
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
    for position in combination:
        if board[position[0]][position[1]] != player:
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
    win = False
    for i in range(3): #Rows -- i know this is not pythonic -- thinking about how to improve    
        if _is_winning_combination(board, ((0,i),(1,i),(2,i)), player):
            return player
    for i in range(3): #Columnbs -- i know this is not pythonic -- thinking about how to improve    
        if _is_winning_combination(board, ((i,0),(i,1),(i,2)), player):
            return player
    if _is_winning_combination(board, ((0,0),(1,1),(2,2)), player) or _is_winning_combination(board, ((0,2),(1,1),(2,0)), player):
        return player
        
    return "None"        

# public interface


def start_new_game(player1, player2):
    """
    Creates and returns a new game configuration.
    """
    gamedict = {
    player1: "X",
    player2: "O",
    'board': [
        ["-", "-", "-"],
        ["-", "-", "-"],
        ["-", "-", "-"],
    ],
    'next_turn': "X",
    'winner': None
    }
    return gamedict


def get_winner(game):
    """
    Returns the winner player if any, or None otherwise.
    """
    if _check_winning_combinations(game['board'],game['player1']) == game['player1']:
        return game['player1']
    elif _check_winning_combinations(game['board'],game['player2']) == game['player1']:
        return game['player2']
    else:
        return None
        



def move(game, player, position):
    """
    Performs a player movement in the game. Must ensure all the pre requisites
    checks before the actual movement is done.
    After registering the movement it must check if the game is over.
    """

    #check initial if game over
    if get_winner(game) != None:
        print("GameOver: {} wins!".format(game['winner']))
    elif _board_is_full(game['board']):
            print("InvalidMovement: Position already taken")
    
    #check valid turn
    if game['next_turn'] != player:
        print("InvalidMovement: {}  moves next.".format(game['next_turn']))
        return

    #check valid move
    if _position_is_valid(position):
        if _position_is_empty_in_board(position, game['board']):
            pass
        else:
            print("InvalidMovement: Position already taken")
    else:
        print("InvalidMovement: Position out of range.")
      
    #make move changing to X/O depending on player

    game['board'][position[0]][position[1]] = player
    
    # need to check for ties
    #check to see if player wins
    if get_winner(game) != None:
        print("GameOver: {} wins!".format(game['winner']))
    elif _board_is_full(game['board']):
        print("GameOver: Game is tied!")
    

    #change turn
    



def get_board_as_string(game):
    """
    Returns a string representation of the game board in the current state.
    """
    print(' | '.join(game['board'][0]))
    print('--------------')
    print(' | '.join(game['board'][1]))
    print('--------------')
    print(' | '.join(game['board'][2]))
    


def get_next_turn(game):
    """
    Returns the player who plays next, or None if the game is already over.
    """
    pass
