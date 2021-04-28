from sudoku_grid import SudokuGrid
from tree_node import TreeNode
from save_to_file import saveToFile

# Cull only - solve rate: (31k solved / 3m puzzles) ~1%
def main():
    """

    """

    puzzle_list = get_data("data/puzzles.csv")

    solved_count = 0
    puzzle_count = 0
    puzzle_total = len(puzzle_list)
    for puzzle in puzzle_list:
        puzzle_count += 1
        all_values = puzzle.rstrip().split(",")
        grid = SudokuGrid(all_values[1])

        TreeNode.count = 0
        root_node = TreeNode()
        solved, solution = root_node.find_solution(grid)

        if solved:
            solved_count += 1
            print(f"Solution - {solution.count} iterations")
            saveToFile.save(solution, solution.count)

        else:
            print(f"Failed to solve after {solution.count} iterations")

        print(solution)

        if puzzle_count % 1000 == 0:
            print(
                f"{puzzle_count} / {puzzle_total} - "
                f"solved {solved_count} / {puzzle_total} - solve rate "
                f"{((solved_count / puzzle_count) * 100):.2f}%"
            )


def get_data(path):
    """
    Read in the entire set of puzzles from the specified path
    :param path: absolute
    :return:
    """
    with open(path, "r") as data_file:
        return data_file.readlines()


# Ensure that main() is called when this file is executed from the commandline
if __name__ == "__main__":
    main()
