from dataclasses import dataclass, field
from exceptions import *

@dataclass
class Move:
    row: int
    col: int
    def __post_init__(self):
        for x in self.row, self.col:
            if x < 0 or x > 2:
                raise OutOfRangeMoveException("Move out of range")

@dataclass
class Player:
    name: str
    label: str
    color: str
    all_moves: list = field(default_factory=list)

    def add_move(self, move: Move):
        self.moves.append(move)