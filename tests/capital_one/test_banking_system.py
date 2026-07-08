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

    # -- Level 2: scheduled payments --------------------------------------

    def test_schedule_payment_returns_incrementing_ids(self):
        system = BankingSystem()
        system.create_account("account1")
        system.create_account("account2")

        assert system.schedule_payment("account1", 100, 5) == "payment1"
        assert system.schedule_payment("account2", 50, 3) == "payment2"
        assert system.schedule_payment("account1", 10, 1) == "payment3"

    def test_schedule_payment_missing_account_returns_empty_string(self):
        system = BankingSystem()
        assert system.schedule_payment("non-existing", 100, 5) == ""

    def test_schedule_payment_does_not_immediately_affect_balance(self):
        system = BankingSystem()
        system.create_account("account1")
        system.deposit("account1", 1000)

        system.schedule_payment("account1", 200, 5)

        assert system.deposit("account1", 0) == 1000

    def test_get_payment_status_is_pending_before_due_time(self):
        system = BankingSystem()
        system.create_account("account1")
        system.deposit("account1", 1000)
        payment_id = system.schedule_payment("account1", 200, 10)

        system.advance_time(9)

        assert system.get_payment_status("account1", payment_id) == "PENDING"
        assert system.deposit("account1", 0) == 1000

    def test_advance_time_processes_due_payment(self):
        system = BankingSystem()
        system.create_account("account1")
        system.deposit("account1", 1000)
        payment_id = system.schedule_payment("account1", 200, 5)

        system.advance_time(5)

        assert system.get_payment_status("account1", payment_id) == "PROCESSED"
        assert system.deposit("account1", 0) == 800
        assert system.top_activity(1) == ["account1(1200)"]

    def test_advance_time_processes_zero_delay_payment(self):
        system = BankingSystem()
        system.create_account("account1")
        system.deposit("account1", 1000)
        payment_id = system.schedule_payment("account1", 200, 0)

        system.advance_time(0)

        assert system.get_payment_status("account1", payment_id) == "PROCESSED"
        assert system.deposit("account1", 0) == 800

    def test_advance_time_accumulates_across_multiple_calls(self):
        system = BankingSystem()
        system.create_account("account1")
        system.deposit("account1", 1000)
        payment_id = system.schedule_payment("account1", 200, 10)

        system.advance_time(4)
        system.advance_time(4)
        assert system.get_payment_status("account1", payment_id) == "PENDING"

        system.advance_time(2)
        assert system.get_payment_status("account1", payment_id) == "PROCESSED"
        assert system.deposit("account1", 0) == 800

    def test_advance_time_fails_payment_with_insufficient_funds(self):
        system = BankingSystem()
        system.create_account("account1")
        system.deposit("account1", 100)
        payment_id = system.schedule_payment("account1", 500, 5)

        system.advance_time(5)

        assert system.get_payment_status("account1", payment_id) == "FAILED"
        assert system.deposit("account1", 0) == 100
        assert system.top_activity(1) == ["account1(100)"]

    def test_cancel_payment_before_due_time_succeeds(self):
        system = BankingSystem()
        system.create_account("account1")
        system.deposit("account1", 1000)
        payment_id = system.schedule_payment("account1", 200, 5)

        assert system.cancel_payment("account1", payment_id) is True
        assert system.get_payment_status("account1", payment_id) == "CANCELLED"

        system.advance_time(10)

        assert system.get_payment_status("account1", payment_id) == "CANCELLED"
        assert system.deposit("account1", 0) == 1000

    def test_cancel_payment_after_processed_returns_false(self):
        system = BankingSystem()
        system.create_account("account1")
        system.deposit("account1", 1000)
        payment_id = system.schedule_payment("account1", 200, 5)

        system.advance_time(5)

        assert system.cancel_payment("account1", payment_id) is False

    def test_cancel_payment_wrong_account_returns_false(self):
        system = BankingSystem()
        system.create_account("account1")
        system.create_account("account2")
        system.deposit("account1", 1000)
        payment_id = system.schedule_payment("account1", 200, 5)

        assert system.cancel_payment("account2", payment_id) is False
        assert system.get_payment_status("account1", payment_id) == "PENDING"

    def test_cancel_payment_unknown_account_or_payment_returns_false(self):
        system = BankingSystem()
        system.create_account("account1")
        payment_id = system.schedule_payment("account1", 100, 5)

        assert system.cancel_payment("non-existing", payment_id) is False
        assert system.cancel_payment("account1", "payment999") is False

    def test_get_payment_status_unknown_returns_empty_string(self):
        system = BankingSystem()
        system.create_account("account1")

        assert system.get_payment_status("account1", "payment999") == ""
        assert system.get_payment_status("non-existing", "payment1") == ""

    # -- Level 3 (bonus): merging accounts ---------------------------------

    def test_merge_accounts_combines_balance_and_activity(self):
        system = BankingSystem()
        system.create_account("account1")
        system.create_account("account2")
        system.deposit("account1", 1000)
        system.deposit("account2", 500)

        assert system.merge_accounts("account1", "account2") is True
        assert system.deposit("account1", 0) == 1500
        assert system.top_activity(1) == ["account1(1500)"]

    def test_merge_accounts_same_id_returns_false(self):
        system = BankingSystem()
        system.create_account("account1")

        assert system.merge_accounts("account1", "account1") is False

    def test_merge_accounts_missing_account_returns_false(self):
        system = BankingSystem()
        system.create_account("account1")

        assert system.merge_accounts("account1", "non-existing") is False
        assert system.merge_accounts("non-existing", "account1") is False

    def test_merge_accounts_removes_second_account(self):
        system = BankingSystem()
        system.create_account("account1")
        system.create_account("account2")
        system.deposit("account2", 500)

        system.merge_accounts("account1", "account2")

        assert system.deposit("account2", 100) == -1
        assert system.create_account("account2") is True

    def test_merge_accounts_transfers_pending_payments_to_first_account(self):
        system = BankingSystem()
        system.create_account("account1")
        system.create_account("account2")
        system.deposit("account1", 1000)
        system.deposit("account2", 1000)
        payment_id = system.schedule_payment("account2", 300, 5)

        system.merge_accounts("account1", "account2")
        system.advance_time(5)

        assert system.get_payment_status("account1", payment_id) == "PROCESSED"
        assert system.deposit("account1", 0) == 1700
