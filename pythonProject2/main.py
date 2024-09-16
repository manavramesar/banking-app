# Banking App

def show_balance(balance, invest):
    print(f"Your balance is ${balance:.2f} and you have ${invest:.2f} invested")

def deposit():
    amount = float(input("Enter an amount to deposit: "))
    if amount < 0:
        print("That is not a valid amount")
        return 0
    else:
        return amount

def withdraw(balance):
    amount = float(input("How much would you like to withdraw? "))
    if amount > balance:
        print("Insufficient funds")
        return 0
    elif amount < 0:
        print("Amount must be greater than 0")
        return 0
    else:
        return amount

def invest(balance):
    amount = float(input("Enter an amount to invest: "))
    if amount > balance:
        print("Insufficient funds")
        return 0
    elif amount < 0:
        print("Amount must be greater than 0")
        return 0
    else:
        return amount

def main():
    balance = 0  # Starting balance
    invest_balance = 0  # Starting investment balance
    is_running = True

    while is_running:
        print("Welcome To Banking App")
        print("1. Show Balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Invest")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            # Display both balance and invest amount
            show_balance(balance, invest_balance)
        elif choice == '2':
            balance += deposit()  # Add deposit to balance
        elif choice == '3':
            balance -= withdraw(balance)  # Subtract withdrawal from balance
        elif choice == '4':
            # Invest amount
            invest_amount = invest(balance)
            balance -= invest_amount  # Deduct invested amount from balance
            invest_balance += invest_amount  # Add to invest balance
        elif choice == '5':
            is_running = False
            print("Thank you for using the Banking App. Goodbye!")
        else:
            print("Invalid Selection, please try again.")

if __name__ == '__main__':
    main()
