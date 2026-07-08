import dataclasses


@dataclasses.dataclass
class Account:
    account_id: str
    balance: int = 0
    activity: int = 0


class BankingSystem:
    """Implement a simplified banking system that supports account creation,
    deposits, transfers between accounts, and a query for the most
    financially active accounts.

    Initially the system contains no accounts.

    Operations:

    create_account(account_id)
        Creates a new account with the given identifier if it doesn't
        already exist.
        Returns True if the account was successfully created.
        Returns False if an account with account_id already exists.

    deposit(account_id, amount)
        Deposits the given amount of money into the specified account.
        Returns the total amount of money in the account after the
        deposit has been processed.
        If the specified account doesn't exist, returns -1.

    transfer(from_id, to_id, amount)
        Transfers the given amount of money from the account with
        from_id to the account with to_id.
        Returns the balance of from_id if the transfer was successful.
        Returns -1 if from_id or to_id doesn't exist.
        Returns -1 if from_id and to_id are the same.
        Returns -1 if the funds in from_id are insufficient to perform
        the transfer.

    top_activity(n)
        Returns the identifiers of the n most active accounts in
        descending order of their financial activity indicator. In case
        of a tie, accounts are sorted alphabetically by account_id in
        ascending order.

        The financial activity indicator of an account is the sum of all
        transactions for that account, including money deposited and/or
        successfully transferred (both money sent and money received).
        Unsuccessful transactions are not included.

        Each identifier in the returned list is formatted as
        "<account_id>(<activity_indicator>)".

        If fewer than n accounts exist in the system, all of them are
        returned (in the described format).

    Example:
        system = BankingSystem()
        system.create_account("account1")          # True
        system.create_account("account1")          # False
        system.create_account("account2")          # True
        system.deposit("non-existing", 2700)       # -1
        system.deposit("account1", 2700)           # 2700
        system.transfer("account1", "account2", 2701)  # -1
        system.transfer("account1", "account2", 200)   # 2500
        system.transfer("account1", "account2", 2500)  # 0
        system.deposit("account2", 300)            # 3000
        system.create_account("account3")          # True
        system.deposit("account3", 4000)           # 4000
        system.top_activity(3)
        # ["account1(5400)", "account3(4000)", "account2(3000)"]
        system.deposit("account2", 1000)           # 4000
        system.top_activity(2)
        # ["account1(5400)", "account2(4000)"]
        system.top_activity(5)
        # ["account1(5400)", "account2(4000)", "account3(4000)"]
    """

    def __init__(self) -> None:
        self._accounts: dict[str, Account] = {}

    def create_account(self, account_id: str) -> bool:
        if self._accounts.get(account_id) is None:
            self._accounts[account_id] = Account(account_id)
            return True
        return False

    def deposit(self, account_id: str, amount: int) -> int:
        account = self._accounts.get(account_id)
        if account is None:
            return -1

        account.balance += amount
        account.activity += amount
        return account.balance

    def transfer(self, from_id: str, to_id: str, amount: int) -> int:
        if from_id == to_id:
            return -1

        from_account = self._accounts.get(from_id)
        if from_account is None:
            return -1

        if from_account.balance < amount:
            return -1

        to_account = self._accounts.get(to_id)
        if to_account is None:
            return -1

        to_account.balance += amount
        from_account.balance -= amount

        to_account.activity += amount
        from_account.activity += amount

        return from_account.balance

    def top_activity(self, n: int) -> list[str]:
        sorted_accounts = sorted(
            self._accounts.values(), key=lambda acc: (-acc.activity, acc.account_id)
        )
        return [f"{acc.account_id}({acc.activity})" for acc in sorted_accounts[:n]]
