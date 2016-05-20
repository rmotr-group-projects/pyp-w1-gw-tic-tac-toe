print("hi there")
print("hey")

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
position = (1,2)
x = game['board'][position][0][1]
print(x)