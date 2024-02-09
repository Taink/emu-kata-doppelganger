from discount_applier import DiscountApplier

class FakeNotifier:
    def __init__(self):
        self.notified_users: list[str] = list()

    def notify(self, user, message):
        self.notified_users.append(user)
        
    def get_notified_users(self):
        return self.notified_users

def test_apply_v1():
    discount = 5
    fake_users = ['user1', 'user2', 'user3']
    notifier = FakeNotifier()

    discount_applier = DiscountApplier(notifier)
    discount_applier.apply_v1(discount, fake_users)
    notified_users = notifier.get_notified_users()
    
    assert len(notified_users) == len(fake_users)


def test_apply_v2():
    discount = 5
    fake_users = ['user1', 'user2', 'user3']
    notifier = FakeNotifier()

    discount_applier = DiscountApplier(notifier)
    discount_applier.apply_v1(discount, fake_users)
    notified_users = notifier.get_notified_users()
    
    assert notified_users == fake_users
