class BankSystem:
    """A simple bank system supporting account creation, fund transfers, and activity reporting.

    Each account tracks its balance and total monetary activity (sum of all debit and credit amounts).
    """

    def create_account(self, account_id: str) -> bool:
        """Create a new account with a zero balance.

        Returns False if an account with the given ID already exists, True otherwise.

        Example:
            bank = BankSystem()
            bank.create_account("ACC1")  # True
            bank.create_account("ACC1")  # False — already exists

        :param account_id: unique identifier for the new account
        :return: True if the account was created, False if it already existed
        """
        pass

    def transfer(self, from_id: str, to_id: str, amount: float) -> bool:
        """Transfer funds from one account to another.

        Returns False if:
            - Either account does not exist
            - The source account has insufficient funds
            - from_id == to_id

        On success, debits from_id and credits to_id by the given amount, and
        records the activity on both accounts.

        Example:
            bank = BankSystem()
            bank.create_account("A")
            bank.create_account("B")
            bank.transfer("A", "B", 100.0)  # False — A has no funds
            bank.transfer("A", "C", 50.0)   # False — C does not exist

        :param from_id: account to debit
        :param to_id: account to credit
        :param amount: positive amount to transfer
        :return: True if the transfer succeeded, False otherwise
        """
        pass

    def get_top_activity(self, n: int) -> list[str]:
        """Return the IDs of the top n accounts ranked by total monetary activity (descending).

        Total monetary activity is the cumulative sum of all amounts debited and credited
        to the account. Ties are broken alphabetically by account_id (ascending).

        Example:
            bank = BankSystem()
            bank.create_account("A")
            bank.create_account("B")
            bank.create_account("C")
            # ... after several transfers ...
            bank.get_top_activity(2)  # e.g. ["B", "A"]

        :param n: number of top accounts to return
        :return: list of account IDs sorted by total activity descending
        """
        pass
