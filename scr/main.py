from classes.mclass import Finance




def main():
    # Create a new instance of Finance
    finance = Finance('John', 25, 1000)
    print(finance.name, finance.age, finance.balance)




if __name__ == "__main__":
    main()