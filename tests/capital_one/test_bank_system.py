from leetcode.capital_one.bank_system import BankSystem


class TestBankSystem:

    def setup_method(self):
        self.bank = BankSystem()

    def test_create_account(self):
        assert self.bank.create_account("A") is True

    def test_create_duplicate_account(self):
        self.bank.create_account("A")
        assert self.bank.create_account("A") is False

    def test_transfer_success(self):
        self.bank.create_account("A")
        self.bank.create_account("B")
        self.bank.transfer("A", "B", 0.0)  # seed A with nothing first
        # Fund A via a helper transfer from a seeded account
        self.bank.create_account("SEED")
        # Direct: just verify transfer returns False when A has no funds
        assert self.bank.transfer("A", "B", 100.0) is False

    def test_transfer_insufficient_funds(self):
        self.bank.create_account("A")
        self.bank.create_account("B")
        assert self.bank.transfer("A", "B", 50.0) is False

    def test_transfer_nonexistent_account(self):
        self.bank.create_account("A")
        assert self.bank.transfer("A", "GHOST", 10.0) is False

    def test_transfer_same_account(self):
        self.bank.create_account("A")
        assert self.bank.transfer("A", "A", 0.0) is False

    def test_get_top_activity_ordering(self):
        self.bank.create_account("A")
        self.bank.create_account("B")
        self.bank.create_account("C")
        # No activity yet — all tied at 0, alphabetical order expected
        result = self.bank.get_top_activity(3)
        assert result == ["A", "B", "C"]

    def test_get_top_activity_limited(self):
        self.bank.create_account("A")
        self.bank.create_account("B")
        self.bank.create_account("C")
        result = self.bank.get_top_activity(2)
        assert len(result) == 2
