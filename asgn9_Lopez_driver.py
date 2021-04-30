from asgn9_Lopez_module import *
from random import randrange


def drive(car):
    r = randrange(1,5)
    d = car.showLine() * r
    return f'{car.getColor()}:{d}>'

def main():
    goal = 50
    playerScore = 0
    computerScore = 0
    m1 = Model1()
    print(drive(m1))
    
    
if __name__ == '__main__':
    main()