from discount_applier import DiscountApplier

def test_apply_v1():
    discount = 5
    fake_users = ['user1', 'user2', 'user3']
    notified_users = list()

    class FakeNotifier:
        def notify(self, user, message):
            notified_users.append(user)
            
    discount_applier = DiscountApplier(FakeNotifier())
    discount_applier.apply_v1(discount, fake_users)
    
    assert fake_users == notified_users


def test_apply_v2():
    expected_users = ['user1', 'user2', 'user3']    
    notified_users: list[str] = list()

    class FakeNotifier:
        def notify(self, user, message):
            notified_users.append(user)
    
    discount_applier = DiscountApplier(FakeNotifier())
    discount_applier.apply_v2(5, expected_users)

    assert notified_users == expected_users
