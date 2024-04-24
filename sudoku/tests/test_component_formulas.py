"""

"""
import pytest

from sudoku import formulas
from sudoku.dataset import ALL_SUDOKUS


class TestFormulas:

    def test_formula_rules(self):
        rule_formula = formulas.generate_rule_formule()
        assert len(rule_formula) == 11988

    def test_formula_grid(self):
        grid_formula = formulas.generate_grid_formula(ALL_SUDOKUS["easy"])
        assert len(grid_formula) <= 9**3
