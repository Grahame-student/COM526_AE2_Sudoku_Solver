from unittest import TestCase
from hamcrest import *

from sudoku_grid import SudokuGrid


class TestGrid(TestCase):
    def test_constraints_broken_returns_true_when_domain_list_empty(self):
        puzzle = "........................................................................"
        grid = SudokuGrid(puzzle)
        # All domains will be set to [1,2,3,4,5,6,7,8,9] at this point

        grid.grid[0]["domains"] = []

        assert_that(grid.constraints_broken(), is_(True))
