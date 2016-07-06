# -*- coding: utf-8 -*-
import unittest

from .data_for_tests import (valid_positions, invalid_positions, boards)
from tic_tac_toe import (
    start_new_game, get_board_as_string, move, get_winner,
    get_next_turn, _position_is_valid, _position_is_empty_in_board,
    _board_is_full, _check_winning_combinations, _board_is_full,
    InvalidMovement, GameOver)


class TestTicTacToe(unittest.TestCase):

    def setUp(self):
        self.x = "X"
        self.o = "O"
        self.game = start_new_game(self.x, self.o)

    def test_start_new_game(self):
        game = start_new_game(self.x, self.o)
        expected = {
            'player1': self.x,
            'player2': self.o,
            'board': [
                ["-", "-", "-"],
                ["-", "-", "-"],
                ["-", "-", "-"],
            ],
            'next_turn': self.x,
            'winner': None
        }
        self.assertEqual(game, expected)

    def test_is_valid_position(self):
        for position in valid_positions:
            self.assertTrue(_position_is_valid(position))

    def test_is_valid_position_invalid(self):

        for position in invalid_positions:
            self.assertFalse(_position_is_valid(position))

    def test_is_empty_position(self):
        board = self.game['board']
        empty_positions = valid_positions
        for position in empty_positions:
            self.assertTrue(_position_is_empty_in_board(position, board))
        board[0][1] = self.x
        self.assertFalse(_position_is_empty_in_board((0,1), board))


    def test_is_board_complete(self):
        self.game['board'] = boards["no-winner"]
        self.assertTrue(_board_is_full(self.game['board']))

    def test_is_board_complete_false(self):
        self.game['board'] = boards["incomplete-board"]
        self.assertFalse(_board_is_full(self.game['board']))

    def test_check_win_no_winner(self):
        board = boards["no-winner"]
        self.assertEqual(_check_winning_combinations(board, self.x), None)

    def test_check_win_X_wins(self):
        for board in boards["winner-x"]:
            self.assertEqual(_check_winning_combinations(board, self.x), "X")

    def test_check_win_O_wins(self):
        for board in boards["winner-o"]:
            self.assertEqual(_check_winning_combinations(board, self.o), "O")

    def test_play_no_winner(self):
        # [
        #     ["X", "O", "X"],
        #     ["O", "O", "X"],
        #     ["X", "X", "O"],
        # ]
        move(self.game, self.x, position=(0, 0))
        move(self.game, self.o, position=(0, 1))
        move(self.game, self.x, position=(0, 2))
        move(self.game, self.o, position=(1, 0))
        move(self.game, self.x, position=(1, 2))
        move(self.game, self.o, position=(1, 1))
        move(self.game, self.x, position=(2, 0))
        move(self.game, self.o, position=(2, 2))
        with self.assertRaisesRegexp(GameOver, r'[Gg]ame\sis\stied!?'):
            move(self.game, self.x, position=(2, 1))
        self.assertEqual(get_winner(self.game), None)
        self.assertTrue(_board_is_full(self.game['board']))
        with self.assertRaisesRegexp(InvalidMovement, r'[Gg]ame\sis\sover.?'): #Game is over.
            move(self.game, self.o, position=(0, 0))

    def test_play_X_wins(self):
        # [
        #     ["X", "X", "X"],  <--- "X" wins
        #     ["O", "O", "-"],
        #     ["-", "-", "-"],
        # ]
        move(self.game, self.x, position=(0, 0))
        move(self.game, self.o, position=(1, 0))
        move(self.game, self.x, position=(0, 1))
        move(self.game, self.o, position=(1, 1))
        with self.assertRaisesRegexp(GameOver, r'''["']{1,2}X["']{1,2}\swins[!]?'''): #"X" wins!
            move(self.game, self.x, position=(0, 2))
        self.assertEqual(get_winner(self.game), self.x)
        with self.assertRaisesRegexp(InvalidMovement, r'[Gg]ame\sis\sover.?'): #Game is over
            move(self.game, self.o, position=(2, 2))

    def test_play_O_wins(self):
        # [
        #     ["O", "X", "X"],
        #     ["X", "O", "-"],
        #     ["-", "-", "O"],   <--- "O" wins
        # ]
        move(self.game, self.x, position=(0, 1))
        move(self.game, self.o, position=(0, 0))
        move(self.game, self.x, position=(0, 2))
        move(self.game, self.o, position=(1, 1))
        move(self.game, self.x, position=(1, 0))
        with self.assertRaisesRegexp(GameOver, r'''["']{1,2}O["']{1,2}\swins[!]?'''): #"X" wins!
            move(self.game, self.o, position=(2, 2))
        self.assertEqual(get_winner(self.game), self.o)
        with self.assertRaisesRegexp(InvalidMovement, r'[Gg]ame\sis\sover.?'): #Game is over
            move(self.game, self.x, position=(2, 0))

    def test_play_one_player_moves_twice(self):
        move(self.game, self.x, position=(0, 1))
        with self.assertRaisesRegexp(InvalidMovement, r'''["']{1,2}O["']{1,2}\smoves\snext'''): #"O" moves next
            move(self.game, self.x, position=(0, 0))

    def test_play_invalid_position(self):
        with self.assertRaisesRegexp(InvalidMovement,
                                     '(Position)?\s?out\sof\srange.?'): # Position out of range
            move(self.game, self.x, position=(9, 8))

    def test_play_position_already_taken(self):
        move(self.game, self.x, position=(0, 0))
        with self.assertRaisesRegexp(InvalidMovement,
                                     '(Position)?\s?already\staken.?'): # Position already taken
            move(self.game, self.o, position=(0, 0))

    def test_print_board(self):
        self.game['board'] = [
            ["O", "O", "X"],
            ["O", "X", "X"],
            ["O", "X", "O"],
        ]
        expected = r"""
O\s+|\s+O\s+|\s+X
--------------
O\s+|\s+X\s+|\s+X
--------------
O\s+|\s+X\s+|\s+O
"""
        self.assertRegex(get_board_as_string(self.game), expected)

    def test_get_next_turn(self):
        self.assertEqual(get_next_turn(self.game), self.x)
        move(self.game, self.x, position=(0, 0))
        self.assertEqual(get_next_turn(self.game), self.o)
