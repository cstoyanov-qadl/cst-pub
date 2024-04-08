"""Unittest of the module operations.py

"""
import pytest

from operations import index


# INDEX TESTCASES STRUCTURE:
# (testname<str>, input<tuple>, expected output<tuple>)
INDEX_TESTCASES = [
    # TESTCASE 1
    ("fixed point (min) transformation", (0, 0), (0, 0)),
    ("fixed point (mid) transformation", (4, 4), (4, 4)),
    ("fixed point (max) transformation", (8, 8), (8, 8)),
    ("exercice value transformation", (3, 6), (5, 0)),
    ("another value transformation", (6, 6), (8, 0)),
]


# INDEX ERROR TESTCASES STRUCTURE:
# (testname<str>, input<tuple>, expected output<tuple>)
INDEX_ERROR_TESTCASES = [
    # TESTCASE 1
    ("out of range transformation (low)", (-1, 6), ValueError),
    ("out of range transformation (high)", (9, 6), ValueError),
]


@pytest.fixture(params=INDEX_TESTCASES)
def vector_index(request):
    """Provide nominal testcases for the function index() """
    return request.param


@pytest.fixture(params=INDEX_ERROR_TESTCASES)
def error_vector_index(request):
    """Provide error testcases for the function index() """
    return request.param


def test_index(vector_index):
    """ """
    original_index = vector_index[1]
    expected_converted_index = vector_index[2]

    converted_index = index(*original_index)
    assert converted_index == expected_converted_index


def test_error_index(error_vector_index):
    """ """
    original_index = error_vector_index[1]
    expected_converted_exp = error_vector_index[2]

    with pytest.raises(expected_converted_exp):
        index(*original_index)
