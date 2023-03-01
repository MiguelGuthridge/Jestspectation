"""
Jestspectation
==============

Pattern matching helper classes designed to be similar to Jest's expect
matchers, but modified to suit a Pythonic style of programming.
"""

from .__any import Any, Anything
from .__containers import (
    DictContainingKeys,
    DictContainingValues,
    DictContainingItems,
    ListContaining,
    SetContaining,
)
from .__float_approx import FloatApprox
from .__equals import Equals, Is
from .logicals import And, Not, Or, Xor
from .__strings import (
    StringMatchingRegex,
    StringContaining,
    TextLike,
    LinesLike,
)


__all__ = [
    'And',
    'Any',
    'Anything',
    'DictContainingKeys',
    'DictContainingValues',
    'DictContainingItems',
    'Equals',
    'FloatApprox',
    'Is',
    'LinesLike',
    'ListContaining',
    'Not',
    'Or',
    'SetContaining',
    'StringContaining',
    'StringMatchingRegex',
    'TextLike',
    'Xor',
]
