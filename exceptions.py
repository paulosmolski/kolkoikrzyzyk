class TicTacToeException(Exception):
    pass

class WrongMoveException(TicTacToeException):
    pass

class OutOfRangeMoveException(WrongMoveException):
    pass

class GameException(TicTacToeException):
    pass

class HasWinnerException(GameException):
    pass

class MadeMoveExcepton(GameException):
    pass