"""Simple Tkinter GUI for Tic-Tac-Toe vs. a Minimax AI."""
import tkinter as tk
from tkinter import messagebox

import engine
import scores as sc

HUMAN, AI = "X", "O"


class App:
    def __init__(self, root):
        self.root = root
        root.title("AI Tic-Tac-Toe")
        self.scores = sc.load()
        self.board = engine.new_board()
        self.human_first = True

        self.status = tk.Label(root, font=("Arial", 12))
        self.status.grid(row=0, column=0, columnspan=3, pady=6)

        self.buttons = []
        for i in range(9):
            b = tk.Button(root, text="", width=5, height=2, font=("Arial", 28),
                          command=lambda i=i: self.human_move(i))
            b.grid(row=1 + i // 3, column=i % 3)
            self.buttons.append(b)

        tk.Button(root, text="New Game", command=self.new_game).grid(row=4, column=0, columnspan=3, pady=6)
        self.new_game(keep_first=True)

    def update_status(self, msg=""):
        s = self.scores
        self.status.config(text=f"{msg}\nWins {s['wins']} | Losses {s['losses']} | Draws {s['draws']}")

    def new_game(self, keep_first=False):
        if not keep_first:
            self.human_first = not self.human_first
        self.board = engine.new_board()
        for b in self.buttons:
            b.config(text="", state="normal")
        self.update_status("Your turn (X)" if self.human_first else "AI is thinking...")
        if not self.human_first:
            self.root.after(300, self.ai_move)

    def human_move(self, i):
        if self.board[i] != engine.EMPTY or engine.game_over(self.board):
            return
        self.place(i, HUMAN)
        if not self.check_end():
            self.update_status("AI is thinking...")
            self.root.after(300, self.ai_move)

    def ai_move(self):
        self.place(engine.best_move(self.board, AI, HUMAN), AI)
        if not self.check_end():
            self.update_status("Your turn (X)")

    def place(self, i, mark):
        self.board[i] = mark
        self.buttons[i].config(text=mark, state="disabled")

    def check_end(self):
        if not engine.game_over(self.board):
            return False
        w = engine.winner(self.board)
        result = "win" if w == HUMAN else "loss" if w == AI else "draw"
        sc.record(self.scores, result)
        msg = {"win": "You win!", "loss": "AI wins!", "draw": "It's a draw."}[result]
        self.update_status(msg)
        for b in self.buttons:
            b.config(state="disabled")
        messagebox.showinfo("Game over", msg)
        return True


if __name__ == "__main__":
    root = tk.Tk()
    App(root)
    root.mainloop()
