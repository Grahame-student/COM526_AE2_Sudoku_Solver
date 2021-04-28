from sudoku_grid import SudokuGrid


class TreeNode:
    count = 0

    def __init__(self):
        self.children = []
        self.grid = None
        self.cells = None

    def find_solution(self, grid):
        TreeNode.count += 1
        self.grid = SudokuGrid(grid._get_puzzle_state())
        self.apply_constraints()
        result = (self.grid.result() == "Solved")

        if not self.grid.constraints_broken():
            self.cells = grid.get_unsolved_cells()
            sorted_list = self._get_sorted_options()

            while sorted_list:
                cell = sorted_list.pop()[1]
                for option in cell["domains"]:
                    self.children.append(TreeNode())
                    self.grid.set_cell_value(cell["id"], option)
                    result, solution = self.children[-1].find_solution(self.grid)
                    if solution.constraints_broken():
                        self.children.pop(-1)

                    if result:
                        self.grid = solution
                        self.grid.setCount(TreeNode.count)
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

    def _add_child(self, child_node):
        self.children.append(child_node)
