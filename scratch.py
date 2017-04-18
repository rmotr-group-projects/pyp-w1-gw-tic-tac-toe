'''
game = {
    'player1': "X",
    'player2': "O",
    'board': [
        ["-", "X", "-"],
        ["-", "-", "-"],
        ["-", "-", "O"],
    ],
    'next_turn': "X",
    'winner': None
}

board = game['board']
'''
#print(game['board'][2][2])
game = {
    'player1': "X",
    'player2': "O",
    'board': [
        ["-", "X", "-"],
        ["-", "-", "-"],
        ["-", "-", "O"],
    ],
    'next_turn': "X",
    'winner': None
}
board= [
        ["-", "X", "-"],
        ["-", "-", "-"],
        ["-", "-", "O"],
    ]
def get_board_as_string(game):
    """
    Returns a string representation of the game board in the current state.
    """
    board = game['board']
    image = '"""' + "\n"
    image += "{}  |  {}  |  {}\n".format(board[0][0],board[0][1],board[0][2])
    image += "-------------\n"
    image += "{}  |  {}  |  {}\n".format(board[1][0],board[1][1],board[1][2])
    image += "-------------\n"
    image += "{}  |  {}  |  {}\n".format(board[2][0],board[2][1],board[2][2])
    image += "\n" + '"""'
 
    return image
print(get_board_as_string(game))
print(len((1,2)))