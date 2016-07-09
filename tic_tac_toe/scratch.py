def start_new_game(player1, player2):
    """
    Creates and returns a new game configuration.
    """
    game = {'player1': self.x,
            'player2': self.o,
            'board': [
                ["-", "-", "-"],
                ["-", "-", "-"],
                ["-", "-", "-"],
            ],
            'next_turn': self.x,
            'winner': None
        }
    return game

def get_board_as_string(game):
    """
    Returns a string representation of the game board in the current state.
    """
    for row in rows[:2]:
        for col in cols:
            print
    pass

print(start_new_game('x', 'y'))

'''
O  |  O  |  X
--------------
O  |  X  |  X
--------------
O  |  X  |  O
'''