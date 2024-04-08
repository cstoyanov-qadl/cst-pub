"""This module regroups methods to generate the formules

There are two main formulas:
    - Formulas from the rules of the game
    - Formulas from the grid to solve

"""
import logging
import sys

from objects import Clause
from objects import Formule
from objects import Litteral
from operations import index

sys.setrecursionlimit(15000)

GRID_SIZE = 9
LOGGER = logging.getLogger(__name__)


def block1() -> Formule:
    """Returns the formula corresponding to the rule B1

    B1: tout bloc de F contient au moins une fois chacun des chiffres 1 à 9

    """
    formule = []
    for block_id in range(GRID_SIZE):
        for value in range(1, GRID_SIZE + 1):
            clause = []
            for cell_id in range(GRID_SIZE):
                line_id, col_id = index(block_id, cell_id)
                clause.append(Litteral(True, line_id, col_id, value))
            formule.append(Clause(clause))
    return Formule(formule)


def block2() -> Formule:
    """Returns the formula corresponding to the rule B2

    B2:  tout bloc de F contient au plus une fois chacun des chiffres 1 à 9

    """
    formule = []
    for block_id in range(GRID_SIZE):
        for value in range(1, GRID_SIZE + 1):
            for cell_id_1 in range(GRID_SIZE):
                for cell_id_2 in range(GRID_SIZE):
                    if cell_id_1 <= cell_id_2:
                        continue
                    line_id_1, col_id_1 = index(block_id, cell_id_1)
                    line_id_2, col_id_2 = index(block_id, cell_id_2)
                    lit1 = Litteral(False, line_id_1, col_id_1, value)
                    lit2 = Litteral(False, line_id_2, col_id_2, value)
                    formule.append(Clause([lit1, lit2]))
    return Formule(formule)


def cell1() -> Formule:
    """Returns the formula corresponding to the rule K1

    K1: Toute case de F contient au moins une fois l'un des chiffres 1 à 9

    """
    formule = []
    for line_id in range(GRID_SIZE):
        for col_id in range(GRID_SIZE):
            clauses = Clause(
                [Litteral(True, line_id, col_id, value) for value in range(1, GRID_SIZE + 1)]
            )
            formule.append(clauses)
    return Formule(formule)


def cell2() -> Formule:
    """Returns the formula corresponding to the rule K2

    K2:  toute case de F contient au plus une fois l’un des chiffres 1 à 9

    """
    formule = []
    for line_id in range(GRID_SIZE):
        for col_id in range(GRID_SIZE):
            for val1 in range(1, GRID_SIZE + 1):
                for val2 in range(1, GRID_SIZE + 1):
                    if val1 <= val2:
                        continue
                    lit1 = Litteral(False, line_id, col_id, val1)
                    lit2 = Litteral(False, line_id, col_id, val2)
                    formule.append(Clause([lit1, lit2]))
    return Formule(formule)


def col1() -> Formule:
    """Returns the formula corresponding to the rule C1

    C1: toute colonne de 𝐹 contient au moins une fois chacun des chiffres 1 à 9

    """
    formule = []
    for col_id in range(GRID_SIZE):
        for value in range(1, GRID_SIZE + 1):
            clause = []
            for line_id in range(GRID_SIZE):
                clause.append(Litteral(True, line_id, col_id, value))
            formule.append(Clause(clause))
    return Formule(formule)


def col2() -> Formule:
    """Returns the formula corresponding to the rule C2

    C2: toute colonne de 𝐹 contient au plus une fois chacun des chiffres 1 à 9

    """
    formule = []
    for col_id in range(GRID_SIZE):
        for value in range(1, GRID_SIZE + 1):
            for line_id_1 in range(GRID_SIZE):
                for line_id_2 in range(GRID_SIZE):
                    if line_id_1 <= line_id_2:
                        continue
                    lit1 = Litteral(False, line_id_1, col_id, value)
                    lit2 = Litteral(False, line_id_2, col_id, value)
                    formule.append(Clause([lit1, lit2]))
    return Formule(formule)


def line1() -> Formule:
    """Returns the formula corresponding to the rule L1

    L1: toute ligne de F contient au moins une fois chacun des chiffres 1 à 9

    """
    formule = []
    for line_id in range(GRID_SIZE):
        for value in range(1, GRID_SIZE + 1):
            clause = [Litteral(True, line_id, col_id, value) for col_id in range(GRID_SIZE)]
            formule.append(Clause(clause))
    return Formule(formule)


def line2() -> Formule:
    """Returns the formula corresponding to the rule L2

    L2: toute ligne de F contient au plus une fois chacun des chiffres 1 à 9

    """
    formule = []
    for line_id in range(GRID_SIZE):
        for value in range(1, GRID_SIZE + 1):
            for col_id_1 in range(GRID_SIZE):
                for col_id_2 in range(GRID_SIZE):
                    if col_id_1 <= col_id_2:
                        continue
                    lit1 = Litteral(False, line_id, col_id_1, value)
                    lit2 = Litteral(False, line_id, col_id_2, value)
                    formule.append(Clause([lit1, lit2]))
    return Formule(formule)


def generate_rule_formule() -> Formule:
    """Return the full formula defined by the rules of the Suduko"""
    # Generate the formule from the rule of the game
    rules_functions = {
        "K1": cell1,
        "K2": cell2,
        "L1": line1,
        "L2": line2,
        "B1": block1,
        "B2": block2,
        "C1": col1,
        "C2": col2,
    }

    formule = Formule([])
    for rulefunc in rules_functions.values():
        formule += rulefunc()

    return formule


def generate_data_formula(grid: list[list[int]]) -> Formule:
    """Generate the formula from the datas contained in the grid to solve

    Args:
        grid (list of list): modelized suduko grid

    Returns:
        Formula corresponding to the grid to solve

    """
    formule = []
    for line_id in range(GRID_SIZE):
        for col_id in range(GRID_SIZE):
            if grid[line_id][col_id] == 0:
                continue
            value = grid[line_id][col_id]
            clauses = [Clause([Litteral(True, line_id, col_id, value)])] + [
                Clause([Litteral(False, line_id, col_id, val)])
                for val in range(1, GRID_SIZE + 1)
                if val != value
            ]
            formule = formule + clauses
    return Formule(formule)


def forbidden_ij(grid: list[list[int]], line_id: int, col_id: int) -> Formule:
    """Return the formula of the forbidden values for a given cell

    Args:
        grid (list of list): modelized suduko grid
        line_id (int): index of the cell line
        col_id (int): index of the cell column

    Returns:
        Formula corresponding to the forbidden values of the cell

    """
    # Compute the block position for the block clauses
    block_id = 3 * int(line_id / 3) + int(col_id / 3)

    formule = []
    # Block forbidden litterals
    for cell_id in range(GRID_SIZE):
        i, j = index(block_id, cell_id)
        # if a value in the cell is not empty, its value cannot be used
        # in the other cells of the block
        if grid[i][j] != 0:
            lit = Litteral(False, line_id, col_id, grid[i][j])
            if Clause([lit]) not in formule:
                formule += [Clause([lit])]
    # Col forbidden litterals
    for i in range(GRID_SIZE):
        if grid[i][col_id] != 0:
            lit = Litteral(False, line_id, col_id, grid[i][col_id])
            if Clause([lit]) not in formule:
                formule += [Clause([lit])]
    # Line forbidden litterals
    for j in range(GRID_SIZE):
        if grid[line_id][j] != 0:
            lit = Litteral(False, line_id, col_id, grid[line_id][j])
            if Clause([lit]) not in formule:
                formule += [Clause([lit])]

    return Formule(formule)


def generate_forbidden_formula(grid: list[list[int]]) -> Formule:
    """Generate the formula of forbidden values of all the cells

    Args:
        grid (list of list): modelized suduko grid

    Returns:
        formula (Formula): forbidden values of all the cells

    """
    formule = []
    for line_id in range(GRID_SIZE):
        for col_id in range(GRID_SIZE):
            if grid[line_id][col_id] == 0:
                forbidden_ij_form = forbidden_ij(grid, line_id, col_id)
                formule += forbidden_ij_form.clauses
    return Formule(formule)


def generate_grid_formula(grid: list[list[int]]) -> Formule:
    """Generate the formula obtained from the suduko grid to solve

    Note:
        - formula_data is F1
        - formula_forbidden is F2

    Args:
        grid (list of list): modelized sudoku grid

    Returns:
        formula (Formula): full formula from the grid to solve

    """
    formula_data = generate_data_formula(grid)
    formula_forbidden = generate_forbidden_formula(grid)
    return Formule(formula_data.clauses + formula_forbidden.clauses)


def generate_initial_formula(grid: list[list[int]]) -> Formule:
    """Generate the formula to solve (from the rules and the grid to solve)

    Args:
        grid (list of list): modelized sudoku grid

    Returns:
        formula (Formula): full formula from the rules and the grid to solve

    """
    grid_formula = generate_grid_formula(grid)
    rule_formula = generate_rule_formule()
    return Formule(grid_formula.clauses + rule_formula.clauses)
