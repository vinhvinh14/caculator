import tkinter as tk
from tkinter import messagebox

class TicTacToe:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Tic-Tac-Toe")
        self.current_player = "X"
        self.board = [[" " for _ in range(3)] for _ in range(3)]
        self.buttons = [[None for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.buttons[i][j] = tk.Button(self.root, text=" ", font=("Helvetica", 16), width=6, height=2,
                                              command=lambda row=i, col=j: self.click(row, col))
                self.buttons[i][j].grid(row=i, column=j)
    def click(self, row, col):
        if self.board[row][col] == " ":
            self.board[row][col] = self.current_player
            self.buttons[row][col].config(text=self.current_player, state="disabled", disabledforeground="black")
            if self.check_winner():
                messagebox.showinfo("Winner", f"Player {self.current_player} wins!")
                self.reset_game()
            elif self.is_board_full():
                messagebox.showinfo("Tie", "The game is a tie!")
                self.reset_game()
            else:
                self.current_player = "O" if self.current_player == "X" else "X"
    def check_winner(self):
        for i in range(3):
            if all(self.board[i][j] == self.current_player for j in range(3)) or all(
                    self.board[j][i] == self.current_player for j in range(3)):
                return True
        if all(self.board[i][i] == self.current_player for i in range(3)) or all(
                self.board[i][2 - i] == self.current_player for i in range(3)):
            return True
        return False
    def is_board_full(self):
        return all(self.board[i][j] != " " for i in range(3) for j in range(3))
    def reset_game(self):
        for i in range(3):
            for j in range(3):
                self.board[i][j] = " "
                self.buttons[i][j].config(text=" ", state="normal")
    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    game = TicTacToe()
    game.run()
