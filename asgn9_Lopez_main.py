from asgn9_Lopez_module import *
import random

def main():
    m2 = Model2()    
    print( f'Your car is a Model_2 and the color is {m2.getColor()}')
    print('\n' + m2.soundHorn())
    m1 = Model1()
    print(f'my car is a Model_1 and the color is {m1.getColor()}')
    print('\n' + m1.soundHorn())
    print(random.randrange(1,5))
    
if __name__ == '__main__':
    main()