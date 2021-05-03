from timeit import default_timer as timer

from sudoku_grid import SudokuGrid
from tree_node import TreeNode


# Cull only - solve rate: (31k solved / 3m puzzles) ~1%
def main():
    """

    """

    puzzle_list = get_data("data/demo.csv")

    solved_count = 0
    puzzle_count = 0
    puzzle_total = len(puzzle_list)
    for puzzle in puzzle_list:
        puzzle_count += 1
        all_values = puzzle.rstrip().split(",")
        grid = SudokuGrid(all_values[1])

        TreeNode.count = 0
        root_node = TreeNode()
        start = timer()
        solved, solution = root_node.find_solution(grid)
        elapsed = timer() - start

        if solved:
            solved_count += 1
            result_string = f"{all_values[0]},Solved,{solution.count},{elapsed}"
        else:
            result_string = f"{all_values[0]},Unsolved,{solution.count},{elapsed}"

        print(result_string)
        with open("results.csv", 'a') as results_file:
            print(result_string, file=results_file)

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
