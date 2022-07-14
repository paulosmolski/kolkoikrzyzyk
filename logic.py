from elements import Player, Move
from exceptions import HasWinnerException, MadeMoveExcepton
from gui import GameBoard

class Game:
    def __init__(self, master, player1: Player, player2: Player) -> None:
        # players
        self.player1 = player1
        self.player2 = player2
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
        self.show_next_player()
    
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
                    self.winner = self.player1
                    print("Has a winner")
                    self.board.winningplayer(self.player1)
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