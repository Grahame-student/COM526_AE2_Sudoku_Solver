from sudoku_grid import SudokuGrid


# Cull only - solve rate: (31k solved / 3m puzzles) ~1%
def main():
    puzzle_list = get_data("data/puzzles.csv")

    solved = 0
    base_domain = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    puzzle_count = 0
    puzzle_total = len(puzzle_list)
    for puzzle in puzzle_list:
        puzzle_count += 1
        all_values = puzzle.rstrip().split(",")
        grid = SudokuGrid(all_values[1], base_domain)

        while grid.cull():
            pass
        if grid.result() == "Solved":
            solved += 1
        if puzzle_count % 1000 == 0:
            print(
                f"{puzzle_count} / {puzzle_total} - "
                f"solved {solved} / {puzzle_total} - solve rate "
                f"{((solved / puzzle_count) * 100):.2f}%"
            )


def get_data(path):
    with open(path, "r") as data_file:
        return data_file.readlines()


# Ensure that main() is called when this file is executed from the commandline
if __name__ == "__main__":
    main()
