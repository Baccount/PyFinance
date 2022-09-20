# from argm.argms import arguments
from classes.mclass import Finance
from functions.functions import showSplash


def main():
    while True:
        # arg = arguments()
        # finance = Finance(arg.name, arg.money) if arg.name and arg.money else None
        # if not finance:
        showSplash()
        name = input("Enter your name: ")
        finance = Finance(name)
        choice = input("1: Deposit\n2: Withdraw\n3: Balance\n: ")
        if choice == "1":
            amount = int(input("Amount: "))
            finance.deposit(amount)
            finance.saveFinance()
        elif choice == "2":
            amount = int(input("Amount: "))
            finance.withdraw(amount)
            finance.saveFinance()
        elif choice == "3":
            print(f"Balance: {finance.getBalance()}")
        input("Press enter to continue...")

def askUsr():
    usr = input("Do you want to continue? (y/n): ")
    return usr


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Exiting...")
        exit(0)
