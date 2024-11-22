class ATM:
    def __init__(self, account_number, pin, balance=0.0):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance

    def check_balance(self):
        """Display the account balance."""
        print(f"Your balance is: ${self.balance:.2f}")

    def deposit(self, amount):
        """Deposit money into the account."""
        if amount > 0:
            self.balance += amount
            print(f"${amount:.2f} has been deposited into your account.")
        else:
            print("Invalid deposit amount.")

    def withdraw(self, amount):
        """Withdraw money from the account."""
        if amount > 0:
            if self.balance >= amount:
                self.balance -= amount
                print(f"${amount:.2f} has been withdrawn from your account.")
            else:
                print("Insufficient funds.")
        else:
            print("Invalid withdrawal amount.")

    def change_pin(self, old_pin, new_pin):
        """Change the ATM PIN."""
        if old_pin == self.pin:
            self.pin = new_pin
            print("Your PIN has been successfully changed.")
        else:
            print("Incorrect old PIN. Try again.")

    def authenticate(self, entered_pin):
        """Authenticate user by checking the PIN."""
        return entered_pin == self.pin


# Function to start the ATM program
def atm_program():
    print("Welcome to the Python ATM")
    account_number = input("Please enter your account number: ")
    pin = input("Enter your PIN: ")

    # Dummy data for testing (in real-world, would be fetched from database)
    atm = ATM(account_number, pin, balance=1000.0)  # Initial balance $1000

    # Authentication loop
    while not atm.authenticate(pin):
        print("Incorrect PIN. Try again.")
        pin = input("Enter your PIN: ")

    print("Authentication successful!")

    # ATM operations loop
    while True:
        print("\nATM Menu:")
        print("1. Check Balance")
        print("2. Deposit Money")
        print("3. Withdraw Money")
        print("4. Change PIN")
        print("5. Exit")

        choice = input("Select an option: ")

        if choice == "1":
            atm.check_balance()
        elif choice == "2":
            amount = float(input("Enter amount to deposit: $"))
            atm.deposit(amount)
        elif choice == "3":
            amount = float(input("Enter amount to withdraw: $"))
            atm.withdraw(amount)
        elif choice == "4":
            old_pin = input("Enter your old PIN: ")
            new_pin = input("Enter your new PIN: ")
            atm.change_pin(old_pin, new_pin)
        elif choice == "5":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    atm_program()
