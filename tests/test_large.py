# -*- coding: utf-8 -*-

import unittest

from tic_tac_toe import (
    start_new_game, get_board_as_string, move, get_winner,
    get_next_turn, _position_is_valid, _position_is_empty_in_board,
    _board_is_full, _check_winning_combinations, _board_is_full,
    InvalidMovement, GameOver)


class LargeTicTacToeTestCase(unittest.TestCase):

    def setUp(self):
        self.x = "X"
        self.o = "O"
        self.game_large = start_new_game(self.x, self.o, 4)

    def test_start_new_game_large(self):
        game = self.game_large
        expected = {
            'player1': self.x,
            'player2': self.o,
            'board': [
                ["-", "-", "-", "-"],
                ["-", "-", "-", "-"],
                ["-", "-", "-", "-"],
                ["-", "-", "-", "-"]
            ],
            'next_turn': self.x,
            'winner': None
        }
        self.assertEqual(game, expected)
        
    def test_is_valid_position_large(self):
        game = self.game_large
        valid_positions = [
            (0,0), (0,1), (0,2), (0,3),
            (1,0), (1,1), (1,2), (1,3),
            (2,0), (2,1), (2,2), (2,3),
            (3,0), (3,1), (3,2), (3,3)
        ]
        for position in valid_positions:
            self.assertTrue(_position_is_valid(game, position))
            
    def test_is_valid_position_invalid_large(self):
        n = len(self.game_large['board'])
        invalid_positions = [
            (n,3), (n,2), (n,3), (9,9), (-1,-1), 1, "something", False, (0,0,0)
        ]
        for position in invalid_positions:
            self.assertFalse(_position_is_valid(self.game_large, position))
            
    def test_is_empty_position(self):
        board = self.game_large['board']
        empty_positions = [
            (0,0), (0,1), (0,2), (0,3),
            (1,0), (1,1), (1,2), (1,3),
            (2,0), (2,1), (2,2), (2,3),
            (3,0), (3,1), (3,2), (3,3),
        ]
        for position in empty_positions:
            self.assertTrue(_position_is_empty_in_board(position, board))
        board[0][1] = self.x
        self.assertFalse(_position_is_empty_in_board((0,1), board))
            
    def test_is_board_complete(self):
        self.game_large['board'] = [
            ["X", "X", "O", "O"],
            ["O", "O", "X", "X"],
            ["O", "O", "X", "O"],
            ["O", "O", "O", "X"],
        ]
        self.assertTrue(_board_is_full(self.game_large['board']))

    def test_is_board_complete_false(self):
        self.game_large['board'] = [
            ["X", "X", "O", "O"],
            ["O", "O", "-", "X"],
            ["-", "O", "X", "O"],
            ["O", "-", "O", "X"],
        ]
        self.assertFalse(_board_is_full(self.game_large['board']))
            
    def test_check_win_no_winner_large(self):
        board = [
            ["X", "X", "O", "O"],
            ["O", "O", "X", "X"],
            ["O", "O", "X", "O"],
            ["O", "O", "O", "X"],
        ]
        self.assertEqual(_check_winning_combinations(board, self.x), None)
            
    def test_check_win_X_wins_large(self):
        # diagonals
        board = [
            ["X", "O", "O", "O"],
            ["O", "X", "X", "X"],
            ["O", "O", "X", "O"],
            ["O", "O", "X", "X"],
        ]
        self.assertEqual(_check_winning_combinations(board, self.x), "X")
        board = [
            ["X", "O", "O", "X"],
            ["O", "X", "X", "X"],
            ["O", "X", "X", "O"],
            ["X", "O", "X", "O"],
        ]
        self.assertEqual(_check_winning_combinations(board, self.x), "X")
        # horizontals
        board = [
            ["X", "X", "X", "X"],
            ["O", "X", "X", "X"],
            ["O", "O", "O", "O"],
            ["O", "O", "X", "X"],
        ]
        self.assertEqual(_check_winning_combinations(board, self.x), "X")
        board = [
            ["X", "O", "O", "O"],
            ["X", "X", "X", "X"],
            ["O", "O", "X", "O"],
            ["O", "O", "X", "O"],
        ]
        self.assertEqual(_check_winning_combinations(board, self.x), "X")
        board = [
            ["X", "O", "O", "O"],
            ["O", "O", "X", "X"],
            ["X", "X", "X", "X"],
            ["O", "O", "X", "X"],
        ]
        self.assertEqual(_check_winning_combinations(board, self.x), "X")
        board = [
            ["X", "O", "O", "O"],
            ["O", "O", "X", "X"],
            ["X", "X", "O", "X"],
            ["X", "X", "X", "X"],
        ]
        self.assertEqual(_check_winning_combinations(board, self.x), "X")
        # verticals
        board = [
            ["X", "O", "O", "X"],
            ["O", "O", "X", "X"],
            ["X", "X", "O", "X"],
            ["O", "O", "X", "X"],
        ]
        self.assertEqual(_check_winning_combinations(board, self.x), "X")
        board = [
            ["X", "O", "X", "O"],
            ["O", "O", "X", "X"],
            ["X", "O", "X", "X"],
            ["X", "X", "X", "O"],
        ]
        self.assertEqual(_check_winning_combinations(board, self.x), "X")
        board = [
            ["X", "X", "O", "O"],
            ["O", "X", "X", "X"],
            ["X", "X", "O", "X"],
            ["X", "X", "X", "O"],
        ]
        self.assertEqual(_check_winning_combinations(board, self.x), "X")
        board = [
            ["X", "X", "O", "O"],
            ["X", "X", "O", "X"],
            ["X", "O", "O", "X"],
            ["X", "X", "X", "O"],
        ]
        self.assertEqual(_check_winning_combinations(board, self.x), "X")

    def test_check_win_O_wins_large(self):
        # diagonals
        board = [
            ["O", "X", "X", "X"],
            ["X", "O", "O", "O"],
            ["X", "X", "O", "O"],
            ["X", "X", "O", "O"]
        ]
        self.assertEqual(_check_winning_combinations(board, self.o), "O")
        board = [
            ["O", "X", "X", "O"],
            ["X", "O", "O", "O"],
            ["X", "O", "O", "O"],
            ["O", "X", "O", "X"]
        ]
        self.assertEqual(_check_winning_combinations(board, self.o), "O")
        # horizontals
        board = [
            ["O", "O", "O", "O"],
            ["X", "O", "O", "O"],
            ["X", "X", "X", "O"],
            ["X", "X", "O", "X"]
        ]
        self.assertEqual(_check_winning_combinations(board, self.o), "O")
        board = [
            ["O", "X", "X", "X"],
            ["O", "O", "O", "O"],
            ["X", "X", "O", "O"],
            ["X", "X", "O", "X"]
        ]
        self.assertEqual(_check_winning_combinations(board, self.o), "O")
        board = [
            ["O", "X", "X", "X"],
            ["X", "O", "O", "O"],
            ["O", "O", "O", "O"],
            ["X", "X", "O", "X"]
        ]
        self.assertEqual(_check_winning_combinations(board, self.o), "O")
        board = [
            ["O", "X", "X", "X"],
            ["X", "X", "O", "O"],
            ["X", "X", "O", "O"],
            ["O", "O", "O", "O"]
        ]
        self.assertEqual(_check_winning_combinations(board, self.o), "O")
        # verticals
        board = [
            ["O", "X", "X", "O"],
            ["X", "X", "O", "O"],
            ["X", "X", "O", "O"],
            ["O", "O", "X", "O"]
        ]
        self.assertEqual(_check_winning_combinations(board, self.o), "O")
        board = [
            ["O", "X", "O", "X"],
            ["X", "X", "O", "O"],
            ["X", "X", "O", "O"],
            ["O", "O", "O", "X"]
        ]
        self.assertEqual(_check_winning_combinations(board, self.o), "O")
        board = [
            ["O", "O", "X", "X"],
            ["X", "O", "O", "O"],
            ["X", "O", "X", "O"],
            ["O", "O", "X", "O"]
        ]
        self.assertEqual(_check_winning_combinations(board, self.o), "O")
        board = [
            ["O", "O", "X", "X"],
            ["O", "X", "O", "O"],
            ["O", "O", "X", "O"],
            ["O", "O", "X", "O"]
        ]
        self.assertEqual(_check_winning_combinations(board, self.o), "O")
            
    def test_play_no_winner_large(self):
        # [
        #     ["X", "O", "X", "O"],
        #     ["O", "O", "X", "O"],
        #     ["X", "X", "O", "X"],
        #     ["X", "X", "O", "O"],
        # ]
        move(self.game_large, self.x, position=(0, 0))
        move(self.game_large, self.o, position=(0, 1))
        move(self.game_large, self.x, position=(0, 2))
        move(self.game_large, self.o, position=(1, 0))
        move(self.game_large, self.x, position=(1, 2))
        move(self.game_large, self.o, position=(1, 1))
        move(self.game_large, self.x, position=(2, 0))
        move(self.game_large, self.o, position=(2, 2))
        move(self.game_large, self.x, position=(2, 3))
        move(self.game_large, self.o, position=(0, 3))
        move(self.game_large, self.x, position=(3, 1))
        move(self.game_large, self.o, position=(1, 3))
        move(self.game_large, self.x, position=(3, 0))
        move(self.game_large, self.o, position=(3, 3))
        move(self.game_large, self.x, position=(3, 2))
        with self.assertRaisesRegexp(GameOver, 'Game is tied!'):
            move(self.game_large, self.o, position=(2, 1))
        self.assertEqual(get_winner(self.game_large), None)
        self.assertTrue(_board_is_full(self.game_large['board']))
        with self.assertRaisesRegexp(InvalidMovement, 'Game is over.'):
            move(self.game_large, self.x, position=(0, 0))
            
    def test_play_X_wins_large(self):
        # [
        #     ["X", "X", "X", "X"],  <--- "X" wins
        #     ["O", "O", "O", "-"],
        #     ["-", "-", "-", "-"],
        #     ["-", "-", "-", "-"],
        # ]
        move(self.game_large, self.x, position=(0, 3))
        move(self.game_large, self.o, position=(1, 2))
        move(self.game_large, self.x, position=(0, 0))
        move(self.game_large, self.o, position=(1, 0))
        move(self.game_large, self.x, position=(0, 1))
        move(self.game_large, self.o, position=(1, 1))
        with self.assertRaisesRegexp(GameOver, '"X" wins!'):
            move(self.game_large, self.x, position=(0, 2))
        self.assertEqual(get_winner(self.game_large), self.x)
        with self.assertRaisesRegexp(InvalidMovement, 'Game is over'):
            move(self.game_large, self.o, position=(2, 2))
            
    def test_play_O_wins_large(self):
        # [
        #     ["O", "X", "X", "-"],
        #     ["X", "O", "-", "-"],
        #     ["", "-", "O", "-"],
        #     ["-", "-", "-", "O"],   <--- "O" wins
        # ]
        move(self.game_large, self.x, position=(0, 1))
        move(self.game_large, self.o, position=(0, 0))
        move(self.game_large, self.x, position=(0, 2))
        move(self.game_large, self.o, position=(1, 1))
        move(self.game_large, self.x, position=(1, 0))
        move(self.game_large, self.o, position=(3, 3))
        move(self.game_large, self.x, position=(2, 0))
        with self.assertRaisesRegexp(GameOver, '"O" wins!'):
            move(self.game_large, self.o, position=(2, 2))
        self.assertEqual(get_winner(self.game_large), self.o)
        with self.assertRaisesRegexp(InvalidMovement, 'Game is over'):
            move(self.game_large, self.x, position=(2, 0))
            
    def test_play_invalid_position_large(self):
        with self.assertRaisesRegexp(InvalidMovement,
                                     'Position out of range.'):
            move(self.game_large, self.x, position=(0, 4))
            
    def test_print_board_large(self):
        self.game_large['board'] = [
            ["O", "O", "X", "O"],
            ["O", "X", "X", "X"],
            ["O", "X", "O", "O"],
            ["O", "X", "O", "O"],
        ]
        expected = """
O  |  O  |  X  |  O
--------------------
O  |  X  |  X  |  X
--------------------
O  |  X  |  O  |  O
--------------------
O  |  X  |  O  |  O
"""
        self.assertEqual(get_board_as_string(self.game_large), expected)
