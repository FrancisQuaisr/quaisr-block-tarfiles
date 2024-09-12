"""Implementation of addition"""

from typing import Union

from quaisr import WireOutput


def add(
    lhs: Union[float, int, complex],
    rhs: Union[float, int, complex],
    sum: WireOutput,  # pylint: disable=redefined-builtin
) -> None:
    """
    Add two values and return the sum.
    """
    sum.write_any(lhs + rhs)
