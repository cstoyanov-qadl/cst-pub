"""This module regroups the methods used to solve a sudoku

"""
import copy

from itertools import chain
from typing import List

from formulas import generate_initial_formula
from objects import Clause
from objects import Formule
from objects import Litteral


class EmptyClause(BaseException):
    """Raise an exception if an empty clause is found (cannot be satisfied)

    """
    pass


def new_isolated_litteral(formule: Formule) -> Litteral:
    """Return a clause which contains one litteral from a formule

    """
    # FIXME: Yield it!!!
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
        return formule

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


def propagate(grid: List[List[int]], formule: Formule, dry: bool = False) -> None:
    """Until there is no more isolated litteral, simplify the formula

    """
    while new_litteral := new_isolated_litteral(formule):
        if new_litteral.sign is True:
            if not dry:
                pass
                # print("[%s][%s] set to %s" % (
                #     new_litteral.i, new_litteral.j, new_litteral.k))
            grid[new_litteral.i][new_litteral.j] = new_litteral.k
        simplify_formula(formule, new_litteral)


############
# SOLVER 2 #
############

def variables(formule: Formule) -> List[Litteral]:
    """Generate flatten list from the list"""
    obj = formule.clauses
    return list(set(chain(*obj)))


def deduce(grid: List[List[int]], litteral: Litteral, formule: Formule) -> int:
    """Define if the litteral can be added of not to the formule"""
    rt_code = 0

    tmp_grid = copy.deepcopy(grid)
    tmp_form = copy.deepcopy(formule)
    tmp_form = tmp_form + Formule([Clause([litteral])])
    try:
        propagate(tmp_grid, tmp_form, dry=True)
    except EmptyClause:
        rt_code -= 1

    tmp_grid = copy.deepcopy(grid)
    tmp_form = copy.deepcopy(formule)
    tmp_form = tmp_form + Formule([Clause([~litteral])])
    try:
        propagate(tmp_grid, tmp_form, dry=True)
    except EmptyClause:
        rt_code += 1

    return rt_code


def propagate2(grid: List[List[int]], formule: Formule) -> None:
    """Solve the grid using the infructuous litteral algorithm

    """
    propagate(grid, formule)

    if not formule:
        return

    while len(formule):

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

        break


class Solver:
    """Factory-fabric pattern object"""

    def __init__(self, solver_name: str = "unitary-propagation"):
        if solver_name == "unitary-propagation":
            self.solver_fn = propagate
        elif solver_name == "unfructuous-litteral":
            self.solver_fn = propagate2
        else:
            raise ValueError("this solver does not exist: %s" % solver_name)

    @staticmethod
    def available_solvers():
        return ["unitary-propagation", "unfructuous-litteral"]

    def solve(self, grid: List[List[int]]) -> None:
        formula = generate_initial_formula(grid)
        return self.solver_fn(grid, formula)
