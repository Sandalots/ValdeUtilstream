from art import *

def stringer():
    stringer = input("Input string to Startstruckt-ify!\n" + ": ")
    return stringer

def printStar():
    return tprint(stringer(), font="random")
    
class Starstruck:
    def __init__(self):
       pass
    def run(self):
        printStar()