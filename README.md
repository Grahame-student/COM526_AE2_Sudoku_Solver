# COM526_AE2_Sudoku_Solver
![Lint Project](https://github.com/Grahame-student/COM526_AE2_Sudoku_Solver/workflows/Lint%20Project/badge.svg)

## Installation
Run the ```prepare_venv.bat``` script to create a python virtual environment and install the necessary libraries for the Sudoku solver.

Add a ```puzzles.csv``` file to the ```data``` directory where each line has the following structure:

```<Puzzle Number>,<Unsolved Puzzle>,<Solved Puzzle>```

* ```<Puzzle Number>```
  * integer, used to identify specific puzzles
* ```<Unsolved Puzzle>```
  * 81 digits, each representing a cell of the puzzle.
  * ```0``` or ```.``` indicates an empty cell
  * ```[1-9]``` indicate a cell with known value
* ```<Solved Puzzle>```
  * 81 digits, each representing a cell of the puzzle.
  * ```[1-9]``` indicate a cell with known value

NOTE: Any additional columns will be ignored

Worked example:
```3000001,.......12....35......6...7.7.....3.....4..8..1...........12.....8.....4..5....6..,673894512912735486845612973798261354526473891134589267469128735287356149351947628```

## Running the Solver
Run the ```run_solver.bat``` script to get the solver to attempt all of the puzzles in ```data/puzzles.csv```

## Getting Additional Puzzles
There are a number of large puzzle sets on Kaggle
* [1,000,000 puzzles](https://www.kaggle.com/bryanpark/sudoku)
* [3,000,000 puzzles](https://www.kaggle.com/radcliffe/3-million-sudoku-puzzles-with-ratings)
* [9,000,000 puzzles](https://www.kaggle.com/rohanrao/sudoku)
