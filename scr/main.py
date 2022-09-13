from classes.mclass import Finance
from classes.rclass import ReadFinances
from classes.sclass import SaveFinances
from argm.argms import arguments


def main():
    arg = arguments()
    finance = Finance(arg.name, arg.age, arg.money)
    SaveFinances().save(finance)
    print(ReadFinances().getFinance())


if __name__ == "__main__":
    main()
