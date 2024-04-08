"""Base Classes to represent mathematical objects"""
import itertools


MIN_VALUE = 1
MAX_VALUE = 9


class Litteral:
    """A litteral is [...]"""

    def __init__(self, sign: bool, i: int, j: int, k: int):
        if not all(itertools.starmap(isinstance, [(i, int), (j, int), (k, int)])):
            raise TypeError("i, j and k shall be integer")

        if not 0 <= i <= MAX_VALUE - 1 or not 0 <= j <= MAX_VALUE - 1:
            raise TypeError("The index values musst be included in ...")

        error_msg = "The value of the litteral must be included in [{}, {}]"
        error_msg = error_msg.format(MIN_VALUE, MAX_VALUE)
        if not MIN_VALUE <= k <= MAX_VALUE:
            raise TypeError(error_msg)

        if not isinstance(sign, bool):
            raise TypeError("The sign of the litteral must be a boolean")

        self.sign = sign
        self.i, self.j = i, j
        self.k = k

    def __eq__(self, litt):
        cond1 = self.sign == litt.sign
        cond2 = self.i == litt.i and self.j == litt.j
        cond3 = self.k == litt.k

        return cond1 and cond2 and cond3

    def __hash__(self):
        return hash((self.sign, self.i, self.j, self.k))

    def __invert__(self):
        return Litteral(not self.sign, self.i, self.j, self.k)

    def __repr__(self):
        str_sign = "" if self.sign else "¬"
        msg = f"{str_sign}X[k={self.k}]({self.i},{self.j})"
        return msg


class Clause:
    """A clause is a set of Litteral corresponding to a global constraint"""

    def __init__(self, litts: list[Litteral]):
        self.litts = litts

    def __add__(self, clause):
        return Clause(self.litts.append(clause))

    def __contains__(self, litt: Litteral) -> bool:
        return litt in self.litts

    def __eq__(self, clause) -> bool:
        return not any(litt not in self.litts for litt in clause.litts)

    def __iter__(self):
        for litt in self.litts:
            yield litt

    def __len__(self):
        return len(self.litts)

    def __repr__(self):
        msg = " v ".join([repr(litt) for litt in self.litts])
        return msg


class Formule:
    """A formula is a set of Clause corresponding to a multiple constraints"""

    def __init__(self, clauses: list[Clause]):
        self.clauses = clauses

    def __add__(self, formule):
        return Formule(self.clauses + formule.clauses)

    def __contains__(self, clause: Clause) -> bool:
        return clause in self.clauses

    def __iter__(self):
        for clause in self.clauses:
            yield clause

    def __len__(self):
        return len(self.clauses)

    def __repr__(self):
        msg = " ^ ".join([repr(clause) for clause in self.clauses])
        return msg
