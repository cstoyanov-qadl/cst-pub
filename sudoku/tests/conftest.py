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


def simple_testcase_displayer(param):
    return param.get("testname")
