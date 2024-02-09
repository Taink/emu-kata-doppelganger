from discount_applier import DiscountApplier
from unittest.mock import MagicMock

def test_apply_v1():
    notifier  = MagicMock()
    applier    = DiscountApplier(notifier)
    users = ['user1', 'user2', 'user3']
    discount = 10
    applier.apply_v1(discount, users)
    assert notifier.notify.call_count == 3

def test_apply_v2():
    notifier  = MagicMock()
    applier   = DiscountApplier(notifier)
    users = ['user1', 'user2', 'user3']
    discount = 10
    
    applier.apply_v2(discount, users)
    notifier.notify.assert_called_with('user1', discount)
    notifier.notify.assert_called_with('user2', discount)
    notifier.notify.assert_called_with('user3', discount)
    assert notifier.notify.call_count == 3
