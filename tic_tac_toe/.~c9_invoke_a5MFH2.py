from exceptions import *
def _position_is_empty_in_board(position, board):
    """
    Checks if given position is empty ("-") in the board.

    :param position: Two-elements tuple representing a
                     position in the board. Example: (0, 1)
    :param board: Game board.

    Returns True if given position is empty, False otherwise.
    """
    #tuple = (1,0)
    x = position[0]
    y = position[1]
    if board[x][y] != '-':
        return False
    return True
    


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
    x, y = position
    return x in (0,1,2) and y in (0,1,2)


def _board_is_full(board):
    """
    Returns True if all positions in given board are occupied.

    :param board: Game board.
    """
    for x in board:
        for y in x:
            if y == '-':
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
    winning_combos = [
        (1,2,3),
        (4,5,6),
        (7,8,9),
        (1,4,7),
        (2,5,8),
        (3,6,9),
        (1,5,9),
        (7,5,3)
        ]
        
    for combo in winning_combos:
        count = 0
        for num in combo:
            if num in combination:
                count += 1
        if count == 3:
            return "you won"
    return "you didnt win"
    """
    
    count = 0
    for position in combination:
        if board[position[0]][position[1]] == player:
            count = count + 1
            if count == 3:
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
    winning_combos = [
        [(0,0),(0,1),(0,2)],
        [(1,0),(1,1),(1,2)],
        [(2,0),(2,1),(2,2)],
        [(0,0),(1,0),(2,0)],
        [(0,1),(1,1),(2,1)],
        [(0,2),(1,2),(2,2)],
        [(0,0),(1,1),(2,2)],
        [(0,2),(1,1),(2,0)]
        ]        
        
    for combo in winning_combos:
        if _is_winning_combination(board, combo, player) == True:
            return player
    return None
            
    
    """
    combination = []
    num = 1
    for i in range(3):
        for j in range(3):
            #print num
            if board[i][j] == player:
                combination.append(num)
            num += 1
        
    return combination
    """

   

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
    next_player = get_next_turn(game)
    if _position_is_valid(position) != True:
        raise InvalidMovement("Position out of range.")
    elif _position_is_empty_in_board(position, board) != True:
        raise InvalidMovement("Position already taken.")
    elif player != next_player:
        raise InvalidMovement((next_player, " moves next"))
    else:
        x = position[0]
        y = position[1]
        game['board'][x][y] = player
    if player == "X":
        game['next_turn'] = "O"
    else:
        game['next_turn'] = "X"
    game['winner'] = _check_winning_combinations(board, player)
    winner = get_winner(game)
    if winner != None:
        raise GameOver(winner + " wins!")
    if _board_is_full(board) == True:
        raise GameOver("Game is tied!")
    

   # raise  GameOver((player, " wins!"))     


def get_board_as_string(game):
    """
    Returns a string representation of the game board in the current state.
    """
    board = game['board']
    image
    image += "{}  |  {}  |  {}\n".format(board[0][0],board[0][1],board[0][2])
    image += "-------------\n"
    image += "{}  |  {}  |  {}\n".format(board[1][0],board[1][1],board[1][2])
    image += "-------------\n"
    image += "{}  |  {}  |  {}\n".format(board[2][0],board[2][1],board[2][2])
    return (""image
    return image

def get_next_turn(game):
    """
    Returns the player who plays next, or None if the game is already over.
    """
    return game['next_turn']



"""
game = {
    'player1': "X",
    'player2': "O",
    'board': [
        ["-", "-", "X"],
        ["-", "-", "X"],
        ["-", "-", "-"],
    ],
    'next_turn': "X",
    'winner': None
}
"""
#print(_position_is_empty_in_board((0,0), game['board']))

#print(_board_is_full(game['board']))
#combination = _check_winning_combinations(game['board'], 'X')
#print(_is_winning_combination(game['board'], combination, 'X'))
#player1="X"
##player2="O"
#move(game,player1,(2,2))

