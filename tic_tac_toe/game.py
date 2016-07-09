from exceptions import InvalidMovement

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
    if isinstance(position,tuple):
        if len(position) >= 3 or len(position) < 2:
            return False
        if position[0] >= 0 and position[0] <= 2 and position[1] >= 0 and position[1] <= 2:
            return True
        else:
            return False
    else:
        return False
        

def _board_is_full(board):
    """
    Returns True if all positions in given board are occupied.

    :param board: Game board.
    """
    for row in board:
        for spot in row:
            if spot == '-':
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
    if board[combination[0][0]][combination[0][1]] == player and board[combination[1][0]][combination[1][1]] == player and board[combination[2][0]][combination[2][1]] == player:
        return True
    else:
        return False


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
    combination = (((0,0),(0,1),(0,2)),
                    ((0,0),(1,0),(2,0)),
                    ((0,0),(1,1),(2,2)),
                    ((0,2),(1,1),(2,0)),
                    ((0,2),(1,2),(2,2)),
                    ((2,0),(2,1),(2,2)),
                    ((1,0),(1,1),(1,2)),
                    ((0,1),(1,1),(2,1)))
    for singleCombo in combination:
        if _is_winning_combination(board,singleCombo,player) == True:
            return player
    # for bigTup in combination:
    #     if board[bigTup[0][0]][bigTup[0][1]] == player and board[bigTup[1][0]][bigTup[1][1]] == player and board[bigTup[2][0]][bigTup[2][1]] == player:
    #         return player
    return None            


# public interface
def start_new_game(player1, player2):
    """
    Creates and returns a new game configuration.
    """
    conf = {
        'player1' : player1,
        'player2' : player2,
        'board' : [
                    ["-", "-", "-"],
                    ["-", "-", "-"],
                    ["-", "-", "-"],
                ],
        'next_turn' : player1,
        'winner' : None
    }
    return conf

def get_winner(game):
    """
    Returns the winner player if any, or None otherwise.
    """
    pass


def move(game, player, position):
    """
    Performs a player movement in the game. Must ensure all the pre requisites
    checks before the actual movement is done.
    After registering the movement it must check if the game is over.
    """
    if _position_is_valid(position) == False:
        raise InvalidMovement()
    else:
        board = game['board']
        board[position[0]][position[1]] = player
        


def get_board_as_string(game):
    """
    Returns a string representation of the game board in the current state.
    """
    board = '\n'
    breakCount = 0
    for row in game['board']:
        board += printRow(row)
        if breakCount == 2:
            break;
        else:
            board += printBreak()
            breakCount += 1
    return board
    
def printRow(row):
    return row[0] + '  |  ' + row[1] + '  |  ' + row[2] + '\n'

def printBreak():
    return '--------------\n'
    

def get_next_turn(game):
    """
    Returns the player who plays next, or None if the game is already over.
    """
    if game['next_turn'] == 'X':
        return 'O'
    else:
        return 'X'
