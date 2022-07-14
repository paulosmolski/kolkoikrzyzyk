import tkinter as tk
from logic import Game
from elements import Player

if __name__ == "__main__":
    root = tk.Tk()
    root.minsize(500, 500)
    pl1 = Player("Marek", "X", "red")
    pl2 = Player("Aviv", "O", "blue")
    game = Game(root, pl1, pl2)
    game.board.pack(expand=True, fill="both")
    root.mainloop()