from classes.mclass import Finance
from classes.rclass import ReadFinances
from classes.sclass import SaveFinances


def main():
    finance = Finance("John", 25, 1000)
    SaveFinances().save(finance)
    print(ReadFinances().getFinance())


if __name__ == "__main__":
    main()
