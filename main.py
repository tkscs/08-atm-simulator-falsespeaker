"""
Options:
- check the balance: prints current balance
- withdraw money:
    ask you how much to withdraw
    reduce the balance by that amount
    if you try to withdraw more than you have...
        print error don't update the balance
    don't withdraw a negative amount
- deposit money:
    ask you how to deposit
    increase the balance by that amount
    don't deposit a negative amount
- loop (with a while loop) until the user says "exit"
"""

# start with 1 million dollars
balance = 1000000

while True:
    current_input = input("Type balance (b), withdraw (w), deposit (d), or exit (e): ")

    if current_input == "e":
        print("Goodbye")
        

    if current_input == "b":
        print("Balance:", balance)

    elif current_input == "w":
        amount = float(input("Amount to withdraw: "))

        if amount < 0:
            print("Cannot withdraw a negative amount")
        elif amount > balance:
            print("Not enough money")
        else:
            balance -= amount
            print("New balance:", balance)

    elif current_input == "d":
        amount = float(input("Amount to deposit: "))

        if amount < 0:
            print("Cannot deposit a negative amount")
        else:
            balance += amount
            print("New balance:", balance)

    else:
        print("Invalid option")