from copy import deepcopy


class TreeNode:
    def __init__(self):
        self.children = []
        self.grid = None
        self.cells = None

    def find_solution(self, grid):
        result = False
        self.grid = grid
        self.apply_constraints()

        if self.grid.result() == "Solved":
            result = True

        if not self.grid.constraints_broken():
            self.cells = grid.get_unsolved_cells()
            sorted_list = []
            for key, cell in self.cells.items():
                sorted_list.append((len(cell["domains"]), cell))

            sorted_list.sort(key=lambda tup: tup[0], reverse=True)

            while sorted_list:
                cell = sorted_list.pop()[1]
                # print(f'Option Count: {len(cell["domains"])}')
                for option in cell["domains"]:
                    self.children.append(TreeNode())
                    new_grid = deepcopy(self.grid)
                    new_grid.set_cell_value(cell["id"], option)
                    result, solution = self.children[-1].find_solution(new_grid)
                    # print(f'key:{cell["id"]} - option:{option} - state:{new_grid._get_puzzle_state()}')
                    if result:
                        self.grid = solution
                        break
                if result:
                    break

        return result, self.grid

    def apply_constraints(self):
        while self.grid.cull():
            pass

    def _add_child(self, child_node):
        self.children.append(child_node)
