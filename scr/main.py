from classes.mclass import Finance

from classes.sclass import SaveFinances 


def main():
    # Create a new instance of Finance
    finance = Finance('John', 25, 1000)
    SaveFinances().save(finance)




if __name__ == "__main__":
    main()