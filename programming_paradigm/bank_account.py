class BankAccount:
    """A simple bank account class that encapsulates balance and transactions."""

    def __init__(self, initial_balance=0):
        """Initialize the account with an optional starting balance (default: 0)."""
        self.account_balance = initial_balance

    def deposit(self, amount):
        """Add the specified amount to account_balance."""
        if amount > 0:
            self.account_balance += amount
            print(f"Deposited: ${amount:.1f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Deduct the amount from account_balance if sufficient funds exist."""
        if amount > 0 and amount <= self.account_balance:
            self.account_balance -= amount
            print(f"Withdrew: ${amount:.1f}")
            return True  # Successful withdrawal
        elif amount > self.account_balance:
            print("Insufficient funds.")
            return False  # Failed withdrawal
        else:
            print("Withdrawal amount must be positive.")
            return False

    def display_balance(self):
        """Print the current balance in a user-friendly format."""
        print(f"Current Balance: ${self.account_balance:.1f}")

