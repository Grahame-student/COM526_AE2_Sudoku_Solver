from unittest import TestCase
from hamcrest import *
from mock import patch

from sudoku_grid import SudokuGrid
from tree_node import TreeNode


class TestTree(TestCase):
    def test_find_solution_returns_true_when_grid_is_solved(self):
        with patch('sudoku_grid.SudokuGrid') as mock:
            grid = mock
            grid.result.return_value = "Solved"
            grid.constraints_broken.return_value = False
            grid.cull.return_value = False

            root = TreeNode()
            solved, solution = root.find_solution(grid)

            assert_that(solved, is_(True))

    def test_find_solution_returns_solved_grid(self):
        puzzle = "198543726643278591527619843914735268876192435235486179462351987381927654759864312"
        grid = SudokuGrid(puzzle)
        root = TreeNode()

        solved, solution = root.find_solution(grid)

        assert_that(solution.get_puzzle_state(), is_(puzzle))

    def test_find_solution_solves_incomplete_puzzle_with_single_number_missing(self):
        puzzle = "19854372664327859152761984391473526887619243523548617946235198738192765475986431."
        grid = SudokuGrid(puzzle)
        root = TreeNode()

        solved, solution = root.find_solution(grid)

        assert_that(solved, is_(True))

    def test_find_solution_solves_incomplete_puzzle_with_multiple_numbers_missing(self):
        puzzle = ".4.1..............653.....1.8.9..74...24..91.......2.8...562....1..7..6...4..1..3"
        grid = SudokuGrid(puzzle)
        root = TreeNode()

        solved, solution = root.find_solution(grid)

        assert_that(solved, is_(True))
