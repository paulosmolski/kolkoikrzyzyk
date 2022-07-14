import tkinter as tk
from elements import Player, Move

class GameBoard(tk.Frame):
    def __init__(self, *nargs, **kwargs):
        super().__init__(*nargs, **kwargs)
        self.buttons = [[None for x in range(3)] for y in range(3)]
        self.create_buttons(text="", highlightbackground="grey")
        self.game = None
        self.curname = tk.StringVar()
        self.namelabel = tk.Label(self, textvariable=self.curname)
        self.namelabel.grid(row=3, column=0, columnspan=3)

    def create_buttons(self, **kwargs):
        maxrow = 3
        maxcol = 3
        for row in range(maxrow):
            for col in range(maxcol):
                self.buttons[row][col] = tk.Button(self, command=lambda row=row, col=col: self.reg_click(row, col), **kwargs)
                button = self.buttons[row][col]
                button.grid(row=row, column=col, padx=5, pady=5, sticky="nesw")
            for x in range(maxrow):
                self.columnconfigure(x, weight=1)
            for x in range(maxcol):
                self.rowconfigure(x, weight=1)

    def click_button(self, move: Move, player: Player):
        row, col = move.row, move.col
        button = self.buttons[row][col]
        button.config(highlightbackground=player.color)
        button.config(fg=player.color)
        button.config(text=player.label)
    
    def reg_click(self, row, col):
        self.game.add_move(Move(row, col))
    
    def set_game(self, game):
        self.game = game

    def message(self, player: Player, message):
        self.curname.set(message)
        self.namelabel.config(fg=player.color)

    def nextplayer(self, player: Player):
        self.message(player, player.name)
    
    def winningplayer(self, player: Player):
        self.message(player, f"Wygrał: {player.name}")

class StartUp(tk.Frame):
    pass