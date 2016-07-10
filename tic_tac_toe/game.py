# Exception classes
class GameOver(Exception):
    pass

class InvalidMovement(Exception):
    pass

# internal helpers

def _position_is_empty_in_board(position, board):
                
    """
    Checks if given position is empty ("-") in the board.

    :param position: Two-elements tuple representing a
                     position in the board. Example: (0, 1)
    :param board: Game board.

    Returns True if given position is empty, False otherwise.
    """
    column = position[0]
    row = position[1]
    if board[column][row] == '-':
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
    if type(position) != tuple:
        return False
    if len(position) != 2:
        return False
    if not all(x in range(0,3) for x in position):
        return False
    return True


def _board_is_full(board):
    """
    Returns True if all positions in given board are occupied.

    :param board: Game board.
    """
    for i in board:
        for j in i:
            if j not in 'XO':
                # We found a position that wasn't either 'X' or 'O'
                # So the board isn't full
                return False
    # We finished looking at all spaces on the board
    # and didn't find any free spots
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
    i = 0
    for i in combination:
        column = i[0]
        row = i[1]
        if board[row][column] != player:
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
    
     
    winning = [
    [(0, 0), (0, 1), (0, 2)],
    [(1, 0), (1, 1), (1, 2)],
    [(2, 0), (2, 1), (2, 2)],
    
    [(0, 0), (1, 0), (2, 0)],
    [(0, 1), (1, 1), (2, 1)],
    [(0, 2), (1, 2), (2, 2)],
    
    [(0, 0), (1, 1), (2, 2)],
    [(0, 2), (1, 1), (2, 0)]
    ]
    
    for i in winning:
        if _is_winning_combination(board, i, player):
            return player
    return None


# public interface
def start_new_game(player1, player2):
    """
    Creates and returns a new game configuration.
    """
    
    new_game = { 'player1' : player1, 'player2' : player2, 'board' : [
                                                ['-', '-', '-'],
                                                ['-', '-', '-'],
                                                ['-', '-', '-']
        ], 'next_turn' : player1, "winner" : None}

    return new_game


def get_winner(game):
    """
    Returns the winner player if any, or None otherwise.
    """
    if game["winner"]:
        return game["winner"]
    return None


def move(game, player, position):
    """
    Performs a player movement in the game. Must ensure all the pre requisites
    checks before the actual movement is done.
    After registering the movement it must check if the game is over.
    """
    if not _position_is_valid(position):
            raise InvalidMovement('Position out of range.')
    if player != game['next_turn']:
        if player == 'X':
            tmp_player = 'O'
        else:
            tmp_player = 'X'
        raise InvalidMovement('"{0}" moves next'.format(tmp_player))
    if not _position_is_empty_in_board(position, game['board']):
        raise InvalidMovement("Position already taken.")
    if  (_position_is_valid(position) and 
        _position_is_empty_in_board(position, game['board']) and
        player == game['next_turn']):
            # Register the move
            game['board'][position[0]][position[1]] = player
            # Check if we have a winner
            if _check_winning_combinations(game['board'], player):
                game['winner'] = player
                raise GameOver('"{0}" wins!'.format(player))
            # Check if there is space left on the board 
            if not _board_is_full(game['board']):
                if game['next_turn'] == "X":
                    game['next_turn'] = "O"
                else:
                    game['next_turn'] = "X"
            else: # Board is full, Game has been tied
                raise GameOver("Game is tied!")

def get_board_as_string(game):
    """
    Returns a string representation of the game board in the current state.
    """
    '''
    board = game['board'][0][0] + ' | ' + game['board'][0][1] + ' | ' + game['board'][0][2] + '\n'
    '-'*14 + '\n'
    game['board'][1][0] + ' | ' + game['board'][1][1] + ' | ' + game['board'][1][2] + '\n'
    '-'*14 + '\n'
    game['board'][2][0] + ' | ' + game['board'][2][1] + ' | ' + game['board'][2][2] + '\n'
    '''
    board = """
%s  |  %s  |  %s
--------------
%s  |  %s  |  %s
--------------
%s  |  %s  |  %s\n""" % (game['board'][0][0], game['board'][0][1], game['board'][0][2],
             game['board'][1][0], game['board'][1][1], game['board'][1][2], game['board'][2][0],
             game['board'][2][1], game['board'][2][2])
   
    print(board)
    return board




def get_next_turn(game):
    """
    Returns the player who plays next, or None if the game is already over.
    """
    if game['winner'] == None:
        return game['next_turn']
    else:
        return None 