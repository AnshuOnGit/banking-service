from typing import List, Dict

from BankingSystem import BankingSystem


class Transaction:
    def __init__(self, timestamp: int, account_id: str, txn_type: str, amount: int = 0):
        self.timestamp = timestamp
        self.account_id = account_id
        self.txn_type = txn_type
        self.amount = amount


class Account:
    def __init__(self, timestamp: int, account_id: str, balance: int = 0):
        self.transactions: List[Transaction] = [Transaction(timestamp, account_id, "open")]
        self.account_id = account_id
        self.balance = balance
        self.spent_amount = 0

    def deposit(self, timestamp: int, account_id: str, amount: int):
        self.transactions.append(Transaction(timestamp, account_id, "credit", amount))
        self.balance = self.balance + amount

    def spend(self, timestamp: int, account_id: str, amount: int):
        self.transactions.append(Transaction(timestamp, account_id, "debit", amount))
        self.balance = self.balance - amount
        self.spent_amount = self.spent_amount + amount


class BankingSystemImpl(BankingSystem):
    def __init__(self):
        self.accounts: List[Account] = []

    def create_account(self, timestamp: int, account_id: str, opening_balance: int = 0) -> bool:
        if opening_balance < 0:
            print(f"opening balance can nt be less than zero")
            return False
        for account in self.accounts:
            if account.account_id == account_id:
                return False
        self.accounts.append(Account(timestamp, account_id, opening_balance))
        return True

    def transfer(self, timestamp: int, source_account_id: str, target_account_id: str, amount: int) -> int | None:
        if source_account_id == target_account_id:
            print(f"source account and target account cannot be same")
            return None
        source_account_exists = False
        source_account: Account = Account(timestamp,"default_account")
        target_account_exists = False
        target_account: Account = Account(timestamp,"default_account")

        for account in self.accounts:
            if account.account_id == source_account_id:
                source_account_exists = True
                source_account = account
            elif account.account_id == target_account_id:
                target_account_exists = True
                target_account = account

        if not source_account_exists and target_account_exists:
            print(f"either source account or target account does not exist")
            return None

        if source_account.balance < amount:
            print(f"either source account or target account does not exist")
            return None

        source_account.spend(timestamp, source_account_id, amount)
        target_account.deposit(timestamp, target_account_id, amount)

        return source_account.balance

    def get_n_top_spenders(self, n: int = 0) -> Dict[str, int]:
        sorted_accounts = sorted(self.accounts, key=lambda x: x.spent_amount, reverse=True)
        top_spenders = {}
        for account in sorted_accounts:
            if account.spent_amount > 0:
                top_spenders[account.account_id] = account.spent_amount
                if 0 < n == len(top_spenders):
                    return top_spenders

        return top_spenders

