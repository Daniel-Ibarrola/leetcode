from leetcode.capital_one.banking_system import BankingSystem


class TestBankingSystem:

    def test_create_account_success_and_duplicate(self):
        system = BankingSystem()
        assert system.create_account("account1") is True
        assert system.create_account("account1") is False
        assert system.create_account("account2") is True

    def test_deposit_to_existing_account(self):
        system = BankingSystem()
        system.create_account("account1")
        assert system.deposit("account1", 2700) == 2700
        assert system.deposit("account1", 300) == 3000

    def test_deposit_to_missing_account(self):
        system = BankingSystem()
        assert system.deposit("non-existing", 2700) == -1

    def test_transfer_success(self):
        system = BankingSystem()
        system.create_account("account1")
        system.create_account("account2")
        system.deposit("account1", 2700)

        assert system.transfer("account1", "account2", 200) == 2500
        assert system.deposit("account2", 0) == 200

    def test_transfer_insufficient_funds(self):
        system = BankingSystem()
        system.create_account("account1")
        system.create_account("account2")
        system.deposit("account1", 2700)

        assert system.transfer("account1", "account2", 2701) == -1
        assert system.deposit("account1", 0) == 2700

    def test_transfer_same_account(self):
        system = BankingSystem()
        system.create_account("account1")
        system.deposit("account1", 100)

        assert system.transfer("account1", "account1", 50) == -1

    def test_transfer_missing_from_account(self):
        system = BankingSystem()
        system.create_account("account2")

        assert system.transfer("non-existing", "account2", 100) == -1

    def test_transfer_missing_to_account(self):
        system = BankingSystem()
        system.create_account("account1")
        system.deposit("account1", 100)

        assert system.transfer("account1", "non-existing", 50) == -1

    def test_top_activity_fewer_accounts_than_n(self):
        system = BankingSystem()
        system.create_account("account1")
        system.deposit("account1", 100)

        assert system.top_activity(5) == ["account1(100)"]

    def test_top_activity_orders_by_descending_activity(self):
        system = BankingSystem()
        system.create_account("account1")
        system.create_account("account2")
        system.create_account("account3")
        system.deposit("account1", 500)
        system.deposit("account2", 900)
        system.deposit("account3", 300)

        assert system.top_activity(2) == ["account2(900)", "account1(500)"]

    def test_top_activity_breaks_ties_alphabetically(self):
        system = BankingSystem()
        system.create_account("account2")
        system.create_account("account3")
        system.deposit("account3", 4000)
        system.deposit("account2", 4000)

        assert system.top_activity(2) == ["account2(4000)", "account3(4000)"]

    def test_top_activity_sorts_by_activity_then_account_id(self):
        system = BankingSystem()
        system.create_account("charlie")
        system.create_account("bravo")
        system.create_account("delta")
        system.create_account("alpha")
        system.deposit("charlie", 500)
        system.deposit("bravo", 500)
        system.deposit("delta", 900)
        system.deposit("alpha", 500)

        assert system.top_activity(4) == [
            "delta(900)",
            "alpha(500)",
            "bravo(500)",
            "charlie(500)",
        ]

    def test_transfer_counts_activity_for_both_accounts(self):
        system = BankingSystem()
        system.create_account("account1")
        system.create_account("account2")
        system.deposit("account1", 1000)

        system.transfer("account1", "account2", 400)

        assert system.top_activity(2) == ["account1(1400)", "account2(400)"]

    def test_unsuccessful_transactions_do_not_count_towards_activity(self):
        system = BankingSystem()
        system.create_account("account1")
        system.create_account("account2")
        system.deposit("account1", 100)

        system.transfer("account1", "account2", 500)  # insufficient funds
        system.transfer("account1", "account1", 10)  # same account

        assert system.top_activity(2) == ["account1(100)", "account2(0)"]

    def test_full_operations_sequence(self):
        system = BankingSystem()

        assert system.create_account("account1") is True
        assert system.create_account("account1") is False
        assert system.create_account("account2") is True
        assert system.deposit("non-existing", 2700) == -1
        assert system.deposit("account1", 2700) == 2700
        assert system.transfer("account1", "account2", 2701) == -1
        assert system.transfer("account1", "account2", 200) == 2500
        assert system.transfer("account1", "account2", 2500) == 0
        assert system.deposit("account2", 300) == 3000
        assert system.create_account("account3") is True
        assert system.deposit("account3", 4000) == 4000
        assert system.top_activity(3) == [
            "account1(5400)",
            "account3(4000)",
            "account2(3000)",
        ]
        assert system.deposit("account2", 1000) == 4000
        assert system.top_activity(2) == ["account1(5400)", "account2(4000)"]
        assert system.top_activity(5) == [
            "account1(5400)",
            "account2(4000)",
            "account3(4000)",
        ]
