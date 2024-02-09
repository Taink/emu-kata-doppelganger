from safe_calculator import SafeCalculator

class MockAuthorizer:
     def authorize(self):
        return True

def test_divide_should_not_raise_any_error_when_authorized():
    authorizer = MockAuthorizer()
    calculator = SafeCalculator(authorizer)

    result = calculator.add(2,3)
    assert result == 5
    # pass
