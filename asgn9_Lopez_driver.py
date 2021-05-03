from asgn9_Lopez_module import *
from random import randrange


def drive(car,currentscore):
    r = randrange(1,5)
    new_score = currentscore + r
    d = car.showLine() * new_score
    print(f'{car.getColor()}:{d}({new_score})>')
    return new_score

def main():
    race(50)
    

    
def race(goal):
    print('Let the Race Begin!\n')
    print(f'* * The first car to {goal} wins * *')
    goal = goal
    playerScore = 0
    computerScore = 0
    myCar = Model1()
    print(f'Your car is a Model 1 and the color is {myCar.getColor()}')
    computerCar = Model2()
    print(f"The Computer's car is a Model 2 an the color is {computerCar.getColor()}")
    while True:
        winner = None
        playerScore += drive(myCar,playerScore)
        computerScore += drive(computerCar,computerScore)
        if playerScore >= goal:
            winner = 'You'
            print(f'Winner is {winner}')
            break
        elif computerScore >= goal:
            winner = 'Computer'
            print(f'Winner is {winner}')
            break
        response = input("Drive some more? (y/n): ")
        if response.lower() == 'n':
            break
        else:
            continue
    
    
    
if __name__ == '__main__':
    main()