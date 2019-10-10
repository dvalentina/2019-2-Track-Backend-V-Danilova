#! /usr/bin/env python3

'''Tests for Tic-tac-toe game'''

import unittest
from unittest import mock
from tictactoe import Tictactoe

class TestTictactoeGame(unittest.TestCase):
    '''Class for Tic-tac-toe tests'''
    def test_init(self):
        '''Tests initialization'''
        game = Tictactoe()
        is_passed = True
        for i in range(9):
            if (game.board[i] != i + 1 or
                    game.x_move is not True or
                    game.player_x_name != 'Player X' or
                    game.player_o_name != 'Player O'):
                is_passed = False
        self.assertEqual(is_passed, True)

    def test_change_player(self):
        '''Tests changing order of moves'''
        game = Tictactoe()
        game.change_player()
        self.assertEqual(game.x_move, False)
        game.change_player()
        self.assertEqual(game.x_move, True)

    def test_check_win(self):
        '''Tests checking if someone wins'''
        game = Tictactoe()
        game.board = ['X', 2, 'O', 'X', 5, 'O', 'X', 8, 9]
        # X 2 O
        # X 5 O
        # X 8 9
        self.assertEqual(game.check_win(), True)
        game.board = ['X', 2, 'O', 'X', 5, 'O', 7, 'X', 9]
        # X 2 O
        # X 5 O
        # 7 X 9
        self.assertEqual(game.check_win(), False)
        game.board = ['O', 'O', 'O', 'X', 5, 'X', 7, 'X', 9]
        # O O O
        # X 5 X
        # 7 X 9
        self.assertEqual(game.check_win(), True)
        game.board = ['O', 2, 3, 'X', 'O', 6, 'X', 'X', 'O']
        # O 2 3
        # X O 6
        # X X O
        self.assertEqual(game.check_win(), True)
        game.board = ['O', 'O', 'X', 'X', 'X', 'O', 'X', 'X', 'O']
        # O O X
        # X X O
        # X X O
        self.assertEqual(game.check_win(), True)
        game.board = ['O', 'X', 'X', 'X', 'O', 'O', 'O', 'X', 'X']
        # O X X
        # X O O
        # O X X
        self.assertEqual(game.check_win(), False)

    def test_check_correct_input(self):
        '''Tests checking if the input is correct'''
        game = Tictactoe()
        game.board = ['O', 2, 3, 'X', 'O', 6, 'X', 'X', 'O']
        # O 2 3
        # X O 6
        # X X O
        not_int = 'N'
        self.assertEqual(game.check_correct_input(not_int), False)
        too_large_int = '10'
        self.assertEqual(game.check_correct_input(too_large_int), False)
        too_small_int = '0'
        self.assertEqual(game.check_correct_input(too_small_int), False)
        already_occupied_cell = '4'
        self.assertEqual(game.check_correct_input(already_occupied_cell), False)
        already_occupied_cell = '9'
        self.assertEqual(game.check_correct_input(already_occupied_cell), False)
        correct_input = '3'
        self.assertEqual(game.check_correct_input(correct_input), True)

    def test_make_move(self):
        '''Tests if make_move method acts correctly'''
        game = Tictactoe()
        with mock.patch('builtins.input', return_value="4"):
            game.make_move()
            self.assertEqual(game.board[3], 'X')

if __name__ == "__main__":
    unittest.main()
