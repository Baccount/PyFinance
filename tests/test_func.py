import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], ".."))
# trunk-ignore(flake8/E402)
from scr.classes.mclass import Finance
# trunk-ignore(flake8/E402)
from scr.classes.rclass import ReadFinances
# trunk-ignore(flake8/E402)
from scr.classes.sclass import SaveFinances


def test_mclass():
    finance = Finance("John", 20, 100)
    assert finance.name == "John"
    assert finance.age == 20
    assert finance.balance == 100


def test_rclass():
    delDatabase()
    finance = Finance("John", 20, 100)
    SaveFinances().save(finance)
    assert ReadFinances().getFinance()[0] == ("John", 20, 100)


def test_sclass():
    delDatabase()
    finance = Finance("BOB", 50, 200)
    SaveFinances().save(finance)
    assert os.path.exists("data.db")
    assert ReadFinances().getFinance()[0] == ("BOB", 50, 200)



def delDatabase():
    os.remove("data.db")