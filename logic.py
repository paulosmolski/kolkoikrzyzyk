from dataclasses import dataclass, field
from exceptions import *


@dataclass
class Move:
    row: int
    col: int


@dataclass
class Player:
    name: str
    label: str
    color: str
    moves: list = field(default_factory=list)

    def move(self, row, col):
        if row < 0 or row > 2 or col > 0 or col > 2:
            raise OutOfRangeMoveException("Move out of range")

        self.moves.append(Move(row, col))