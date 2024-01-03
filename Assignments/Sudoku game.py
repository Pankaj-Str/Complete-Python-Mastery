import tkinter as tk
from tkinter import messagebox
import random

class SudokuGame:
    def __init__(self, master):
        self.master = master
        self.master.title("Sudoku Game - codeswithpankaj")
        self.master.geometry("800x800")
        self.board = [[0]*9 for _ in range(9)]
        self.initialize_board()
        self.create_widgets()

    def initialize_board(self):
        # Generate a completed Sudoku board
        base = list(range(1, 10))
        random.shuffle(base)
        self.board[0] = base
        for i in range(1, 9):
            self.board[i] = self.shift_list(self.board[i - 1], 3)

        # Create a puzzle by removing some numbers
        for _ in range(40):
            row, col = random.randint(0, 8), random.randint(0, 8)
            self.board[row][col] = 0

    def shift_list(self, lst, n):
        return lst[n:] + lst[:n]

    def create_widgets(self):
        self.frame = tk.Frame(self.master)
        self.frame.pack(padx=10, pady=10)

        # Create Sudoku board
        self.entries = [[None]*9 for _ in range(9)]
        for i in range(9):
            for j in range(9):
                self.entries[i][j] = tk.Entry(self.frame, width=3, font=("Helvetica", 12))
                self.entries[i][j].grid(row=i, column=j)
                if self.board[i][j] != 0:
                    self.entries[i][j].insert(0, str(self.board[i][j]))
                    self.entries[i][j].config(state=tk.DISABLED)

        # Bind Enter key to the grid
        self.master.bind("<Return>", self.enter_pressed)

        # Create New Game button
        new_game_button = tk.Button(self.master, text="New Game", command=self.new_game)
        new_game_button.pack(pady=10)

    def enter_pressed(self, event):
        # Handle Enter key press event
        focused_widget = self.master.focus_get()
        for i in range(9):
            for j in range(9):
                if self.entries[i][j] == focused_widget:
                    self.button_click(i, j)

    def button_click(self, row, col):
        # Handle cell click event
        if self.board[row][col] == 0:
            try:
                entry_value = int(self.entries[row][col].get())
                if 1 <= entry_value <= 9:
                    self.board[row][col] = entry_value
                    self.entries[row][col].config(state=tk.DISABLED, disabledforeground="black")
                    if self.check_win():
                        messagebox.showinfo("Congratulations!", "You've completed the Sudoku puzzle!")
                else:
                    messagebox.showwarning("Invalid Value", "Please enter a number between 1 and 9.")
            except ValueError:
                messagebox.showwarning("Invalid Value", "Please enter a valid number.")
        else:
            messagebox.showinfo("Invalid Move", "This cell is fixed. You cannot change its value.")

    def new_game(self):
        # Reset the game with a new Sudoku board
        for i in range(9):
            for j in range(9):
                self.entries[i][j].delete(0, tk.END)
                self.entries[i][j].config(state=tk.NORMAL)
                if self.board[i][j] != 0:
                    self.entries[i][j].insert(0, str(self.board[i][j]))
                    self.entries[i][j].config(state=tk.DISABLED)

        self.initialize_board()

    def check_win(self):
        # Check if the current board is a winning configuration
        for i in range(9):
            if not self.is_valid(self.board[i]) or not self.is_valid([self.board[j][i] for j in range(9)]):
                return False

        for i in range(0, 9, 3):
            for j in range(0, 9, 3):
                if not self.is_valid(self.get_square(i, j)):
                    return False

        return True

    def is_valid(self, lst):
        # Check if a list has unique non-zero values
        lst = [x for x in lst if x != 0]
        return len(lst) == len(set(lst))

    def get_square(self, row, col):
        # Get values in a 3x3 square
        return [self.board[i][j] for i in range(row, row + 3) for j in range(col, col + 3)]

if __name__ == "__main__":
    root = tk.Tk()
    app = SudokuGame(root)
    root.mainloop()
