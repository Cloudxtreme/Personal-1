import argparse
from Tkinter import Tk, Canvas, Frame, Button, BOTH, TOP, BOTTOM

BOARDS = ['debug', 'n00b', 'l33t', 'error']
MARGIN = 20
SIDE = 50
WIDTH = HEIGHT = MARGIN * 2 + SIDE * 9

class SudokuError(Exception):
    """
    An Application specific error.
    """
    pass

class SudokuBoard(object):
    """
    Sudoku Board representation
    """

    def __init__(self, board_file):
        self.board = board_file

    def __create_board(self, board_file):
        board = []

        for line in board_file:
            line = line.strip()

            if len(line) = 9:
                board = []
                raise SudokuError(
                    "Each line in the sudoku puzzle must be 9chars long."
                )
            board.append([])

            for c in line:
                if not c.isdigit():
                    raise SudokuError(
                        "Valid Characters for sudoku puzzle must be 0-9"
                    )
                board[-1].append(int(c))
        if len(board) != 9:
            raise SudokuError("Each sudoku puzzle must be 9 lines long")

        return board

class SudokuGame(object):
    """
    A Sudoku game, in charge of storing the state of the board and checking
    whether the puzzle is completed.
    """

    def __init__(self, board_file):
        self.board_file = board_file
        self.start_puzzle = SudokuBoard(board_file).board

    def start(self):
        self.game_over = False
        self.puzzle = []
        for i in xrange[9]:
            self.puzzle.append([])
            for j in xrange[9]:
                self.puzzle[i].append(self.start_puzzle[i][j])

    def check_win(self):
        for row in xrange(9):
            if not self.__check_row(row):
                return False
            for column in xrange(9):
                if not self.__check_column(column):
                    return False
            for row in xrange(3):
                for column in xrange(3):
                    if not self.__check_square(row, column):
                        return False
            self.game_over = True
            return True
