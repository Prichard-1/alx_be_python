class BankAccount:
    """Represents a simple bank account with deposit, withdraw, and balance display functionalities."""

    def __init__(self, initial_balance=0.0):
        """Initialize a new bank account with an optional starting balance."""
        if initial_balance < 0:
            raise ValueError("Initial balance cannot be negative.")
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Deposit a positive amount into the account."""
        if amount <= 0:
            print("Deposit amount must be positive.")
            return False
        self.account_balance += amount
        return True

    def withdraw(self, amount):
        """Withdraw a specified amount if sufficient funds are available."""
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        if amount > self.account_balance:
            print("Insufficient funds.")
            return False
        self.account_balance -= amount
        return True

    def display_balance(self):
        """Display the current account balance."""
        print(f"Current Balance: ${self.account_balance:.2f}")

