#!/usr/bin/env python3
"""Entry point of the sudoku solver:

- User interface management
- Validation of entry data
- Execution of the selected solver

"""
import argparse
import logging
import sys

from pathlib import Path

from solvers import Solver


GRID_SIZE = 9

RC_OK = 0
RC_INVALID_GRID_VALUE = 10
RC_INVALID_GRID_SIZE = 11

LOGGER = logging.getLogger()


def sudoku_parser():
    """Manage the argument of the command"""
    parser = argparse.ArgumentParser(
        prog="Suduko Solver", description="Solve sudoku grid(s)"
    )
    parser.add_argument(
        "-g", "--grids",
        type=str, required=True,
        help="Path to the description files of the suduko",
    )
    parser.add_argument(
        "-l", "--solver-list",
        action="store_true",
        help="List the available solvers",
    )
    parser.add_argument(
        "-s", "--solver-name",
        type=str, required=False, default="unitary-propagation",
        help="Select the solver to use",
    )

    return parser


def process_parser(parser):
    """Process and validate the arguments provided by the user"""
    args = parser.parse_args()

    if args.solver_list:
        return args

    args.grids = [Path(filepath) for filepath in args.grids.split(",")]

    LOGGER.debug("CLI arguments: %s", args)
    return args


def load_grid(filepath):
    """Load the grid from a file"""
    data = None
    if filepath.exists():
        with filepath.open() as fd_read:
            data = [[int(elt) for elt in line.strip().split(" ")] for line in fd_read.readlines()]
    return data


def validate_grid(grid):
    """Check the the grid is valid

    - good square size

    """
    if 0 <= len(grid) <= GRID_SIZE - 1:
        raise ValueError("The grid should be of size 9 x 9")
    for i in range(GRID_SIZE):
        for j in range(GRID_SIZE):
            if not 0 <= grid[i][j] <= 9 or not 0 <= grid[i][j] <= 9:
                raise ValueError(
                    "The value of ({},{}) is not in the value range ({})".format(
                        i, j, grid[i][j]))


def print_grid(grid):
    """Dump the grid"""
    print("=" * (2 * GRID_SIZE + 1))
    for line in grid:
        inner_line = " ".join(str(elt) for elt in line)
        print("|" + inner_line + "|")
    print("=" * (2 * GRID_SIZE + 1))


if __name__ == "__main__":
    args = process_parser(sudoku_parser())

    if args.solver_list:
        LOGGER.info("The following solvers are available:")
        for element in Solver.available_solvers():
            print("\t- %s" % element)
        sys.exit(RC_OK)

    RETURN_CODE = 0
    grids = []
    for str_grid in args.grids:
        LOGGER.info("solve the grid: '%s'", str_grid)

        try:
            grid = load_grid(str_grid)
        except ValueError as err:
            print("The grid '%s' is not valid: %s", str_grid, str(err))
            sys.exit(RC_INVALID_GRID_VALUE)

        try:
            validate_grid(grid)
        except ValueError as err:
            print("The grid '%s' is not valid: %s", str_grid, str(err))
            sys.exit(RC_INVALID_GRID_SIZE)

        grids.append(grid)
        print_grid(grid)

        solver = Solver(args.solver_name)
        solver.solve(grid)
        print_grid(grid)

    sys.exit(RETURN_CODE)
