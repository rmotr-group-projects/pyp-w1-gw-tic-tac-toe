from tic_tac_toe.exceptions import InvalidMovement, GameOver



def _position_is_empty_in_board(position, board):
    pos1 = position[0]
    pos2 = position[1]
    if board[pos1][pos2] == "-":
        return True
    else:
        return False



def _position_is_valid(position):
    valid_positions = [(row, col) for row in range(3) for col in range(3)]
    
    if position in valid_positions:
        return True
    else:
        return False
    
    

def _board_is_full(board):
    for row in board:
        for pos in row:
            if pos == '-':
                return False
    else:
        return True



def _is_winning_combination(board, combination, player):
    vals_in_combination = [board[pos[0]][pos[1]] for pos in combination]
    return len(set(vals_in_combination)) == 1
    


def _check_winning_combinations(board, player):
    across_combinations = [[(index, col) for col in range(len(row))] \
    for index, row in enumerate(board)]
    
    vertical_combinations = [[(col, index) for col in range(len(row))] \
    for index, row in enumerate(board)]
    
    diagonal_1_combination = [[(index, index)for index, row in enumerate(board)]]
    
    diagonal_2_combination = [[(len(row)-1-index, index)for index, row in \
    enumerate(board)]]
    
    all_combinations = across_combinations + vertical_combinations + \
    diagonal_2_combination + diagonal_1_combination

    for lists in all_combinations:
        test_for_equality = []
        for pos in lists:
            test_for_equality.append(board[pos[0]][pos[1]])
        if len(set(test_for_equality)) == 1 and test_for_equality[0] != '-':
            return test_for_equality[0]
        else:
            continue
    else:
        return None

            

# public interface
def start_new_game(player1, player2):
    game = {
        'player1': player1,
        'player2': player2,
        'board': [
            ["-", "-", "-"],
            ["-", "-", "-"],
            ["-", "-", "-"],
        ],
        'next_turn': "X",
        'winner': None
        }

    return game

def get_winner(game):
    return game["winner"]


def move(game, player, position):
    winner = _check_winning_combinations(game["board"], player)
    if _board_is_full(game["board"]) == True and game["winner"] is not None:
        raise InvalidMovement('Game is over.')
    
    if not _position_is_valid(position):
        raise InvalidMovement('Position out of range.')
    
    next_turn = get_next_turn(game)
    if next_turn is None:
        raise InvalidMovement("Game is over.")
    
    if not _position_is_empty_in_board(position, game["board"]):
        raise InvalidMovement('Position already taken.')
        
    if next_turn != player:
        raise InvalidMovement('"{}" moves next'.format(next_turn))
    
    game['board'][position[0]][position[1]] = player
    
    winner = _check_winning_combinations(game["board"], player)
    if _board_is_full(game["board"]) and winner is None:
        raise GameOver('Game is tied!')
    elif winner is not None:
        game['winner'] = winner
        raise GameOver('"{}" wins!'.format(winner))
    else:
        if game["next_turn"] == game['player1']:
            game['next_turn'] = game['player2']
        else:
            game['next_turn'] = game['player1']
    
    




def get_board_as_string(game):
    return '''
{}  |  {}  |  {}
--------------
{}  |  {}  |  {}
--------------
{}  |  {}  |  {}
'''.format(game["board"][0][0], game["board"][0][1], \
    game["board"][0][2], game["board"][1][0], game["board"][1][1], \
    game["board"][1][2], game["board"][2][0], game["board"][2][1], \
    game["board"][2][2])
    


def get_next_turn(game):
    if get_winner(game) is None and _board_is_full(game["board"]) == False:
        return game["next_turn"]
    else:    
        return None

