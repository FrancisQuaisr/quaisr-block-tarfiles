"""Test addition block."""

from quaisr.test import MockOutput

from addition.add import add


def test_add() -> None:
    """Test that addition adds"""
    with MockOutput("sum") as sum:  # pylint: disable=redefined-builtin
        sum.enqueue_expected(5)
        add(2, 3, sum)
