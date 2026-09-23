"""Bank account system with abstract base class."""

from abc import ABC, abstractmethod


class BankAccount(ABC):
    """Abstract bank account interface."""

    @abstractmethod
    def create_account(self, account_number: str, account_type: str):
        """Create a new bank account."""
        pass

    @abstractmethod
    def deposit(self, account_number: str, amount: float) -> bool:
        """Deposit the amount into the account."""
        pass

    @abstractmethod
    def withdraw(self, account_number: str, amount: float) -> bool:
        """Withdraw the amount from the account."""
        pass

    @abstractmethod
    def get_balance(self, account_number: str) -> float:
        """Return current balance."""
        pass

    @abstractmethod
    def get_transaction_history(self, account_number: str) -> list:
        """Return list of transactions."""
        pass

    @abstractmethod
    def apply_interest(self):
        """Apply interest to applicable accounts."""
        pass


class BankAccountImpl(BankAccount):
    """Concrete bank account implementation."""

    INTEREST_MULTIPLIER = 1.05

    def __init__(self):
        self._accounts = {}

    def create_account(self, account_number: str, account_type: str):
        if account_number not in self._accounts:
            self._accounts[account_number] = {
                'account_type': account_type,
                'balance': 0,
                'history': [],
            }

    def deposit(self, account_number: str, amount: float) -> bool:
        if account_number not in self._accounts:
            return False
        if not isinstance(amount, (int, float)) or amount <= 0:
            return False

        self._accounts[account_number]['balance'] += amount
        self._accounts[account_number]['history'].append({
            'type': 'deposit',
            'amount': amount,
        })
        return True

    def withdraw(self, account_number: str, amount: float) -> bool:
        if account_number not in self._accounts:
            return False
        if not isinstance(amount, (int, float)) or amount <= 0:
            return False
        if self._accounts[account_number]['balance'] < amount:
            return False

        self._accounts[account_number]['balance'] -= amount
        self._accounts[account_number]['history'].append({
            'type': 'withdraw',
            'amount': amount,
        })
        return True

    def get_balance(self, account_number: str) -> float:
        if account_number in self._accounts:
            return self._accounts[account_number]['balance']
        return 0.0

    def get_transaction_history(self, account_number: str) -> list:
        if account_number in self._accounts:
            return self._accounts[account_number]['history']
        return []

    def apply_interest(self):
        for account in self._accounts.values():
            if account['account_type'] == 'savings':
                account['balance'] *= self.INTEREST_MULTIPLIER