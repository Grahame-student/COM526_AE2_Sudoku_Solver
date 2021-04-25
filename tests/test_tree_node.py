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
        base_domain = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        grid = SudokuGrid(puzzle, base_domain)
        root = TreeNode()

        solved, solution = root.find_solution(grid)

        assert_that(solution._get_puzzle_state(), is_(puzzle))

    def test_find_solution_solves_incomplete_puzzle_with_single_number_missing(self):
        puzzle = "19854372664327859152761984391473526887619243523548617946235198738192765475986431."
        base_domain = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        grid = SudokuGrid(puzzle, base_domain)
        root = TreeNode()

        solved, solution = root.find_solution(grid)

        assert_that(solved, is_(True))

    def test_find_solution_returns_false_when_constraints_broken(self):
        with patch('sudoku_grid.SudokuGrid') as mock:
            grid = mock
            grid.constraints_broken.return_value = True
            grid.cull.return_value = False
            root = TreeNode()
            solved, solution = root.find_solution(grid)
            assert_that(solved, is_(False))

    def test_find_solution_solves_incomplete_puzzle_with_multiple_numbers_missing(self):
        puzzle = "198543726643278591527619843914735268876192435235486179462351987381927654759864..."
        base_domain = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        grid = SudokuGrid(puzzle, base_domain)
        root = TreeNode()

        solved, solution = root.find_solution(grid)

        assert_that(solved, is_(True))
