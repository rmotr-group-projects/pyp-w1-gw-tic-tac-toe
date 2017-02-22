from tic_tac_toe.exceptions import *

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
    if type(position) == tuple:
        if len(position) == 2 and 0 <= position[0] <= 2 and 0 <= position[1] <=2: #interval comparison
            return True
    return False
    


def _board_is_full(board): #done
    """
    Returns True if all positions in given board are occupied.

    :param board: Game board.
    """
    for row in board:
        for elem in row:
            if elem == '-':
              return False;
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
    if all([val if val == player else False for val in combination]):
        return True
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
    for i in range(len(board)): #checks horizontal
        if _is_winning_combination(board, board[i], player):
            return player
        if _is_winning_combination(board, [elem[i] for elem in board], player):
            return player
    if _is_winning_combination(board, [board[0][0], board[1][1], board[2][2]], player) or _is_winning_combination(board, [board[2][0], board[1][1], board[0][2]], player):
        return player


# public interface
def start_new_game(player1, player2): #done
    """
    Creates and returns a new game configuration.
    """
    return {
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


def get_winner(game): #done
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
    if player != game['next_turn']: #player goes twice
        raise InvalidMovement('"' + game['next_turn'] + '" moves next')
    elif _board_is_full(game['board']) or game['winner'] != None:
        raise InvalidMovement('Game is over.')
    elif not _position_is_valid(position): #checks validity
        raise InvalidMovement('Position out of range.')
    elif not _position_is_empty_in_board(position, game['board']): #already played
        raise InvalidMovement('Position already taken.')
    else:
        game['board'][position[0]][position[1]] = player
        game['next_turn'] = game['player1'] if game['player1'] != player else game['player2'] #whoever did not move
        game['winner'] = _check_winning_combinations(game['board'], player)
        if _board_is_full(game['board']):
            raise GameOver('Game is tied!')
        if game['winner'] != None:
            raise GameOver('Gameover: "' + game['winner'] + '" wins!')


def get_board_as_string(game): #done
    """
    Returns a string representation of the game board in the current state.
    """
    ans = '\n'
    for line in range(len(game['board'])):
        ans += '  |  '.join(game['board'][line])
        if line < len(game['board']) - 1:
            ans += '\n--------------\n'
    return ans + '\n'


def get_next_turn(game): #done
    """
    Returns the player who plays next, or None if the game is already over.
    """
    return game['next_turn']