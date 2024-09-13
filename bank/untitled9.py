#BANK#

print("Welcome to our bank")
balance = int(input("Enter your balance: "))

while True:

    print("Please select a transaction")
    transaction = int(input("Choose the transaction you want to perform: \n 1-Withdraw money \n 2-Deposit money \n 3-Check balance \n 4-Exit"))

    if transaction == 1:
        print("Your current balance: ", balance)
        amount = int(input("Enter the amount you want to withdraw: "))
        if balance < amount:
            print("You don't have enough balance.")
        else:
            new_balance = balance - amount
            print("Your new balance: ", new_balance)
        balance = new_balance
    elif transaction == 2:
        print("Your current balance: ", balance)
        amount = int(input("Enter the amount you want to deposit: "))
        new_balance = balance + amount
        print("Your new balance: ", new_balance)
        balance = new_balance

    elif transaction == 3:
        print("Your current balance: ", balance)

    elif transaction == 4:
        print("Thank you for choosing us, have a nice day")
        break

    else:
        print("Invalid input")
