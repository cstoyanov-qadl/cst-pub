#!/usr/bin/env -S python3.11 -m pytest
"""This module contains the functional system-tests of the Software Under Test
"""

import subprocess

import pytest

from .conftest import simple_testcase_displayer
from .conftest import SUDOKU_CLI_USAGE
from .conftest import SUDOKU_CLI_MISSING_ARGS
from .conftest import SUDOKU_CLI_EXP_ARGS
from .conftest import SUDOKU_CLI_MANDAT_ARGS


BINARY_PATH = "sudoku"

# NOTE: These options, if modified, change the behaviour of subprocess.run
SUBCOMMAND_OPTS = dict(shell=True, capture_output=True, text=True)


# Description of the testcases
TESTCASES = [
    dict(
        testname="command usage",
        command=f"{BINARY_PATH} --help",
        returncode=0,
        stdout=SUDOKU_CLI_USAGE,
        stderr=""),
    dict(
        testname="no arg command",
        command=f"{BINARY_PATH}",
        returncode=2,
        stdout="",
        stderr=SUDOKU_CLI_MISSING_ARGS),
    dict(
        testname="exp arg command",
        command=f"{BINARY_PATH} -g",
        returncode=2,
        stdout="",
        stderr=SUDOKU_CLI_EXP_ARGS),
    dict(
        testname="missing mandatory arg",
        command=f"{BINARY_PATH} -l",
        returncode=2,
        stdout="",
        stderr=SUDOKU_CLI_MANDAT_ARGS),
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
