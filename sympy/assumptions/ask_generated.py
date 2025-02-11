"""
The contents of this file are the return value of
``sympy.assumptions.ask.compute_known_facts``.

Do NOT manually edit this file.
Instead, run ./bin/ask_update.py.
"""

from sympy.core.cache import cacheit
from sympy.assumptions.cnf import Literal
from sympy.assumptions.ask import Q

@cacheit
def get_all_known_facts():
    """
    Known facts as CNF clauses. Used by satask.
    """
    return {
        frozenset((Literal(Q.algebraic, False), Literal(Q.imaginary, True), Literal(Q.transcendental, False))),
        frozenset((Literal(Q.algebraic, False), Literal(Q.negative, True), Literal(Q.transcendental, False))),
        frozenset((Literal(Q.algebraic, False), Literal(Q.positive, True), Literal(Q.transcendental, False))),
        frozenset((Literal(Q.algebraic, False), Literal(Q.rational, True))),
        frozenset((Literal(Q.algebraic, False), Literal(Q.transcendental, False), Literal(Q.zero, True))),
        frozenset((Literal(Q.algebraic, True), Literal(Q.finite, False))),
        frozenset((Literal(Q.algebraic, True), Literal(Q.transcendental, True))),
        frozenset((Literal(Q.antihermitian, False), Literal(Q.hermitian, False), Literal(Q.zero, True))),
        frozenset((Literal(Q.antihermitian, False), Literal(Q.imaginary, True))),
        frozenset((Literal(Q.commutative, False), Literal(Q.finite, True))),
        frozenset((Literal(Q.commutative, False), Literal(Q.infinite, True))),
        frozenset((Literal(Q.complex_elements, False), Literal(Q.real_elements, True))),
        frozenset((Literal(Q.composite, False), Literal(Q.even, True), Literal(Q.positive, True), Literal(Q.prime, False))),
        frozenset((Literal(Q.composite, True), Literal(Q.even, False), Literal(Q.odd, False))),
        frozenset((Literal(Q.composite, True), Literal(Q.positive, False))),
        frozenset((Literal(Q.composite, True), Literal(Q.prime, True))),
        frozenset((Literal(Q.diagonal, False), Literal(Q.lower_triangular, True), Literal(Q.upper_triangular, True))),
        frozenset((Literal(Q.diagonal, True), Literal(Q.lower_triangular, False))),
        frozenset((Literal(Q.diagonal, True), Literal(Q.normal, False))),
        frozenset((Literal(Q.diagonal, True), Literal(Q.symmetric, False))),
        frozenset((Literal(Q.diagonal, True), Literal(Q.upper_triangular, False))),
        frozenset((Literal(Q.even, False), Literal(Q.odd, False), Literal(Q.prime, True))),
        frozenset((Literal(Q.even, False), Literal(Q.zero, True))),
        frozenset((Literal(Q.even, True), Literal(Q.odd, True))),
        frozenset((Literal(Q.even, True), Literal(Q.rational, False))),
        frozenset((Literal(Q.finite, False), Literal(Q.transcendental, True))),
        frozenset((Literal(Q.finite, True), Literal(Q.infinite, True))),
        frozenset((Literal(Q.fullrank, False), Literal(Q.invertible, True))),
        frozenset((Literal(Q.fullrank, True), Literal(Q.invertible, False), Literal(Q.square, True))),
        frozenset((Literal(Q.hermitian, False), Literal(Q.negative, True))),
        frozenset((Literal(Q.hermitian, False), Literal(Q.positive, True))),
        frozenset((Literal(Q.hermitian, False), Literal(Q.zero, True))),
        frozenset((Literal(Q.imaginary, True), Literal(Q.negative, True))),
        frozenset((Literal(Q.imaginary, True), Literal(Q.positive, True))),
        frozenset((Literal(Q.imaginary, True), Literal(Q.zero, True))),
        frozenset((Literal(Q.infinite, False), Literal(Q.negative_infinite, True))),
        frozenset((Literal(Q.infinite, False), Literal(Q.positive_infinite, True))),
        frozenset((Literal(Q.integer_elements, True), Literal(Q.real_elements, False))),
        frozenset((Literal(Q.invertible, False), Literal(Q.positive_definite, True))),
        frozenset((Literal(Q.invertible, False), Literal(Q.singular, False))),
        frozenset((Literal(Q.invertible, False), Literal(Q.unitary, True))),
        frozenset((Literal(Q.invertible, True), Literal(Q.singular, True))),
        frozenset((Literal(Q.invertible, True), Literal(Q.square, False))),
        frozenset((Literal(Q.irrational, False), Literal(Q.negative, True), Literal(Q.rational, False))),
        frozenset((Literal(Q.irrational, False), Literal(Q.positive, True), Literal(Q.rational, False))),
        frozenset((Literal(Q.irrational, False), Literal(Q.rational, False), Literal(Q.zero, True))),
        frozenset((Literal(Q.irrational, True), Literal(Q.negative, False), Literal(Q.positive, False), Literal(Q.zero, False))),
        frozenset((Literal(Q.irrational, True), Literal(Q.rational, True))),
        frozenset((Literal(Q.lower_triangular, False), Literal(Q.triangular, True), Literal(Q.upper_triangular, False))),
        frozenset((Literal(Q.lower_triangular, True), Literal(Q.triangular, False))),
        frozenset((Literal(Q.negative, False), Literal(Q.positive, False), Literal(Q.rational, True), Literal(Q.zero, False))),
        frozenset((Literal(Q.negative, True), Literal(Q.positive, True))),
        frozenset((Literal(Q.negative, True), Literal(Q.zero, True))),
        frozenset((Literal(Q.negative_infinite, True), Literal(Q.positive_infinite, True))),
        frozenset((Literal(Q.normal, False), Literal(Q.unitary, True))),
        frozenset((Literal(Q.normal, True), Literal(Q.square, False))),
        frozenset((Literal(Q.odd, True), Literal(Q.rational, False))),
        frozenset((Literal(Q.orthogonal, False), Literal(Q.real_elements, True), Literal(Q.unitary, True))),
        frozenset((Literal(Q.orthogonal, True), Literal(Q.positive_definite, False))),
        frozenset((Literal(Q.orthogonal, True), Literal(Q.unitary, False))),
        frozenset((Literal(Q.positive, False), Literal(Q.prime, True))),
        frozenset((Literal(Q.positive, True), Literal(Q.zero, True))),
        frozenset((Literal(Q.square, False), Literal(Q.symmetric, True))),
        frozenset((Literal(Q.triangular, False), Literal(Q.unit_triangular, True))),
        frozenset((Literal(Q.triangular, False), Literal(Q.upper_triangular, True)))
    }

# -{ Known facts in compressed sets }-
@cacheit
def get_known_facts_dict():
    """
    Logical implication as dictionary. Key implies every item in its value.
    Used for quick lookup of single facts.
    """
    return {
        Q.algebraic: set([Q.algebraic, Q.commutative, Q.finite, ~Q.infinite,
        ~Q.negative_infinite, ~Q.positive_infinite,
        ~Q.transcendental]),
        Q.antihermitian: set([Q.antihermitian]),
        Q.commutative: set([Q.commutative]),
        Q.complex_elements: set([Q.complex_elements]),
        Q.composite: set([Q.algebraic, Q.commutative, Q.composite, Q.finite,
        Q.hermitian, Q.positive, Q.rational, ~Q.imaginary,
        ~Q.infinite, ~Q.irrational, ~Q.negative, ~Q.negative_infinite,
        ~Q.positive_infinite, ~Q.prime, ~Q.transcendental, ~Q.zero]),
        Q.diagonal: set([Q.diagonal, Q.lower_triangular, Q.normal, Q.square,
        Q.symmetric, Q.triangular, Q.upper_triangular]),
        Q.even: set([Q.algebraic, Q.commutative, Q.even, Q.finite,
        Q.hermitian, Q.rational, ~Q.imaginary, ~Q.infinite,
        ~Q.irrational, ~Q.negative_infinite, ~Q.odd,
        ~Q.positive_infinite, ~Q.transcendental]),
        Q.finite: set([Q.commutative, Q.finite, ~Q.infinite,
        ~Q.negative_infinite, ~Q.positive_infinite]),
        Q.fullrank: set([Q.fullrank]),
        Q.hermitian: set([Q.hermitian]),
        Q.imaginary: set([Q.antihermitian, Q.commutative, Q.finite,
        Q.imaginary, ~Q.composite, ~Q.even, ~Q.infinite,
        ~Q.irrational, ~Q.negative, ~Q.negative_infinite, ~Q.odd,
        ~Q.positive, ~Q.positive_infinite, ~Q.prime, ~Q.rational,
        ~Q.zero]),
        Q.infinite: set([Q.commutative, Q.infinite, ~Q.algebraic,
        ~Q.composite, ~Q.even, ~Q.extended_real, ~Q.finite, ~Q.imaginary, ~Q.irrational,
        ~Q.negative, ~Q.odd, ~Q.positive, ~Q.prime, ~Q.rational,
        ~Q.transcendental, ~Q.zero]),
        Q.integer_elements: set([Q.complex_elements, Q.integer_elements,
        Q.real_elements]),
        Q.invertible: set([Q.fullrank, Q.invertible, Q.square, ~Q.singular]),
        Q.irrational: set([Q.commutative, Q.finite, Q.hermitian, Q.irrational,
        ~Q.composite, ~Q.even, ~Q.imaginary, ~Q.infinite,
        ~Q.negative_infinite, ~Q.odd, ~Q.positive_infinite, ~Q.prime,
        ~Q.rational, ~Q.zero]),
        Q.is_true: set([Q.is_true]),
        Q.lower_triangular: set([Q.lower_triangular, Q.triangular]),
        Q.negative: set([Q.commutative, Q.finite, Q.hermitian, Q.negative,
        ~Q.composite, ~Q.imaginary, ~Q.infinite, ~Q.negative_infinite,
        ~Q.positive, ~Q.positive_infinite, ~Q.prime, ~Q.zero]),
        Q.negative_infinite: set([Q.commutative, Q.infinite,
        Q.negative_infinite, ~Q.algebraic, ~Q.composite, ~Q.even,
        ~Q.finite, ~Q.imaginary, ~Q.irrational, ~Q.negative, ~Q.odd,
        ~Q.positive, ~Q.positive_infinite, ~Q.prime, ~Q.rational,
        ~Q.transcendental, ~Q.zero]),
        Q.normal: set([Q.normal, Q.square]),
        Q.odd: set([Q.algebraic, Q.commutative, Q.finite, Q.hermitian, Q.odd,
        Q.rational, ~Q.even, ~Q.imaginary, ~Q.infinite, ~Q.irrational,
        ~Q.negative_infinite, ~Q.positive_infinite, ~Q.transcendental,
        ~Q.zero]),
        Q.orthogonal: set([Q.fullrank, Q.invertible, Q.normal, Q.orthogonal,
        Q.positive_definite, Q.square, Q.unitary, ~Q.singular]),
        Q.positive: set([Q.commutative, Q.finite, Q.hermitian, Q.positive,
        ~Q.imaginary, ~Q.infinite, ~Q.negative, ~Q.negative_infinite,
        ~Q.positive_infinite, ~Q.zero]),
        Q.positive_definite: set([Q.fullrank, Q.invertible,
        Q.positive_definite, Q.square, ~Q.singular]),
        Q.positive_infinite: set([Q.commutative, Q.infinite,
        Q.positive_infinite, ~Q.algebraic, ~Q.composite, ~Q.even,
        ~Q.finite, ~Q.imaginary, ~Q.irrational, ~Q.negative,
        ~Q.negative_infinite, ~Q.odd, ~Q.positive, ~Q.prime,
        ~Q.rational, ~Q.transcendental, ~Q.zero]),
        Q.prime: set([Q.algebraic, Q.commutative, Q.finite, Q.hermitian,
        Q.positive, Q.prime, Q.rational, ~Q.composite, ~Q.imaginary,
        ~Q.infinite, ~Q.irrational, ~Q.negative, ~Q.negative_infinite,
        ~Q.positive_infinite, ~Q.transcendental, ~Q.zero]),
        Q.rational: set([Q.algebraic, Q.commutative, Q.finite, Q.hermitian,
        Q.rational, ~Q.imaginary, ~Q.infinite, ~Q.irrational,
        ~Q.negative_infinite, ~Q.positive_infinite,
        ~Q.transcendental]),
        Q.real_elements: set([Q.complex_elements, Q.real_elements]),
        Q.singular: set([Q.singular, ~Q.invertible, ~Q.orthogonal,
        ~Q.positive_definite, ~Q.unitary]),
        Q.square: set([Q.square]),
        Q.symmetric: set([Q.square, Q.symmetric]),
        Q.transcendental: set([Q.commutative, Q.finite, Q.transcendental,
        ~Q.algebraic, ~Q.composite, ~Q.even, ~Q.infinite,
        ~Q.negative_infinite, ~Q.odd, ~Q.positive_infinite, ~Q.prime,
        ~Q.rational, ~Q.zero]),
        Q.triangular: set([Q.triangular]),
        Q.unit_triangular: set([Q.triangular, Q.unit_triangular]),
        Q.unitary: set([Q.fullrank, Q.invertible, Q.normal, Q.square,
        Q.unitary, ~Q.singular]),
        Q.upper_triangular: set([Q.triangular, Q.upper_triangular]),
        Q.zero: set([Q.algebraic, Q.commutative, Q.even, Q.finite,
        Q.hermitian, Q.rational, Q.zero, ~Q.composite, ~Q.imaginary,
        ~Q.infinite, ~Q.irrational, ~Q.negative, ~Q.negative_infinite,
        ~Q.odd, ~Q.positive, ~Q.positive_infinite, ~Q.prime,
        ~Q.transcendental]),
    }
