# Overview

This exercise is inspired by the Informatic Session of the concours of Centrale PARIS, a french engineering school.
The document is available here: <link> [french]

# Purpose

This exercise has been designed to:

- Improve the modelization capacities of the teammates
- Play different roles of an engineering development production chain
- Implement advanced methods following a math model
- Test the production at different level of the software and at different steps of the development
- Promote good practices for development and CI integrations

The technical pillars of this exercise are: Modelization, Python, Multiprocessing

# Tool: Sudoku solver

## Installation

### From the repository

Execute the following line to install the tool:

	git clone <<<>>>
	cd <<<>>>
        python setup.py install

### From the package

TODO


## Usage


### List the solvers

Different solvers are available. They can be listed using:

	./sudoku-solver -l

### Format of the grid

The sudoku grid should be provided in a text file following:

	$ cat example_grid.txt

	0 9 0 2 0 0 6 0 5
	3 2 0 0 0 7 0 0 0
	0 7 0 9 0 5 0 0 8
	0 1 0 0 0 0 0 0 0
	0 0 7 0 0 0 0 9 4
	6 0 0 0 0 0 0 0 0
	0 0 8 0 0 0 0 0 7
	0 3 0 4 9 1 5 0 0
	0 0 0 0 0 3 0 0 0	

### Solve a grid of sudoku

If the solver is not defined, the default one is used.

	./sudoku-solver -g <path to the grid>

The solver can be selected by using:

	./sudoku-solver -g <path to the grid> -s <name of the solver>


### Solve grids of sudoku

	./sudoku-solver -g <list of paths to the grids, comma separated>


## Developers

### Execute the tests

The tests can be run with the following command:

	./run_tests.sh


# TODO list


- packaging/installation
- performance improvements
- move to full object modelization
- implement multiprocessing to solve grids in //
- add CI script for:
	- static analysis (pylint, black)
	- test executions
