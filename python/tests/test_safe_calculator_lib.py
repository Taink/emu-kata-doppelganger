from safe_calculator import SafeCalculator
from unittest.mock import MagicMock

def test_add_authorized():
    calculator = SafeCalculator(MagicMock(return_value=True))
    assert calculator.add(1, 2) == 3