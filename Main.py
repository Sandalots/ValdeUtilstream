import Starstruck
import rStr
class Main:
    def __init__(self):
        self.starstruck = Starstruck.Starstruck()

    def run(self):
        self.starstruck.run()
    
    def randomise(self):
        self.starstruck.stringer = rStr.randomString()
        self.starstruck.run()

if __name__ == "__main__":
    main = Main()
    main.run()
    main.randomise()