class Account:
    def __init__(self, name, account_number, balance=0):
        self.name = name
        self.account_number = account_number
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        if amount <= 0:
            print("❌ Invalid deposit amount")
            return
        self.balance += amount
        self.transactions.append(f"Deposited ₹{amount}")
        print(f"✅ ₹{amount} deposited successfully")

    def withdraw(self, amount):
        if amount <= 0:
            print("❌ Invalid withdrawal amount")
        elif amount > self.balance:
            print("❌ Insufficient balance")
        else:
            self.balance -= amount
            self.transactions.append(f"Withdrawn ₹{amount}")
            print(f"✅ ₹{amount} withdrawn successfully")

    def check_balance(self):
        print(f"💰 Current Balance: ₹{self.balance}")

    def show_transactions(self):
        print("\n📜 Transaction History")
        if not self.transactions:
            print("No transactions yet.")
        else:
            for i, t in enumerate(self.transactions, 1):
                print(f"{i}. {t}")


def bank_app():
    print("🏦 Welcome to Simple Bank App")

    name = input("Enter account holder name: ")
    account_number = int(input("Enter account number: "))

    account = Account(name, account_number)

    while True:
        print("\n========== MENU ==========")
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Check Balance")
        print("4. Transaction History")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == "1":
            amount = float(input("Enter amount to deposit: "))
            account.deposit(amount)

        elif choice == "2":
            amount = float(input("Enter amount to withdraw: "))
            account.withdraw(amount)

        elif choice == "3":
            account.check_balance()

        elif choice == "4":
            account.show_transactions()

        elif choice == "5":
            print("👋 Thank you for using the Bank App")
            break

        else:
            print("❌ Invalid choice. Try again.")


# Run the app
bank_app()
