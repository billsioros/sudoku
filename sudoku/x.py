
from pulp import *

from sudoku import classic


class SudokuXLP(classic.SudokuLP):

    def __init__(self, matrix):

        super().__init__(matrix)

        for k in range(self.n):

            self += lpSum([
                self.x[r][r][k] for r in range(self.n)
            ]) == 1, f"in the diagonal only one {k + 1}"

        for k in range(self.n):

            self += lpSum([
                self.x[r][self.n - 1 - r][k] for r in range(self.n)
            ]) == 1, f"in the anti diagonal only one {k + 1}"
