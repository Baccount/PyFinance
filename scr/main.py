#from argm.argms import arguments
from classes.rclass import ReadFinances
from classes.sclass import SaveFinances
from functions.functions import showSplash, clear_screen, purple
from classes.mclass import Finance

def main():
    showSplash()
    usr = loginUsr()
    name = usr.name
    clear_screen()
    print(purple("Welcome, " + name + " you have "))
    print(purple(str(ReadFinances().getFinance(name)[0][1]) + " $ in your account"))
    while True:
        choice = input("1. Deposit money\n2. Withdraw money\n3. Show balance\n4. Exit\n")
        if choice == "1":
            clear_screen()
            amount = int(input("Enter the amount you want to deposit: "))
            SaveFinances().save(usr, amount)
        elif choice == "2":
            # withdraw money
            clear_screen()
            amount = int(input("Enter the amount you want to withdraw: "))
            blance = ReadFinances().getFinance(name)[0][1] - amount
            print(blance)
            SaveFinances().save(usr, -blance)
        elif choice == "3":
            print(ReadFinances().getFinance(name))
            input("Press enter to continue...")
            clear_screen()
        elif choice == "4":
            exit()
    showSplash()

    input("Press enter to continue...")





def loginUsr() -> Finance:
    name = input("Enter your name: ")
    usr = Finance(name)
    return usr

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Exiting...")
        exit(0)