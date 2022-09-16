#from argm.argms import arguments
from classes.rclass import ReadFinances
from classes.sclass import SaveFinances
from functions.functions import showSplash, clear_screen, purple
from classes.mclass import Finance

def main():
    showSplash()
    usr = loginUsr()
    clear_screen()
    print(purple("Welcome, " + usr.getName() + "!"))
    while True:
        choice = input("1. deposit money\n2. withdraw money\n3. Show balance\n4. exit\n")
        if choice == "1":
            SaveFinances().save(usr.deposit())
        # elif choice == "2":
        #     withdraw(usr)
        elif choice == "3":
            print(ReadFinances().getFinance(usr.getName()))
            input("Press enter to continue...")
            clear_screen()
        elif choice == "4":
            exit()
    showSplash()

    input("Press enter to continue...")





def loginUsr() -> Finance:
    name = input("Enter your name: ")
    usr = Finance(name)
    SaveFinances().save(usr)
    return usr

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Exiting...")
        exit(0)