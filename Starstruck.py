from art import *

def printStar():
    tprint("Starstruck!", font="random")

def testPrint():
    assert printStar() == printStar()

if __name__ == "__main__":
    printStar()
    testPrint()
else:
    pass
