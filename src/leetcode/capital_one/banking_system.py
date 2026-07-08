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

    Level 2: Scheduled payments
    ============================

    The system now tracks an internal clock, starting at time 0. Time only
    moves forward via advance_time(); no other operation advances it or
    processes payments as a side effect.

    schedule_payment(account_id, amount, delay)
        Schedules a deduction of amount from account_id, to be processed
        once delay time units have elapsed (i.e. when the internal clock
        reaches the current time plus delay).
        Returns the identifier of the payment, formatted as
        "payment<k>", where k starts at 1 and increases by 1 for every
        successfully scheduled payment in the system (ids are never
        reused, even if a payment is later cancelled).
        Returns "" (empty string) if account_id doesn't exist. In this
        case no id is consumed.
        Scheduling a payment does not by itself affect the account's
        balance or activity indicator — only processing it does.

    cancel_payment(account_id, payment_id)
        Cancels a scheduled payment that hasn't been processed yet.
        Returns True if the payment was successfully cancelled.
        Returns False if account_id doesn't exist, if payment_id doesn't
        exist, if payment_id belongs to a different account than
        account_id, or if the payment has already been processed (or
        already failed, or was already cancelled).

    advance_time(units)
        Moves the internal clock forward by units. Every payment whose
        due time is now less than or equal to the current time is
        processed, in any order:
        - If the account's balance is greater than or equal to the
          payment's amount, the amount is deducted from the balance and
          added to the account's activity indicator, and the payment's
          status becomes "PROCESSED".
        - Otherwise (insufficient funds at the time the payment is due),
          the payment's status becomes "FAILED" and neither the balance
          nor the activity indicator is affected.
        A payment with delay 0 is due as soon as advance_time is called
        (even with units=0) and has not yet been processed.

    get_payment_status(account_id, payment_id)
        Returns the current status of a scheduled payment: "PENDING",
        "PROCESSED", "FAILED", or "CANCELLED".
        Returns "" if account_id doesn't exist, if payment_id doesn't
        exist, or if payment_id belongs to a different account.

    Level 3 (bonus): Merging accounts
    ==================================

    merge_accounts(account_id_1, account_id_2)
        Merges account_id_2 into account_id_1.
        - account_id_2's balance is added to account_id_1's balance, and
          account_id_2's activity indicator is added to account_id_1's
          activity indicator.
        - Every pending (not yet processed, failed, or cancelled)
          payment scheduled under account_id_2 is reassigned to
          account_id_1: once due, it deducts from account_id_1's
          balance, and its status from then on must be queried using
          account_id_1's id.
        - account_id_2 is removed from the system entirely: it no
          longer exists for any subsequent operation (create_account
          may be used to create a new, unrelated account with that same
          identifier afterwards).
        Returns True if the merge was successful.
        Returns False if account_id_1 equals account_id_2, or if either
        account doesn't exist.
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

    def schedule_payment(self, account_id: str, amount: int, delay: int) -> str:
        raise NotImplementedError

    def cancel_payment(self, account_id: str, payment_id: str) -> bool:
        raise NotImplementedError

    def advance_time(self, units: int) -> None:
        raise NotImplementedError

    def get_payment_status(self, account_id: str, payment_id: str) -> str:
        raise NotImplementedError

    def merge_accounts(self, account_id_1: str, account_id_2: str) -> bool:
        raise NotImplementedError
