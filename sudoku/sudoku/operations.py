"""This module describes the high-level behaviour of the Sudoku solver

The implementation is inspired from the concours Centrale/Supelec
(Computer Science - 2014), french engineer schools:

    https://www.concours-centrale-supelec.fr/CentraleSupelec/2014/MP/sujets/2012-013.pdf

"""


def contains(element: object, container: list[object]) -> bool:
    """Is an element in the container

    Args:
        element: object to compare into the object list
        container: list of elements

    Returns:
        a boolean

    """
    return element in container


def delete(element: object, container: list[object]) -> None:
    """Delete of the items equal to element in the container

    Args:
        element: object to compare into the object list
        container: list of elements
    """
    while contains(element, container):
        container.remove(element)


def add(element: object, container: list[object]) -> None:
    """Add an element in a container if it does not exist in the container

    Args:
        element: object to compare into the object list
        container: list of elements

    """
    if not contains(element, container):
        container.append(element)


def index(block_id: int, element_id: int) -> tuple[int, int]:
    """Convert the position of a cell from a block/element_block format to raw/col format"""
    if block_id not in range(0, 9):
        raise ValueError("block_id value is not between 0 and 9")
    if element_id not in range(0, 9):
        raise ValueError("element_id value is not between 0 and 9")

    step = 3

    mod_block = block_id % step
    div_block = block_id // step
    mod_elt = element_id % step
    div_elt = element_id // step

    j = step * mod_block + mod_elt
    i = step * div_block + div_elt

    return i, j
