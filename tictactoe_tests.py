#! /usr/bin/env python3

'''Tests for Tic-tac-toe game'''

from unittest import mock
from tictactoe import Tictactoe

def init_test():
    '''Tests initialization'''
    game = Tictactoe()
    is_passed = True
    for i in range(9):
        if (game.board[i] != i + 1 or
                game.x_move is not True or
                game.player_x_name != 'Player X' or
                game.player_o_name != 'Player O'):
            is_passed = False
    assert is_passed is True
    print("init_test passed")

def change_player_test():
    '''Tests changing order of moves'''
    game = Tictactoe()
    game.change_player()
    assert game.x_move is False
    game.change_player()
    assert game.x_move is True
    print("change_player_test passed")

def check_win_test():
    '''Tests checking if someone wins'''
    game = Tictactoe()
    game.board = ['X', 2, 'O', 'X', 5, 'O', 'X', 8, 9]
    # X 2 O
    # X 5 O
    # X 8 9
    assert game.check_win() is True
    game.board = ['X', 2, 'O', 'X', 5, 'O', 7, 'X', 9]
    # X 2 O
    # X 5 O
    # 7 X 9
    assert game.check_win() is False
    game.board = ['O', 'O', 'O', 'X', 5, 'X', 7, 'X', 9]
    # O O O
    # X 5 X
    # 7 X 9
    assert game.check_win() is True
    game.board = ['O', 2, 3, 'X', 'O', 6, 'X', 'X', 'O']
    # O 2 3
    # X O 6
    # X X O
    assert game.check_win() is True
    game.board = ['O', 'O', 'X', 'X', 'X', 'O', 'X', 'X', 'O']
    # O O X
    # X X O
    # X X O
    assert game.check_win() is True
    game.board = ['O', 'X', 'X', 'X', 'O', 'O', 'O', 'X', 'X']
    # O X X
    # X O O
    # O X X
    assert game.check_win() is False
    print("check_win_test passed")

def check_correct_input_test():
    '''Tests checking if the input is correct'''
    game = Tictactoe()
    game.board = ['O', 2, 3, 'X', 'O', 6, 'X', 'X', 'O']
    # O 2 3
    # X O 6
    # X X O
    not_int = 'N'
    assert game.check_correct_input(not_int) is False
    too_large_int = '10'
    assert game.check_correct_input(too_large_int) is False
    too_small_int = '0'
    assert game.check_correct_input(too_small_int) is False
    already_occupied_cell = '4'
    assert game.check_correct_input(already_occupied_cell) is False
    already_occupied_cell = '9'
    assert game.check_correct_input(already_occupied_cell) is False
    correct_input = '3'
    assert game.check_correct_input(correct_input) is True
    print("check_correct_input passed")

def make_move_test():
    '''Tests if make_move method acts correctly'''
    game = Tictactoe()
    with mock.patch('builtins.input', return_value="4"):
        game.make_move()
        assert game.board[3] == 'X'
        print("make_move_test passed")

if __name__ == "__main__":
    init_test()
    change_player_test()
    make_move_test()
    check_correct_input_test()
    check_win_test()
