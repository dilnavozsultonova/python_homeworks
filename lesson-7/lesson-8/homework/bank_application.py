import json


class Account:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def __str__(self):
        return f"Account Number: {self.account_number}, Name: {self.name}, Balance: {self.balance}"


class Bank:
    def __init__(self):
        
        self.accounts = {}

    
    def create_account(self, name, initial_deposit):
        account_number = str(len(self.accounts) + 1).zfill(4) 
        if initial_deposit < 0:
            print("Initial deposit cannot be negative.")
            return
        account = Account(account_number, name, initial_deposit)
        self.accounts[account_number] = account
        print(f"Account created successfully! Account Number: {account_number}, Name: {name}, Balance: {initial_deposit}")
        self.save_to_file()  

    
    def view_account(self, account_number):
        if account_number in self.accounts:
            print(self.accounts[account_number])
        else:
            print(f"Account with account number {account_number} not found.")

    
    def deposit(self, account_number, amount):
        if account_number in self.accounts:
            if amount > 0:
                self.accounts[account_number].balance += amount
                print(f"Deposited {amount} to account {account_number}. New Balance: {self.accounts[account_number].balance}")
                self.save_to_file()  
            else:
                print("Deposit amount must be greater than zero.")
        else:
            print(f"Account with account number {account_number} not found.")

  
    def withdraw(self, account_number, amount):
        if account_number in self.accounts:
            if amount > 0 and self.accounts[account_number].balance >= amount:
                self.accounts[account_number].balance -= amount
                print(f"Withdrew {amount} from account {account_number}. New Balance: {self.accounts[account_number].balance}")
                self.save_to_file()  
            elif amount > self.accounts[account_number].balance:
                print("Insufficient funds.")
            else:
                print("Withdrawal amount must be greater than zero.")
        else:
            print(f"Account with account number {account_number} not found.")

   
    def save_to_file(self, filename="accounts.json"):
        try:
           
            accounts_data = {account_number: account.__dict__ for account_number, account in self.accounts.items()}
            with open(filename, 'w') as file:
                json.dump(accounts_data, file, indent=4)
            print("Account data saved successfully.")
        except Exception as e:
            print(f"Error saving data: {e}")

    
    def load_from_file(self, filename="accounts.json"):
        try:
            with open(filename, 'r') as file:
                accounts_data = json.load(file)
                for account_number, account_info in accounts_data.items():
                    account = Account(account_number, account_info['name'], account_info['balance'])
                    self.accounts[account_number] = account
            print("Account data loaded successfully.")
        except FileNotFoundError:
            print("No previous account data found. Starting with an empty set of accounts.")
        except Exception as e:
            print(f"Error loading data: {e}")


def main():
    bank = Bank()
    bank.load_from_file() 

    while True:
        print("\n1. Create Account")
        print("2. View Account")
        print("3. Deposit Money")
        print("4. Withdraw Money")
        print("5. Save to File")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter the account holder's name: ")
            initial_deposit = float(input("Enter the initial deposit amount: "))
            bank.create_account(name, initial_deposit)

        elif choice == "2":
            account_number = input("Enter the account number: ")
            bank.view_account(account_number)

        elif choice == "3":
            account_number = input("Enter the account number: ")
            amount = float(input("Enter the deposit amount: "))
            bank.deposit(account_number, amount)

        elif choice == "4":
            account_number = input("Enter the account number: ")
            amount = float(input("Enter the withdrawal amount: "))
            bank.withdraw(account_number, amount)

        elif choice == "5":
            bank.save_to_file()

        elif choice == "6":
            print("Exiting program...")
            break

        else:
            print("Invalid choice, please try again.")


if __name__ == "__main__":
    main()
