class MoneyNotEnoughError(Exception):
    pass


class PINCodeError(Exception):
    pass


class UnderageTransactionError(Exception):
    pass


class MoneyIsNegativeError(Exception):
    pass


MIN_AGE = 18


pin, balance, age = [int(x) for x in input().split(", ")]

while True:
    line = input().split("#")
    command = line[0]

    if command == "End":
        break

    money = int(line[1])

    if command == "Send Money":
        transaction_pin = int(line[2])

        if money > balance:
            raise MoneyNotEnoughError("Insufficient funds for the requested transaction")

        if transaction_pin != pin:
            raise PINCodeError("Invalid PIN code")

        if age < MIN_AGE:
            raise UnderageTransactionError("You must be 18 years or older to perform online transactions")

        balance -= money
        print(f"Successfully sent {money:.2f} money to a friend")
        print(f"There is {balance:.2f} money left in the bank account")

    elif command == "Receive Money":
        if money < 0:
            raise MoneyIsNegativeError("The amount of money cannot be a negative number")

        salary = money * 0.5
        balance += salary
        print(f"{salary:.2f} money went straight into the bank account")
