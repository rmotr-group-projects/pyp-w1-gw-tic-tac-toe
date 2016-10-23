# internal helpers
def _position_is_empty_in_board(position, board):
    """
    Checks if given position is empty ("-") in the board.

    :param position: Two-elements tuple representing a
                     position in the board. Example: (0, 1)
    :param board: Game board.

    Returns True if given position is empty, False otherwise.
    """
    pass


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
    pass


def _board_is_full(board):
    """
    Returns True if all positions in given board are occupied.

    :param board: Game board.
    """
    pass


def _is_winning_combination(board, combination, player):
    """
    Checks if all 3 positions in given combination are occupied by given player.

    :param board: Game board.
    :param combination: Tuple containing three position elements.
                        Example: ((0,0), (0,1), (0,2))

    Returns True of all three positions in the combination belongs to given
    player, False otherwise.
    """
    pass


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
    pass


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
   
    # if tests are true
    game['board'][position[0]][position[1]] = game[player]

def get_board_as_string(game):
    """
    Returns a string representation of the game board in the current state.
    """
    board_as_string = ''
    list_of_rows_as_strings = []
    #iterate through each row
    for row in game['board']:
        #iterate through each element in each row
        row_as_string = ''
        for pos in row:
            
        #add each row to the list of rows with newly formatted elements    
        list_of_rows_as_strings.append(row_as_string)
    #return list of 3 formatted strings 
    return list_of_rows_as_strings
'''    divider = "--------"
    row_num = 0
    for row in list_of_rows_as_strings:
        if row_num < len(list_of_rows_as_strings):
            row = "\n".join(row) + "\n".join(divider)
        else:
            row = "\n".join(row)
    
    return board_as_string '''

def get_next_turn(game):
    """
    Returns the player who plays next, or None if the game is already over.
    """
    if game['winner'] == 'None':
        return game['next_turn']
    else:
        return game['winner']
    pass

game = start_new_game('X','O')
x = get_board_as_string(game)
print x