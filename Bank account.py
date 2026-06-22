name = "john"
account_number = "1001"
pin = 101
balance = 0
print("Account created successfully")
print("login")
entered_account = input("Enter account number:")
entered_pin = int(input("Enter pin:"))
if entered_account == account_number and entered_pin == pin:
    print("login completed")
    print("1.Deposit")
    print("2.Withdraw")
    print("3.Check balance")
    choice = int(input("Enter your choice:"))
    if choice == 1:
        amount = float(input("Enter amount to deposit:"))
        balance = balance + amount
        print("Deposit successfully")
        print("Current balance:",balance)
    elif choice == 2:
        amount = float(input("Enter amount to withdraw:"))
        if amount <= balance:
           balance = balance - amount
           print("Withdraw successful")
           print("Current balance:",balance)
        else:
           print("Insufficient balance")
    elif choice == 3:
        print("Current balance:",balance)
    else:
        print("Invalid choice")
else:
    print("Incorrect account number or pin")
