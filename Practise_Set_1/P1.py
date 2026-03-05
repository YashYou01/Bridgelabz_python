ini_bal = int(input("Enter amount: "))
n = int(input("Enter number of transactions: "))

rem_bal = ini_bal

for i in range(n):
    amount = int(input("Enter transaction amount: "))

    if amount <= rem_bal:
        rem_bal = rem_bal - amount
        print("success")
    else:
        print("failed")