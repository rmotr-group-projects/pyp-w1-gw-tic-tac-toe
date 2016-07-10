# internal helpers
import random


def _position_is_empty_in_board(position, board):
    """
    Checks if given position is empty ("-") in the board.

    :param position: Two-elements tuple representing a
                     position in the board. Example: (0, 1)
    :param board: Game board.

    Returns True if given position is empty, False otherwise.
    """
    
    #checks if each position in the board is "-", denoting if its empty
    if board[position][board] == "-":
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
    if len(position) == 2:
        if 0 <= position(0) <= 2 and 0 <= position(1) <= 2:
            return True
        else: return False
    else: 
        return False


def _board_is_full(board):
    """
    Returns True if all positions in given board are occupied.

    :param board: Game board.
    """
    
    if (reduce(lambda x,y: x+y,board)).count("-") == 0:
        return True
    else: return False


def _is_winning_combination(board, combination, player):
    """
    Checks if all 3 positions in given combination are occupied by given player.

    :param board: Game board.
    :param combination: Tuple containing three position elements.
                        Example: ((0,0), (0,1), (0,2)) 
    for 
    Returns True if all three positions in the combination belongs to given
    player, False otherwise.
    """
    
    #check if each position of the combination in the list contains player's
    #value, return true if so, false otherwise
    
    if combination.count(player) == 3:
        return True
    else: return False
        
    
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
    
    #loop through and select each row
    for row in range(0,3):
        combination = board[row]
        if _is_winning_combination(board, combination, player) == True:
            return player
            
        else: 
            return None

    #loop through and select each column
    for column in range(0,3):
        combination = []
        #select each position and check if index was players move
        for position in range(0,3):
            combination.append(board[column[position]])
    if _is_winning_combination(board, combination, player) == True:
        return player
        
    else: return None
        
    
    combination = [board[0][0], board[1][1], board[2][2]]
    if _is_winning_combination(board, combination, player) == True:
        return player
        
    else: return None
  
    combination = [board[0][2], board[1][1], board[2][0]]
    if _is_winning_combination(board, combination, player) == True:
        return player
        
    else: return None
    
    
    

def start_new_game(player1, player2):
    '''if random.randint(0,1) == 0:
        game['next_turn'] = player1
    else:
        game['next_turn'] = player2
    return (game)
    '''

    game = {
        'player1': "X",
        'player2': "O",
        'board': [
                ["-", "-", "-"],
                ["-", "-", "-"],
                ["-", "-", "-"],
        ],
        'next_turn': "X",
        'winner': None
    }
    return game
    # public interface, use random module to select who goes first

    """
    #call method to start game & call method to print board
    replay = input("Would you like to play again? Yes or No?")
    if replay.isalpha() == "yes":
        start_new_game(player1, player2)
    else:
        print("Thanks for playing!")
    """
    
    
    
def get_winner(game):
    if game['winner'] != None:
        return game['winner']
    
        
    


def move(game, player, position=None):
    """
    Performs a player movement in the game. Must ensure all the pre requisites
    checks before the actual movement is done.
    After registering the movement it must check if the game is over.
    """
    row = input("Please enter the row you would like to play")
    if 0 >= row >=3:
        row = input("Invalid row; please enter new row")
    column = input("Please enter the column you would like to play")
    if 0 >= column >= 3:
        column = input("invalid column, please enter a new column")
    if game["board"][row][column] != "-":
        print "Position already taken."
        move(game, player, position)
    #_position_is_empty_in_board(position, board)
    #_position_is_valid(position)
    _check_winning_combinations(game["board"], player)
    get_next_turn(game)
    move(game, player, position)


def get_board_as_string(game):
        
        
        print (game["board"][0][0] + "  |  " + game["board"][0][1] + "  |  " + game['board'][0][2])
        print ("--------------") 
        print (game["board"][1][0] + "  |  " + game["board"][1][1] + "  |  " + game['board'][1][2])
        print ("--------------") 
        print (game["board"][2][0] + "  |  " + game["board"][2][1] + "  |  " + game['board'][2][2])
        
        
        '''
        print(game["board"][0][0] + "  |  " + game["board"][0][1] + "  |  " + game['board'][0][2] 
        /n --------------" 
        /n game["board"][1][0] + "  |  " + game["board"][1][1] + "  |  " + game['board'][1] 
        /n "--------------"
        /n game["board"][2][0] + "  |  " + game["board"][2][1] + "  |  " + game['board'][2][2])
        '''
       
    
        return game["board"]

def get_next_turn(game):
    """
    Returns the player who plays next, or None if the game is already over.
    """
    if game['winner'] == None:
        if game["next_turn"] == "X":
            game["next_turn"] = "O"
        else: game["next_turn"] = "X"
        return game['next_turn']

    
    
