#! /usr/bin/env python3

from tictactoe import Tictactoe

# ===============================
# tests
# ===============================

def initTest():
    game = Tictactoe()
    is_passed = True
    for i in range(9):
        if (game.board[i] != i + 1 or
                game.x_move != True or
                game.player_x_name != 'Player X' or
                game.player_o_name != 'Player O'):
            is_passed = False
    assert is_passed == True
    print("initTest passed")

def changePlayerTest():
    game = Tictactoe()
    game.changePlayer()
    assert game.x_move == False
    game.changePlayer()
    assert game.x_move == True
    print("changePlayerTest passed")

def checkWinTest():
    game = Tictactoe()
    game.board = ['X', 2, 'O', 'X', 5, 'O', 'X', 8, 9]
    # X 2 O
    # X 5 O
    # X 8 9
    assert game.checkWin() == True
    game.board = ['X', 2, 'O', 'X', 5, 'O', 7, 'X', 9]
    # X 2 O
    # X 5 O
    # 7 X 9
    assert game.checkWin() == False
    game.board = ['O', 'O', 'O', 'X', 5, 'X', 7, 'X', 9]
    # O O O
    # X 5 X
    # 7 X 9
    assert game.checkWin() == True 
    game.board = ['O', 2, 3, 'X', 'O', 6, 'X', 'X', 'O']
    # O 2 3
    # X O 6
    # X X O
    assert game.checkWin() == True  
    game.board = ['O', 'O', 'X', 'X', 'X', 'O', 'X', 'X', 'O']
    # O O X
    # X X O
    # X X O
    assert game.checkWin() == True  
    game.board = ['O', 'X', 'X', 'X', 'O', 'O', 'O', 'X', 'X']
    # O X X
    # X O O
    # O X X
    assert game.checkWin() == False
    print("checkWinTest passed")

def checkCorrectInputTest():
    game = Tictactoe()
    game.board = ['O', 2, 3, 'X', 'O', 6, 'X', 'X', 'O']
    # O 2 3
    # X O 6
    # X X O
    not_int = 'N'
    assert game.checkCorrectInput(not_int) == False
    too_large_int = '10'
    assert game.checkCorrectInput(too_large_int) == False
    too_small_int = '0'
    assert game.checkCorrectInput(too_small_int) == False
    already_occupied_cell = '4'
    assert game.checkCorrectInput(already_occupied_cell) == False
    already_occupied_cell = '9'
    assert game.checkCorrectInput(already_occupied_cell) == False
    correct_input = '3'
    assert game.checkCorrectInput(correct_input) == True
    print("checkCorrectInput passed")

from unittest import mock
from unittest.mock import patch

def makeMoveTest():
    game = Tictactoe()
    with mock.patch('builtins.input', return_value = "4"):
        game.makeMove()
        assert game.board[3] == 'X'
        print("makeMoveTest passed")

if __name__ == "__main__":
    initTest()
    changePlayerTest()
    makeMoveTest()
    checkCorrectInputTest()
    checkWinTest()