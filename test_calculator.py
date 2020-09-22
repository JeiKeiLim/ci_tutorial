"""
Testing calculator classes implemented in calculator.py.

 - Author: Jongkuk Lim
 - Email: lim.jeikei@gmail.com
 - Date: 2020. 09.22.
"""

from calculator import Adder, Divider, Multiplier, Subtractor


class TestCalculator:
    """Calculator tester class."""

    def test_add(self):
        """Adder test function."""
        assert Adder().operate(5, 2) == 7

    def test_sub(self):
        """Subtractor test function."""
        assert Subtractor().operate(5, 2) == 3

    def test_mul(self):
        """Multiplier test function."""
        assert Multiplier().operate(5, 2) == 10

    def test_div(self):
        """Divider test function."""
        assert Divider().operate(5, 2) == 2
