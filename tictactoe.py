#! /usr/bin/env python3

class Tictactoe(object):
    def __init__(self):
        self.board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.x_move = True
        self.player_x_name = 'Player X'
        self.player_o_name = 'Player O'

    def start(self):
        self.hello()
        self.play()
    
    def hello(self):
        print("Hello! I'm the Tic-tac-toe game.")
        print("Player X, do you want to introduce yourself? (y/n)")
        answer = input()
        if answer == 'y':
            print("Enter your name:")
            self.player_x_name = input()
            print(f"Hello, {self.player_x_name}!")
        elif answer == 'n':
            print("OK")
        print("Player O, do you want to introduce yourself? (y/n)")
        answer = input()
        if answer == 'y':
            print("Enter your name:")
            self.player_o_name = input()
            print(f"Hello, {self.player_o_name}!")
        elif answer == 'n':
            print("OK")
        print("We are ready to start!")
        print("To make a move, enter a number of the preferred cell.")
        print(f"{self.player_x_name} makes the first move.")
    
    def play(self):
        for i in range(9):
            self.draw()
            self.makeMove()
            if i >= 4 and self.checkWin() == True:
                self.end(True)
                break
            elif i == 8 and self.checkWin() == False:
                self.end(False)
            else:
                self.changePlayer()
            
    def draw(self):
        print("=====")
        for i in range(3):
            print(f"{self.board[i * 3]}|{self.board[i * 3 + 1]}|{self.board[i * 3 + 2]}")
        print("=====")       
        
    def changePlayer(self):
        if self.x_move:
            self.x_move = False
        else:
            self.x_move = True

    def makeMove(self):
        if self.x_move:
            print(f"{self.player_x_name}, make your move.")
            symbol = 'X'
        else:
            print(f"{self.player_o_name}, make your move.")
            symbol = 'O'
        while True:
            number_of_cell = input()
            if self.checkCorrectInput(number_of_cell):
                self.board[int(number_of_cell) - 1] = symbol
                break
            else:
                print("Input is incorrect, please try again.")

    def checkCorrectInput(self, input):
        is_correct = False
        for i in range(9):
            if (input == f'{self.board[i]}' and 
                    self.board[i] != 'X' and
                    self.board[i] != 'O'):
                is_correct = True
        return is_correct
               
    def checkWin(self):
        for i in range(3):
            if (self.board[i * 3] == self.board[i * 3 + 1] == self.board[i * 3 + 2] or 
                    self.board[i] == self.board[i + 3] == self.board[i + 6] or
                    self.board[0] == self.board[4] == self.board[8] or
                    self.board[2] == self.board[4] == self.board[6]):
                return True
        return False


    def end(self, if_someone_wins):
        self.draw()
        if if_someone_wins:
            if self.x_move:
                print(f"Congratulations! {self.player_x_name} wins!")
            else:
                print(f"Congratulations! {self.player_o_name} wins!")
        else:
            print("That's a draw!")
        print("Thanks for a good game.")
            
if __name__ == "__main__":
    game = Tictactoe()
    game.start()