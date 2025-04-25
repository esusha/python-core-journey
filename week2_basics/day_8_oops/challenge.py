class BankAccount:
    """ 
    A simple bank account class to manage deposits and withdrawals.
    """
    def __init__(self, owner: str, balance: float = 0.0):
        self.owner = owner
        self.balance = balance
        
    def deposit(self, amount: float):
        """
        Deposit a specified amount into the bank account.
        :param amount: Amount to deposit
        """
         # Check if the amount is positive
         # If it is, add it to the balance
         # If not, print an error message
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount}. New balance is {self.balance}.")
        else:
            print("Deposit amount must be positive.")
    def withdraw(self, amount: float):
        """
        Withdraw a specified amount from the bank account.  
        :param amount: Amount to withdraw
        """
         # Check if the amount is positive and less than or equal to the balance
         # If it is, subtract it from the balance
         # If not, print an error message
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew {amount}. New balance is {self.balance}.")
        else:
            print("Withdrawal amount must be positive and less than or equal to the balance.")
    def get_balance(self):
        """
        Get the current balance of the bank account.
        :return: Current balance
        """
         # Return the current balance
         # This method is used to check the balance without modifying it
        return self.balance