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
        self.apply_constraints()

        result = (self.grid.result() == "Solved")

        if not self.grid.constraints_broken():
            self.cells = self.grid.get_unsolved_cells()

            sorted_list = self._get_sorted_options()

            while sorted_list:
                cell = sorted_list.pop()[1]
                for option in cell["domains"]:
                    node = TreeNode()
                    self.grid.set_cell_value(cell["id"], option)
                    result, solution = node.find_solution(self.grid)
                    if result:
                        self.grid = solution
                        self.grid.set_count(TreeNode.count)
                        break
                if result:
                    break

        return result, self.grid

    def apply_constraints(self):
        while self.grid.cull():
            pass

    def _get_sorted_options(self):
        sorted_options = []
        for key, cell in self.cells.items():
            sorted_options.append((len(cell["domains"]), cell))

        sorted_options.sort(key=lambda tup: tup[0], reverse=True)
        return sorted_options
