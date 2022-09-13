from classes.mclass import Finance

def getInput():
    name = input("Enter your name: ")
    age = input("Enter your age: ")
    money = input("Enter your deposit amount: ")
    return Finance(name, age, money)