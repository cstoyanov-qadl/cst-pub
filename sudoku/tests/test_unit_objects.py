
import pytest

import objects

TESTCASE_LITTERAL_CREATION = [
    ("valid corner 1", (True, 0, 0, 1)),
    ("valid corner 2", (True, 0, 8, 9)),
    ("valid corner 3", (True, 8, 8, 1)),
    ("valid corner 4", (True, 8, 0, 9)),
]


TESTCASE_LITTERAL_CREATION_ERROR = [
    ("empty args", ()),
    ("not enough args 1", (1,)),
    ("not enough args 2", (1, 2)),
    ("not enough args 3", (1, 2, 3)),
    ("invalid value min", (True, 0, 0, 0)),
    ("invalid value max", (True, 0, 0, 10)),
    ("invalid type 1", (True, "bla", 0, 1)),
    ("invalid type 2", (True, 0, "bla", 1)),
    ("invalid type 3", (True, 0, 0, "bla")),
    ("invalid type 4", (0, 0, 0, 1)),
    ("invalid range 1", (True, -1, 0, 1)),
    ("invalid range 2", (True, 0, -1, 1)),
    ("invalid range 3", (True, 9, 0, 1)),
    ("invalid range 4", (True, 0, 9, 1)),
]


@pytest.fixture(params=TESTCASE_LITTERAL_CREATION)
def tc_litteral_creation(request):
    return request.param[1]


@pytest.fixture(params=TESTCASE_LITTERAL_CREATION_ERROR)
def tc_litteral_creation_error(request):
    return request.param[1]


class TestLitteral:

    def test_creation_valid(self, tc_litteral_creation):
        objects.Litteral(*tc_litteral_creation)

    def test_creation_error(self, tc_litteral_creation_error):
        with pytest.raises(TypeError):
            objects.Litteral(*tc_litteral_creation_error)

    def test_equal(self):
        assert objects.Litteral(True, 0, 0, 1) == objects.Litteral(True, 0, 0, 1)

    def test_different(self):
        assert objects.Litteral(True, 0, 0, 1) != objects.Litteral(True, 0, 0, 2)
        assert objects.Litteral(True, 0, 0, 1) != objects.Litteral(False, 0, 0, 1)
        assert objects.Litteral(True, 0, 0, 1) != objects.Litteral(True, 1, 0, 1)
        assert objects.Litteral(True, 0, 0, 1) != objects.Litteral(True, 0, 1, 1)

    def test_invert(self):
        litteral = objects.Litteral(True, 0, 0, 1)
        assert ~litteral == objects.Litteral(False, 0, 0, 1)
        assert ~~litteral == litteral


class TestClause:

    def test_clause_creation(self):
        objects.Clause([objects.Litteral(True, 0, 0, 1)])

    def test_clause_creation_error(self):
        with pytest.raises(TypeError):
            objects.Clause()

    def test_clause_add(self):
        pass

    def test_clause_contains(self):
        pass

    def test_clause_len(self):
        pass


class TestFormule:

    def test_formule_creation(self):
        pass

    def test_formule_creation_error(self):
        pass

    def test_formule_add(self):
        litteral_a = objects.Litteral(True, 0, 0, 1)
        litteral_b = objects.Litteral(True, 0, 1, 2)
        clause_a = objects.Clause([litteral_a])
        clause_b = objects.Clause([litteral_b])
        formule_a = objects.Formule([clause_a])
        formule_b = objects.Formule([clause_b])
        formule_c = objects.Formule([clause_a, clause_b])
        formule = formule_a + formule_b

        assert formule.clauses == formule_c.clauses

    def test_formule_contains(self):
        pass
