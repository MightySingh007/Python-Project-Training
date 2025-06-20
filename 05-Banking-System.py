balance = 10000
def deposit(amount):
    global balance
    balance += amount
    print(f"Deposited ₹{amount}. New balance: ₹{balance}")
def withdraw(amount):
    global balance
    if amount <= balance:
        balance -= amount
        print(f"Withdrew ₹{amount}. New balance: ₹{balance}")
    else:
        print("Not Enough balance")
def check_balance():
    print(f"Current balance: ₹{balance}")
while True:
    print("D.Deposit")
    print("W.Withdraw")
    print("C. Check Balance")
    print("E.Exit")
    i = input("Enter your choice")
    if i == 'D':
        amt = int(input("Enter amount to deposit: ₹"))
        deposit(amt)
    elif i == 'W':
        amt = int(input("Enter amount to withdraw: ₹"))
        withdraw(amt)
    elif i == 'C':
        check_balance()
    elif i == 'E':
        print("Thank you for using the Bank App!")
        break
    else:
        print("Invalid")
