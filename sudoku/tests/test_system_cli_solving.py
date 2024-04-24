#!/usr/bin/env -S python3.11 -m pytest
"""This module contains the functional system-tests of the Software Under Test
"""

import subprocess

import pytest

from .conftest import simple_testcase_displayer
from .conftest import EASY_001_UNSOLVED
from .conftest import EASY_002_SOLVED
from .conftest import MEDIUM_001_SOLVED
from .conftest import MASTER_001_SOLVED


BINARY_PATH = "sudoku"

# NOTE: These options, if modified, change the behaviour of subprocess.run
SUBCOMMAND_OPTS = dict(shell=True, capture_output=True, text=True)
BASE_COMMAND = BINARY_PATH + " -g ../sudoku/grids/{} -s {}"


# Description of the testcases
TESTCASES = [
    dict(
        testname="solve simple with unitary-propagation (cannot be solved)",
        command=BASE_COMMAND.format("easy_001.txt", "unitary-propagation"),
        returncode=0,
        stdout=EASY_001_UNSOLVED,
        stderr=""),
    dict(
        testname="solve simple with unitary-propagation",
        command=BASE_COMMAND.format("easy_002.txt", "unitary-propagation"),
        returncode=0,
        stdout=EASY_002_SOLVED,
        stderr=""),
    dict(
        testname="solve simple with unfructuous-litteral",
        command=BASE_COMMAND.format("easy_002.txt", "unfructuous-litteral"),
        returncode=0,
        stdout=EASY_002_SOLVED,
        stderr=""),
    dict(
        testname="solve medium with unfructuous-litteral",
        command=BASE_COMMAND.format("medium_001.txt", "unfructuous-litteral"),
        returncode=0,
        stdout=MEDIUM_001_SOLVED,
        stderr=""),
    dict(
        testname="solve master with unfructuous-litteral",
        command=BASE_COMMAND.format("master_001.txt", "unfructuous-litteral"),
        returncode=0,
        stdout=MASTER_001_SOLVED,
        stderr=""),
]


@pytest.fixture(params=TESTCASES, ids=simple_testcase_displayer)
def testcase(request):
    """Fixture that provides the testcase one per one"""
    return request.param


class TestCommandNoSolving:
    """Test the commands that do not lead to solve a grid"""

    def test_output_info(self, testcase):
        """Execute the given command to validate the CLI behaviour of the tool

        Expected results:
            The following items must be validated (accordingly to the testcase)
            - the return code
            - the standard output
            - the standard error

        """
        output = subprocess.run(testcase["command"], **SUBCOMMAND_OPTS)
        assert output.returncode == testcase["returncode"]
        assert output.stdout.strip() == testcase["stdout"]
        assert output.stderr.strip() == testcase["stderr"]
