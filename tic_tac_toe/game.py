# internal helpers
def _position_is_empty_in_board(position, board):
    """
    Checks if given position is empty ("-") in the board.

    :param position: Two-elements tuple representing a
                     position in the board. Example: (0, 1)
    :param board: Game board.

    Returns True if given position is empty, False otherwise.
    """
    if board[position[0][position[1]]] == "-":
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
    if len(position) != 2:
        return False
    
    if position[0] == 0 or position[0] == 1 or position[0] == 2:
        return False
    
    if position[1] == 0 or position[1] == 1 or position[1] == 2:
        return False
    
    return True


def _board_is_full(board):
    """
    Returns True if all positions in given board are occupied.

    :param board: Game board.
    """
    for row in board:
        if row.contains('-'):
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
    for c in combination:
        if board[c[0:1]] != player:
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
    
    combinations = (
        ((0,0), (0,1), (0,2)),
        ((1,0), (1,1), (1,2)),
        ((2,0), (2,1), (2,2)),
        
        #Horizontals
        ((0,0), (1,0), (2,0)),
        ((0,1), (1,1), (2,1)),
        ((0,2), (1,2), (2,2)),
        
        #Diagonals
        ((0,0), (1,1), (2,2)),
        ((2,0), (1,1), (0,2))
    )
    
    for c in combinations:
        if _is_winning_combination(board, c, player):
            return player
    return None


# public interface
def start_new_game(player1, player2):
    """
    Creates and returns a new game configuration.
    """
    game = {'player1': player1,
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
    #check move validity
    if not _position_is_empty_in_board(position, game['board']):
        raise InvalidMovement("Position already taken.")
    if not _position_is_valid(position):
        raise InvalidMovement("Position out of range.")
        
    #check turn
    if player == get_next_turn(game):
        raise InvalidTurn("It's not your turn!")
        
    #update board
    game['board'][position[0]][position[1]] = player
    
    #update next_turn
    if player == game['player1']:
        game['next_turn'] = game['player2']
    else:
        game['next_turn'] = game['player1']
        
    #check if game is over


def get_board_as_string(game):
    """
    Returns a string representation of the game board in the current state.
    """
    board = game['board']
    print_str = ""
    for row in board:
    	for col in row:
            if row.index(col) <= 1:
    			print_str += col + "  |  "
    			#print(row.index(col))
            else:
                print_str += col
    	if board.index(row) != 2:
    		print_str += "\n--------------\n"
    #print(board)
    print(print_str)
'''    for row in board:
        for col in row:
            stringout = ""
            if row.index(col) != 2:
                print(col + "  | "),
            else:
                print(col),
        if board.index(row) != 2:
            print("\n--------------")
'''
        

''''
O  |  O  |  X
--------------
O  |  X  |  X
--------------
O  |  X  |  O
'''


def get_next_turn(game):
    """
    Returns the player who plays next, or None if the game is already over.
    """
    if game['winner'] == True:
        return None
    elif _board_is_full(game['board']):
        return None
    else:
        return game['next_turn']