from leetcode.capital_one.account_balances import get_account_balances


class TestGetAccountBalances:

    def test_basic(self):
        transactions = [
            {"account_id": "A1", "type": "credit", "amount": 200.0},
            {"account_id": "A2", "type": "credit", "amount": 500.0},
            {"account_id": "A1", "type": "debit",  "amount": 50.0},
            {"account_id": "A2", "type": "debit",  "amount": 100.0},
        ]
        result = get_account_balances(transactions)
        assert result == [("A2", 400.0), ("A1", 150.0)]

    def test_single_account(self):
        transactions = [
            {"account_id": "ACC", "type": "credit", "amount": 1000.0},
        ]
        result = get_account_balances(transactions)
        assert result == [("ACC", 1000.0)]

    def test_credits_only(self):
        transactions = [
            {"account_id": "X", "type": "credit", "amount": 300.0},
            {"account_id": "Y", "type": "credit", "amount": 100.0},
        ]
        result = get_account_balances(transactions)
        assert result[0][0] == "X"
        assert result[1][0] == "Y"

    def test_zero_balance_after_debits(self):
        transactions = [
            {"account_id": "Z", "type": "credit", "amount": 100.0},
            {"account_id": "Z", "type": "debit",  "amount": 100.0},
        ]
        result = get_account_balances(transactions)
        assert result == [("Z", 0.0)]

    def test_order_by_activity_not_balance(self):
        transactions = [
            {"account_id": "A", "type": "credit", "amount": 1000.0},
            {"account_id": "A", "type": "debit",  "amount": 999.0},
            {"account_id": "B", "type": "credit", "amount": 5.0},
        ]
        # A: balance=1, activity=1999. B: balance=5, activity=5
        result = get_account_balances(transactions)
        assert result[0][0] == "A"
        assert result[1][0] == "B"
