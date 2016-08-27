# internal helpers

from .exceptions import InvalidMovement, GameOver


def _position_is_empty_in_board(position, board):
    
    row = position[0]
    col = position[1]
    
    if board[row][col] == "-":
        return True
    else: 
        return False
    """
    Checks if given position is empty ("-") in the board.

    :param position: Two-elements tuple representing a
                     position in the board. Example: (0, 1)
    :param board: Game board.

    Returns True if given position is empty, False otherwise.
    """


def _position_is_valid(position):
    if not type(position)==tuple:
        return False
    if len(position)>2:
        return False
    if not -1<position[0]<3:
        return False
    if not -1<position[1]<3:
        return False
    return True

    """
    Checks if given position is a valid. To consider a position as valid, it
    must be a two-elements tuple, containing values from 0 to 2.
    Examples of valid positions: (0,0), (1,0)
    Examples of invalid positions: (0,0,1), (9,8), False

    :param position: Two-elements tuple representing a
                     position in the board. Example: (0, 1)

    Returns True if given position is valid, False otherwise.
    """

def _board_is_full(board):
    for row in board:
        if "-" in row:
            return False
    return True
    """
    Returns True if all positions in given board are occupied.

    :param board: Game board.
    """

def _is_winning_combination(board, combination, player):#########lathos mallon
    for comb in combination:
        row = comb[0]
        col = comb [1]
        if board[row][col] != player:
            return False
    return True
    """
    Checks if all 3 positions in given combination are occupied by given player.

    :param board: Game board.
    :param combination: Tuple containing three position elements.
                        Example: ((0,0), (0,1), (0,2))

    Returns True of all three positions in the combination belongs to given
    player, False otherwise.
    """


def _check_winning_combinations(board, player="O"):#doit
    for item in board:#checing the rows first
        row = all (x == player for x in item )
        if row:
            return player #what you do has to much typing waste of time, as my method... go on doit
    #make neater lol
    #let me see if i can fit in a for loop
    col={'1':[ board[0][0], board[1][0], board[2][0] ],
         '2':[ board[0][1], board[1][1], board[2][1] ],
         '3':[ board[0][2], board[1][2], board[2][2] ],
         '4':[ board[0][0], board[1][1], board[2][2] ],
         '5':[ board[0][2], board[1][1], board[2][0] ]
    }
    for key in col:
        check=all(x==player for x in col[key])
        if check:
            return player
    
    
    '''
    col = [ board[0][0], board[1][0], board[2][0] ]
    check = all( x == player for x in col )
    if check:
        return player
        
    col = [ board[0][1], board[1][1], board[2][1] ]
    check = all( x == player for x in col )
    if check:
        return player
        
    col = [ board[0][2], board[1][2], board[2][2] ]
    check = all( x == player for x in col )
    if check:
        return player
        
    col = [ board[0][0], board[1][1], board[2][2] ]
    check = all( x == player for x in col )
    if check:
        return player
        
    col = [ board[0][2], board[1][1], board[2][0] ]
    check = all( x == player for x in col )
    if check:
        return player
    '''    #u see it?
    return None
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

# public interface
def start_new_game(player1, player2):
    game = {}
    game['player1'] = player1
    game['player2'] = player2
    game['board'] = [
        ["-", "-", "-"],
        ["-", "-", "-"],
        ["-", "-", "-"],
    ]
    
    game['next_turn'] = 'X'
    game['winner'] = None
    
    return game
 

def get_winner(game):
    """
    Returns the winner player if any, or None otherwise.
    """
    return game["winner"]


def move(game, player, position):
    if get_winner(game) != None or _board_is_full(game['board'])==True:
        raise InvalidMovement("Game is over.")
    if not _position_is_valid(position): 
        raise InvalidMovement("Position out of range.")
    if not _position_is_empty_in_board(position, game['board']):
        raise InvalidMovement("Position already taken.")
    if not player == game['next_turn']:
        message= '"' + game['next_turn'] + '"'
        raise InvalidMovement(message +" moves next.")
        
    game['board'][position[0]][position[1]] = player

    if _check_winning_combinations(game['board'], player = "O") == "O":
        game['winner'] = "O"
        raise GameOver('"O" wins!')
    elif _check_winning_combinations(game['board'], player = "X") =="X":
        game['winner'] = "X"
        raise GameOver('"X" wins!')
    elif _board_is_full(game['board'])==True:
        raise GameOver("Game is tied!")
    else:
        if game['next_turn']== "O":
            game['next_turn']= "X"
        else:
            game['next_turn']= "O"
    """
    Performs a player movement in the game. Must ensure all the pre requisites
    checks before the actual movement is done.
    After registering the movement it must check if the game is over.
    """


def get_board_as_string(game):
    """
    Returns a string representation of the game board in the current state.
    """
    board = game['board']
    lines = "--------------"
    space = "  |  "
    firstrow, secondrow, thirdrow = space.join(board[0]), space.join(board[1]), space.join(board[2])
    return ("\n" +firstrow + "\n" + lines + "\n" +
        secondrow + "\n" + lines + "\n" +
        thirdrow + '\n')

def get_next_turn(game):
    """
    Returns the player who plays next, or None if the game is already over.
    """
    if game['winner']!=None:
        return None
    return game['next_turn']