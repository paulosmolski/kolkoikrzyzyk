from dataclasses import dataclass, field
from exceptions import *

@dataclass
class Move:
    row: int
    column: int


@dataclass
class Player:
    name: str
    label: str
    color: str
    moves: list = field(default_factory=list)

    def move(self, row, column):
        if row < 0 or row > 2 or column < 0 or column > 2:
            raise OutOfRangeMoveException("Move out of range")
        self.moves.append(Move(row, column))
