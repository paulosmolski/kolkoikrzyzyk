import tkinter as tk
from exceptions import PlayersException
from collections import deque
from logic import Game
from gui import StartUp

class TicTacToe(tk.Tk):
    def __init__(self, *nargs, **kwargs) -> None:
        super().__init__(*nargs, **kwargs)
        self.minsize(500, 500)
        self.games = []
        self.players = deque([], 2)
        self.startup = StartUp(self)
        self.startup.set_game(self)
        self.startup.pack(fill="x")
    def next_game(self):
        if len(self.players) != 2:
            raise PlayersException("Wrong players, cannot start game")
        game = Game(self, self, *self.players)
        try:
            self.games[-1].pack_forget()
        except (IndexError, AttributeError):
            pass
        self.games.append(game)
        self.players.append(self.players[0])
        game.pack(expand=True, fill="both")
    def set_players(self, player1, player2):
        self.players.append(player1)
        self.players.append(player2)
        self.next_game()

    @property
    def winners(self):
        return [game.winner for game in self.games]

if __name__ == "__main__":
    a = TicTacToe()
    a.mainloop()