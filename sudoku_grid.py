class SudokuGrid:
    def __init__(self, puzzle, domain):
        self.start = puzzle
        self.grid = SudokuGrid._get_grid(puzzle, domain)
        self.grid = SudokuGrid._set_peers(self.grid)

    def __str__(self):
        result = ""
        for chunk in SudokuGrid._split_into_x_chunks(self._get_puzzle_state()):
            result += f"{chunk}\n"
        return result

    @staticmethod
    def _split_into_x_chunks(
        string, chunk_size=9
    ):  # we assume here that x is an int and > 0
        size = len(string)
        for pos in range(0, size, chunk_size):
            yield string[pos : pos + chunk_size]

    @staticmethod
    def _get_grid(puzzle, domain):
        """
        Create the game grid from the puzzle string and domain
        - Cells that are zero are empty and will be set to a list of all the domain
          values
        - Cells that are non-zero are solved and are therefore set to a list containing
          just that value
        No culling is carried out at this stage
        :param puzzle: String representation of the puzzle starting state
        :param domain: List of all the possible values that each cell can be set to
        :return: A list of lists, where each sub-list represents the values that a cell
                 could be set to
        """
        grid = {}
        cell_id = 0
        puzzle = puzzle.replace(".", "0")
        for value in puzzle:
            grid[cell_id] = {
                "id": cell_id,
                "peers": set(),
                "domains": domain[:] if value == "0" else [int(value)],
            }
            cell_id += 1
        return grid

    @staticmethod
    def _set_peers(cells):
        for key, cell in cells.items():
            cells[key] = SudokuGrid._set_row_peers(cell)
            cells[key] = SudokuGrid._set_col_peers(cell)
            cells[key] = SudokuGrid._set_box_peers(cell)
            if (len(cell["peers"])) != 20:
                print(f'id: {cell["id"]} - {cell["peers"]}')
        return cells

    @staticmethod
    def _set_row_peers(cell):
        row = SudokuGrid._get_row(cell["id"])
        for col in range(9):
            cell_id = (row * 9) + col
            if cell_id != cell["id"]:
                cell["peers"].add(cell_id)
        return cell

    @staticmethod
    def _get_row(cell_no):
        return cell_no // 9

    @staticmethod
    def _set_col_peers(cell):
        col = SudokuGrid._get_col(cell["id"])
        for row in range(9):
            cell_id = (row * 9) + col
            if cell_id != cell["id"]:
                cell["peers"].add(cell_id)
        return cell

    @staticmethod
    def _get_col(cell_no):
        return cell_no % 9

    @staticmethod
    def _set_box_peers(cell):
        box_row = SudokuGrid._get_row(cell["id"]) // 3
        box_col = SudokuGrid._get_col(cell["id"]) // 3

        for row in range((box_row * 3), (box_row * 3) + 3):
            for col in range((box_col * 3), (box_col * 3) + 3):
                cell_id = (row * 9) + col
                if cell_id != cell["id"]:
                    cell["peers"].add(cell_id)
        return cell

    def cull(self):
        """
        For each solved cell remove the known value from that cell's peer's domain
        :return: True if any culling has occurred, False otherwise
        """
        changed = False
        for key, cell in self.grid.items():
            changed |= self._cull_peers(cell)
        return changed

    def _cull_peers(self, cell):
        changed = False
        if len(cell["domains"]) == 1:
            for peer in cell["peers"]:
                if cell["domains"][0] in self.grid[peer]["domains"]:
                    self.grid[peer]["domains"].remove(cell["domains"][0])
                    changed = True
        return changed

    def display_state(self):
        for row in range(9):
            row_string = ""
            for col in range(9):
                cell_id = (row * 9) + col
                row_string += str(self.grid[cell_id]["domains"])
            print(f"{row_string}")

    def result(self):
        for key, cell in self.grid.items():
            if len(cell["domains"]) > 1:
                return "Unsolved"
        return "Solved"

    def constraints_broken(self):
        """
        Check to see if the constraints of the problem have been broken
        :return: True if no further options remain in the domain, False otherwise
        """
        for key, cell in self.grid.items():
            if len(cell["domains"]) == 0:
                return True
        return False

    def _get_puzzle_state(self):
        """
        Create a string representing the current state of the puzzle. Each character shows the state of a single cell
        A number from 1-9 shows a solved cell and a '.' character shows an unsolved cell
        :return: 
        """
        solution = ""
        for key, cell in self.grid.items():
            if len(cell["domains"]) == 1:
                solution += str(cell["domains"][0])
            else:
                solution += "."
        return solution
