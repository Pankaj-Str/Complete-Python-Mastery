import tkinter as tk
from tkinter import messagebox
import random

class TicTacToeGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Tic-Tac-Toe Game - Codes With Pankaj")

        # Player Names
        self.player1_name = "Codes With Pankaj"
        self.player2_name = "Computer"

        # Game Variables
        self.current_player = "X"
        self.board = [""] * 9  # Represents the Tic-Tac-Toe board

        # GUI Components
        self.create_game_board()

    def create_game_board(self):
        self.buttons = [[None, None, None] for _ in range(3)]

        for i in range(3):
            for j in range(3):
                button = tk.Button(
                    self.root,
                    text="",
                    font=("Arial", 18),
                    width=8,
                    height=4,
                    command=lambda row=i, col=j: self.make_move(row, col),
                )
                button.grid(row=i, column=j, padx=5, pady=5)
                self.buttons[i][j] = button

        reset_button = tk.Button(self.root, text="Reset Game", command=self.reset_game)
        reset_button.grid(row=3, column=0, columnspan=3, pady=10)

    def make_move(self, row, col):
        index = row * 3 + col
        if self.board[index] == "" and not self.check_winner():
            self.board[index] = self.current_player
            self.update_button(row, col)

            if self.check_winner():
                messagebox.showinfo("Game Over", f"{self.get_current_player_name()} wins!")
                self.reset_game()
            elif "" not in self.board:
                messagebox.showinfo("Game Over", "It's a draw!")
                self.reset_game()
            else:
                self.switch_player()

    def update_button(self, row, col):
        button = self.buttons[row][col]
        button.config(text=self.current_player, state="disabled")

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"
        if self.current_player == "O":
            self.computer_move()

    def computer_move(self):
        empty_cells = [i for i in range(9) if self.board[i] == ""]
        if empty_cells:
            index = random.choice(empty_cells)
            row, col = divmod(index, 3)
            self.make_move(row, col)

    def check_winner(self):
        # Check rows, columns, and diagonals for a winner
        for i in range(3):
            if self.board[i] == self.board[i + 3] == self.board[i + 6] != "":
                return True
            if self.board[i * 3] == self.board[i * 3 + 1] == self.board[i * 3 + 2] != "":
                return True
        if self.board[0] == self.board[4] == self.board[8] != "":
            return True
        if self.board[2] == self.board[4] == self.board[6] != "":
            return True
        return False

    def get_current_player_name(self):
        return self.player1_name if self.current_player == "X" else self.player2_name

    def reset_game(self):
        for i in range(3):
            for j in range(3):
                self.buttons[i][j].config(text="", state="active")
        self.board = [""] * 9
        self.current_player = "X"

if __name__ == "__main__":
    root = tk.Tk()
    tic_tac_toe_app = TicTacToeGame(root)
    root.mainloop()
