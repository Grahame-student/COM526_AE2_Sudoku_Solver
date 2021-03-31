# COM526_AE2_Sudoku_Solver

# Installation
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

Worked example:
```3000001,.......12....35......6...7.7.....3.....4..8..1...........12.....8.....4..5....6..,673894512912735486845612973798261354526473891134589267469128735287356149351947628```

# Running the Solver
Run the ```run_solver.bat``` script to get the solver to attempt all of the puzzles in ```data/puzzles.csv```
