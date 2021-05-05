from sudoku_grid import SudokuGrid


class TreeNode:
    count = 0

    def __init__(self):
        self.grid = None
        self.cells = None

    def find_solution(self, grid):
        TreeNode.count += 1
        if TreeNode.count % 10000 == 0:
            print(TreeNode.count)

        self.grid = SudokuGrid(grid.get_puzzle_state())
        self._apply_constraints()

        result = (self.grid.result() == "Solved")
        if result:
            # Solved, succeed fast
            return result, self.grid
        elif self.grid.constraints_broken():
            # Constraints broken
            pass
        else:
            # Unsolved, search for a valid solution
            result = self._depth_first_search()

        return result, self.grid

    def _apply_constraints(self):
        while self.grid.cull():
            pass

    def _depth_first_search(self):
        sorted_list = self._get_sorted_options()
        while sorted_list:
            cell = sorted_list.pop()[1]
            for option in cell["domains"]:
                node = TreeNode()
                self.grid.set_cell_value(cell["id"], option)
                result, solution = node.find_solution(self.grid)
                if result:
                    self.grid = solution
                    return True
        return False

    def _get_sorted_options(self):
        self.cells = self.grid.get_unsolved_cells()
        sorted_options = []
        for key, cell in self.cells.items():
            sorted_options.append((len(cell["domains"]), cell))

        sorted_options.sort(key=lambda tup: tup[0], reverse=True)
        return sorted_options
