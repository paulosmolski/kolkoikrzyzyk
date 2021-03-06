import tkinter as tk
from elements import Player, Move
from exceptions import WrongPlayerException

class GameBoard(tk.Frame):
    def __init__(self, *nargs, **kwargs):
        super().__init__(*nargs, **kwargs)
        self.buttons = [[None for x in range(3)] for y in range(3)]
        self.create_buttons(text="", highlightbackground="grey")
        self.game = None

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
    
    def set_main(self, main):
        self.main = main

    def message(self, player: Player, message):
        self.curname.set(message)
        self.namelabel.config(fg=player.color)

    def nextplayer(self, player: Player):
        self.message(player, f"{player.name} moves")
    
    def winningplayer(self, player: Player):
        self.message(player, f"{player.name} won")
    
    def bottom_panel(self):
        self.panel = tk.Frame(self)
        for x in range(4):
            self.panel.columnconfigure(x, weight=1)
        self.scorepl1 = tk.Label(self.panel, text=f"{self.game.player1.name}: {self.game.player1.victories}", fg=self.game.player1.color)
        self.scorepl1.grid(column=0, row=0)
        self.scorepl2 = tk.Label(self.panel, text=f"{self.game.player2.name}: {self.game.player2.victories}", fg=self.game.player2.color)
        self.scorepl2.grid(column=1, row=0)
        self.curname = tk.StringVar()
        self.namelabel = tk.Label(self.panel, textvariable=self.curname)
        self.namelabel.grid(column=2, row=0)
        self.nextbutton = tk.Button(self.panel, text="Next game", command=self.main.next_game)
        self.nextbutton.grid(column=3, row=0)
        self.panel.grid(column=0, row=3, columnspan=3, sticky="nesw")

class StartUp(tk.Frame):
    def __init__(self, *nargs, **kwargs):
        super().__init__(*nargs, **kwargs)
        self.pl1 = tk.LabelFrame(self, text="Player 1")
        self.pl2 = tk.LabelFrame(self, text="Player 2")
        self.players = [self.pl1, self.pl2]
        self.labels = ["X", "O", "+", "=", "*"]
        self.colors = ["red", "blue", "green", "pink", "violet", "orange"]
        tk.Label(self, text="Tic Tac Toe").pack()
        for player in self.players:
            tk.Label(player, text="What's your name").pack()
            player.namefield = tk.Entry(player, width=40)
            player.namefield.insert(0, player.cget("text"))
            player.namefield.pack()
            tk.Label(player, text="Choose your label").pack()
            player.label = tk.StringVar()
            player.label.set(self.labels[self.players.index(player)])
            tk.OptionMenu(player, player.label, *self.labels).pack()
            tk.Label(player, text="Choose your color").pack()
            player.color = tk.StringVar()
            player.color.set(self.colors[self.players.index(player)])
            tk.OptionMenu(player, player.color, *self.colors).pack()
            player.pack()
        self.button = tk.Button(self, text="Next", command=self.get_players)
        self.button.pack()
        self.messagestr = tk.StringVar()
        tk.Label(self, textvariable=self.messagestr, fg="red").pack()

    def get_players(self):
        name1 = self.pl1.namefield.get()
        name2 = self.pl2.namefield.get()
        label1 = self.pl1.label.get()
        label2 = self.pl2.label.get()
        color1 = self.pl1.color.get()
        color2 = self.pl2.color.get()
        if name1 == name2 or name1 == "" or name2 == "" or label1 == label2 or color1 == color2:
            self.messagestr.set("Wrong players choice")
            raise WrongPlayerException("Wrong players choice")
        self.messagestr.set("")
        pl1 = Player(name1, label1, color1)
        pl2 = Player(name2, label2, color2)
        print([pl1, pl2])
        self.game.set_players(pl1, pl2)
        self.pack_forget()
    
    def set_game(self, game):
        self.game = game
    
class History(tk.Frame):
    def __init__(self, game, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.game = game
        self.games = game.games

class Menu(tk.Frame):
    pass