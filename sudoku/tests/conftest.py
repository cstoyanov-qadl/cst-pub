"""Conftest PYTEST configuration files

We use this file to:
    - define some global pytest behaviour
    - define wide-scope fixture

"""

import pytest


SUDOKU_CLI_USAGE = """usage: Suduko Solver [-h] -g GRIDS [-l] [-s SOLVER_NAME]

Solve sudoku grid(s)

options:
  -h, --help            show this help message and exit
  -g GRIDS, --grids GRIDS
                        Path to the description files of the suduko
  -l, --solver-list     List the available solvers
  -s SOLVER_NAME, --solver-name SOLVER_NAME
                        Select the solver to use"""


SUDOKU_CLI_MISSING_ARGS = """usage: Suduko Solver [-h] -g GRIDS [-l] [-s SOLVER_NAME]
Suduko Solver: error: the following arguments are required: -g/--grids"""

SUDOKU_CLI_EXP_ARGS = """usage: Suduko Solver [-h] -g GRIDS [-l] [-s SOLVER_NAME]
Suduko Solver: error: argument -g/--grids: expected one argument"""

SUDOKU_CLI_MANDAT_ARGS = """usage: Suduko Solver [-h] -g GRIDS [-l] [-s SOLVER_NAME]
Suduko Solver: error: the following arguments are required: -g/--grids"""

EASY_002_SOLVED = """===================
|0 0 5 0 0 3 0 9 4|
|7 3 0 0 0 0 6 0 0|
|0 9 2 4 1 5 0 8 3|
|0 5 0 6 0 2 0 4 0|
|0 6 0 0 3 0 0 7 2|
|0 8 0 5 0 9 0 0 0|
|9 0 6 1 5 0 3 0 0|
|1 0 8 0 9 0 4 0 0|
|5 0 0 2 0 4 0 6 0|
===================
===================
|8 1 5 7 6 3 2 9 4|
|7 3 4 9 2 8 6 1 5|
|6 9 2 4 1 5 7 8 3|
|3 5 1 6 7 2 8 4 9|
|4 6 9 8 3 1 5 7 2|
|2 8 7 5 4 9 1 3 6|
|9 4 6 1 5 7 3 2 8|
|1 2 8 3 9 6 4 5 7|
|5 7 3 2 8 4 9 6 1|
==================="""

EASY_001_UNSOLVED = """===================
|0 9 0 2 0 0 6 0 5|
|3 2 0 0 0 7 0 0 0|
|0 7 0 9 0 5 0 0 8|
|0 1 0 0 0 0 0 0 0|
|0 0 7 0 0 0 0 9 4|
|6 0 0 0 0 0 0 0 0|
|0 0 8 0 0 0 0 0 7|
|0 3 0 4 9 1 5 0 0|
|0 0 0 0 0 3 0 0 0|
===================
===================
|8 9 1 2 3 4 6 7 5|
|3 2 5 0 0 7 0 0 0|
|4 7 6 9 1 5 0 0 8|
|0 1 0 0 0 0 0 6 0|
|0 0 7 0 0 0 0 9 4|
|6 0 0 0 0 0 0 5 0|
|0 0 8 0 0 0 0 0 7|
|7 3 2 4 9 1 5 8 6|
|0 0 0 0 0 3 0 0 0|
==================="""

MEDIUM_001_SOLVED = """===================
|0 0 9 0 0 0 0 0 0|
|0 6 0 0 0 0 5 0 0|
|0 0 0 2 9 1 0 0 4|
|2 5 0 1 0 9 6 8 0|
|6 0 0 3 0 4 0 1 0|
|0 0 3 5 0 0 0 0 7|
|0 9 0 0 3 0 0 5 6|
|0 0 6 0 0 0 0 4 9|
|3 0 0 0 0 2 0 0 1|
===================
===================
|4 7 9 6 5 8 1 3 2|
|1 6 2 7 4 3 5 9 8|
|5 3 8 2 9 1 7 6 4|
|2 5 4 1 7 9 6 8 3|
|6 8 7 3 2 4 9 1 5|
|9 1 3 5 8 6 4 2 7|
|8 9 1 4 3 7 2 5 6|
|7 2 6 8 1 5 3 4 9|
|3 4 5 9 6 2 8 7 1|
==================="""

MASTER_001_SOLVED = """===================
|6 0 0 0 0 0 0 0 4|
|0 0 9 0 8 0 2 0 1|
|0 3 0 0 0 9 0 0 0|
|0 5 0 1 0 0 6 0 2|
|0 0 0 0 6 0 0 3 0|
|0 0 2 0 0 0 0 4 0|
|0 0 0 0 0 0 0 6 0|
|7 0 0 5 0 0 0 0 0|
|0 0 3 0 1 0 8 0 9|
===================
===================
|6 2 8 7 5 1 3 9 4|
|4 7 9 3 8 6 2 5 1|
|1 3 5 4 2 9 7 8 6|
|9 5 4 1 3 8 6 7 2|
|8 1 7 2 6 4 9 3 5|
|3 6 2 9 7 5 1 4 8|
|2 9 1 8 4 3 5 6 7|
|7 8 6 5 9 2 4 1 3|
|5 4 3 6 1 7 8 2 9|
==================="""

def simple_testcase_displayer(param):
    return param.get("testname")
