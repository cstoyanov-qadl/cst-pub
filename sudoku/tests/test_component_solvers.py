"""This module regroups tests on the following component: solvers.py

"""
from itertools import chain

import pytest

import solvers
from dataset import ALL_SUDOKUS, ALL_SUDOKUS_SOLVED
from formulas import generate_initial_formula


LEVEL_SOLVERS = [
    # ("name of the solver", "level of the grid", "is solvable")
    ("unitary-propagation", "easy", True),
    ("unitary-propagation", "medium", True),
    ("unitary-propagation", "hard", True),
    ("unitary-propagation", "expert", False),
    ("unitary-propagation", "master", False),
    ("unfructuous-litteral", "easy", True),
    ("unfructuous-litteral", "medium", True),
    ("unfructuous-litteral", "hard", True),
    ("unfructuous-litteral", "expert", True),
    ("unfructuous-litteral", "master", True)]


@pytest.fixture(params=LEVEL_SOLVERS)
def level_solver(request):
    return request.param


class TestSolvers:
    """Test the different type of solvers with different level of difficulty

    """

    def test_solver(self, level_solver):
        """Check that the for a given solver, it is possible to solve
        a given level of difficulty (or not, if not solvable)

        """
        solver_name = level_solver[0]
        solver_level =  level_solver[1]
        is_solvable = level_solver[2]

        if solver_name == "unitary-propagation":
            used_solver = solvers.propagate
        elif solver_name == "unfructuous-litteral":
            used_solver = solvers.propagate2
        else:
            raise AssertionError("Unknown solver used")

        grid = ALL_SUDOKUS[solver_level]
        solved_grid = ALL_SUDOKUS_SOLVED[solver_level]
        initial_formula = generate_initial_formula(grid)

        if is_solvable:
            used_solver(grid, initial_formula)
            assert grid == solved_grid
        else:
            used_solver(grid, initial_formula)
            assert 0 in list(set(chain(*grid)))
