def get_account_balances(transactions: list[dict]) -> list[tuple[str, float]]:
    """Given a list of banking transactions, compute each account's final balance
    and return accounts sorted in descending order by total monetary activity.

    Each transaction is a dict with:
        - "account_id" (str): identifier of the account
        - "type" (str): either "credit" or "debit"
        - "amount" (float): a positive value

    Total monetary activity for an account is the sum of the absolute values of all
    its transactions (credits + debits), regardless of direction.

    Example:
        Input: transactions = [
            {"account_id": "A1", "type": "credit", "amount": 200.0},
            {"account_id": "A2", "type": "credit", "amount": 500.0},
            {"account_id": "A1", "type": "debit",  "amount": 50.0},
            {"account_id": "A2", "type": "debit",  "amount": 100.0},
        ]
        Output: [("A2", 400.0), ("A1", 150.0)]
        Explanation:
            A1 balance = 200 - 50 = 150, activity = 250
            A2 balance = 500 - 100 = 400, activity = 600
            Sorted by activity descending: A2 first, then A1.

    Constraints:
        - 1 <= len(transactions) <= 10^5
        - amount > 0
        - type is always "credit" or "debit"
        - account_id is a non-empty string

    :param transactions: list of transaction dicts
    :return: list of (account_id, balance) tuples sorted by total activity descending
    """
    pass
