#!/usr/bin/env bash

# Run all the different tests available for the module
# Returns 0 if everything is OK, or 1 if there is an error

FILE_LIST="__main__.py dataset.py formulas.py objects.py operations.py solvers.py"
PYTHON_BIN="python3.11"
PYLINT_CONFIG_PATH="tests/pylint-config-file"


export PYTHONPATH=$PYTHONPATH:sudoku/


# BLACK PART
echo "[static-analysis] Execute black"
sa_black_error=0
for filename in ${FILE_LIST}
do
  echo "[static-analysis] run black on ${filename}"
  res=$(${PYTHON_BIN} -m black --line-length 100 --check --quiet sudoku/${filename})
  rtcode=$?

  if [ $rtcode -ne 0 ]; then
    echo "[static-analysis][error] black failed with ${filename}"
    echo "[static-analysis][error} review the file with '${PYTHON_BIN} -m black --diff --line-length 100 ${filename}'"
    sa_black_error=$(($sa_black_error + 1))
  fi
done

if [ $sa_black_error -ne 0 ]; then
    echo "[static-analysis][error] ${sa_black_error} files are not formatted as expected"
fi


# PYLINT PART
echo "[static-analysis] Execute pylint"
sa_pylint_error=0
for filename in ${FILE_LIST}
do
  echo "[static-analysis] run pylint on ${filename}"
  res=$(${PYTHON_BIN} -m pylint sudoku/${filename})
  rtcode=$?

  if [ $rtcode -ne 0 ]; then
    echo "[static-analysis][error] pylint failed with ${filename}"
    echo "[static-analysis][error} review the file with '${PYTHON_BIN} -m pylint --rcfile tests/pylint-config-file ${filename}'"
    sa_pylint_error=$(($sa_pylint_error + 1))
  fi
done

if [ $sa_pylint_error -ne 0 ]; then
    echo "[static-analysis][error] ${sa_pylint_error} files are not coded as expected"
fi

# PYTEST PART
echo "Execute the full testsuite"
${PYTHON_BIN} -m pytest -vv tests/
tt_pytest_errors=$?

sa_total_error=$(($sa_black_error + $sa_pylint_error + $tt_pytest_errors))
if [ $sa_total_error -ne 0 ]; then
    echo "TEST FAILED"
    exit 1
fi

echo "TEST OK"
exit 0
