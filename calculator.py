"""Integer calculator including add, subtract, multiply, and divide.

- Author: Jongkuk Lim
- Date: 2020. 09. 16.

amix/vimrc

01. Formatter:
- Standard: PEP8
- Black:
- Isort:

02. Linter
- Flake8: bugbear, pep8-naming, flake8-docstrings
- Mypy: https://github.com/python/mypy
- Pylint: https://pypi.org/project/pylint/

03. Unit test
- doctest
- pytest
  + pytest-pylint
  + pytest-flake8
  + pytest-mypy
  + pytest-cov

HW:
1. Formatter + Linter + pre-commit hook
2. Unit test: pytest + extensions
3. Dockerfile creation(Miniconda base + requirements install)
4. CircleCI(Automation test) / GitHub Actions : Formatting + Linting + Unit test
"""

from abc import ABC, abstractmethod


class Calculator(ABC):
    """Abstract calculator interface"""

    @abstractmethod
    def operate(self, x, y):
        """Abstract method that is inherited by a specific mathmatical operations
        Args:
            x (int): left operand
            y (int): right operand

        Returns:
            int: operation result
        """
        pass

class Adder(Calculator):
    """Add operation."""
    def operate(self, x, y):
        """Operate add.

        Test:
        >>> Adder().operate(1, 0)
        1
        >>> Adder().operate(1, -2)
        -1
        """
        return x+y

class Subtractor(Calculator):
    """Subract operation."""
    def operate(self, x, y):
        """Operate subtract.

        Test:
        >>> Subtractor().operate(4, 2)
        2
        >>> Subtractor().operate(1, -2)
        3
        >>> Subtractor().operate(1, 2)
        -1
        """
        return x-y

class Multiplier(Calculator):
    """Multiply operation."""
    def operate(self, x, y):
        """Operate multiply.

        Test:
        >>> Multiplier().operate(1, 0)
        0
        >>> Multiplier().operate(1, -2)
        -2
        >>> Multiplier().operate(5, 3)
        15
        """
        return x*y

class Divider(Calculator):
    """Dividing operation."""
    def operate(self, x, y):
        """Operate divide.

        Test:
        >>> Divider().operate(1, 0)
        Traceback (most recent call last):
        ...
        ZeroDivisionError: integer division or modulo by zero
        >>> Divider().operate(5, 2)
        2
        >>> Divider().operate(5, -2)
        -3
        """
        return x//y


if __name__ == "__main__":
    import doctest

    doctest.testmod()