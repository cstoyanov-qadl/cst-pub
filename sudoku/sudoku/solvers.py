"""This module regroups the methods used to solve a sudoku

"""
import copy

from itertools import chain

from .formulas import generate_initial_formula
from .objects import Clause
from .objects import Formule
from .objects import Litteral


class EmptyClause(BaseException):
    """Raise an exception if an empty clause is found (cannot be satisfied)"""

    pass  # pylint: disable=unnecessary-pass


def new_isolated_litteral(  # pylint: disable=inconsistent-return-statements
    formule: Formule,
) -> Litteral:
    """Return a clause which contains one litteral from a formule"""
    for clause in formule.clauses:
        if len(clause) == 1:
            return clause.litts[-1]


def simplify_formula(formule: Formule, isolated_litteral: Litteral) -> None:
    """Simplify a formula following the following rules:

    - if the isolated litteral is included in a clause, remove the clause
    - if the opposite of the isolated litteral is included in a clase, remove
        it from the clauses
    """
    if formule.clauses == []:
        return

    n_isolated_litteral = ~isolated_litteral

    nb_clauses = len(formule.clauses)
    for i in range(nb_clauses):
        # Delete clauses than contain the litteral
        clause = formule.clauses[nb_clauses - 1 - i]
        if isolated_litteral in clause.litts:
            formule.clauses.pop(nb_clauses - 1 - i)
        elif n_isolated_litteral in clause.litts:
            clause.litts.pop(clause.litts.index(n_isolated_litteral))
            if clause.litts == []:
                raise EmptyClause("Empty clause detected")


def propagate(grid: list[list[int]], formule: Formule) -> None:
    """Until there is no more isolated litteral, simplify the formula"""
    while new_litteral := new_isolated_litteral(formule):
        if new_litteral.sign is True:
            grid[new_litteral.i][new_litteral.j] = new_litteral.k
        simplify_formula(formule, new_litteral)


############
# SOLVER 2 #
############


def variables(formule: Formule) -> list[Litteral]:
    """Generate flatten list from the list"""
    obj = formule.clauses
    return list(set(chain(*obj)))


def deduce(grid: list[list[int]], litteral: Litteral, formule: Formule) -> int:
    """Define if the litteral can be added of not to the formule"""
    rt_code = 0

    tmp_grid = copy.deepcopy(grid)
    tmp_form = copy.deepcopy(formule)
    tmp_form = tmp_form + Formule([Clause([litteral])])
    try:
        propagate(tmp_grid, tmp_form)
    except EmptyClause:
        rt_code -= 1

    tmp_grid = copy.deepcopy(grid)
    tmp_form = copy.deepcopy(formule)
    tmp_form = tmp_form + Formule([Clause([~litteral])])
    try:
        propagate(tmp_grid, tmp_form)
    except EmptyClause:
        rt_code += 1

    return rt_code


def propagate2(grid: list[list[int]], formule: Formule) -> None:
    """Solve the grid using the infructuous litteral algorithm"""
    propagate(grid, formule)

    if not formule:
        return

    un_vars = variables(formule)
    for litteral in un_vars:
        is_infr_litteral = deduce(grid, litteral, formule)
        if is_infr_litteral == 0:
            pass
        elif is_infr_litteral == 1:
            formule = formule + Formule([Clause([litteral])])
            propagate(grid, formule)
        elif is_infr_litteral == -1:
            formule = formule + Formule([Clause([~litteral])])
            propagate(grid, formule)
        else:
            raise ValueError("unexpected case")


class Solver:
    """Factory-fabric pattern object"""

    def __init__(self, solver_name: str = "unitary-propagation"):
        if solver_name == "unitary-propagation":
            self.solver_fn = propagate
        elif solver_name == "unfructuous-litteral":
            self.solver_fn = propagate2
        else:
            raise ValueError(f"this solver does not exist: {solver_name}")

    @staticmethod
    def available_solvers():
        """list the available solvers"""
        return ["unitary-propagation", "unfructuous-litteral"]

    def solve(self, grid: list[list[int]]) -> None:
        """Solve the sudoku using the expected propagation strategy"""
        formula = generate_initial_formula(grid)
        return self.solver_fn(grid, formula)
