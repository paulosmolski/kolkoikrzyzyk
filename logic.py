from elements import Player, Move
from exceptions import HasWinnerException, MadeMoveExcepton
from gui import GameBoard
import time

class Game:
    def __init__(self, master, main, player1: Player, player2: Player) -> None:
        # set main
        self.main = main
        # measure time
        self.timetaken = None
        self.start = time.time()
        # players
        self.player1 = player1
        self.player2 = player2
        self.player1.new_instance()
        self.player2.new_instance()
        # winning combinations
        self.win_comb = []
        self.win_comb.extend([Move(row, col) for col in range(3)] for row in range(3))
        self.win_comb.extend([Move(row, col) for row in range(3)] for col in range(3))
        self.win_comb.append([Move(x, x) for x in range(3)])
        self.win_comb.append([Move(2-x, x) for x in range(3)])
        # winner
        self.winner = None
        # moves
        self.all_moves = []
        # board
        self.board = GameBoard(master)
        self.board.set_game(self)
        self.board.set_main(self.main)
        self.board.bottom_panel()
        self.show_next_player()
    
    def __getattr__(self, attr):
        return getattr(self.board, attr)
    
    @property
    def player1_moves(self):
        return self.player1.all_moves
    
    @property
    def player2_moves(self):
        return self.player2.all_moves
    
    def check_winner(self):
        if self.winner:
            raise HasWinnerException("Game already has a winner")

    def check_move(self, move):
        self.check_winner()
        if move in self.all_moves:
            raise MadeMoveExcepton("Move already made")
    
    def next_player(self):
        try:
            self.check_winner()
            old = self.player1
            self.player1 = self.player2
            self.player2 = old
        except HasWinnerException:
            pass

    def find_winner(self):
        try:
            self.check_winner()
            for comb in self.win_comb:
                if all(move in self.player1_moves for move in comb):
                    self.end = time.time()
                    self.timetaken = self.end - self.start
                    self.winner = self.player1
                    self.winner.won()
                    print(f"Player {self.winner.name} won in {self.timetaken} seconds")
                    self.board.winningplayer(self.winner)
                    break
        except HasWinnerException:
            pass
    
    def show_next_player(self):
        try:
            self.check_winner()
            self.board.nextplayer(self.player1)
        except HasWinnerException:
            pass
    
    def add_move(self, move):
        self.check_move(move)
        self.all_moves.append(move)
        self.player1.all_moves.append(move)
        self.board.click_button(move, self.player1)
        self.find_winner()
        self.next_player()
        self.show_next_player()
