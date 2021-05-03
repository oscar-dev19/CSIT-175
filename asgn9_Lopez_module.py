class Car:
    color = ''
    horn_style = 'beep beep'
    distance = 2
    line= '-'
    
    def soundHorn(self) -> str:
        return self.horn_style

    def getColor(self) -> str:
        return self.color

    def showLine(self) -> int:
        return self.line

class Model1(Car):
    def __init__(self):
        self.color = 'Blue'
    
    def getColor(self) -> str:
        return self.color
    def __str__(self):
        return f'Model_1:\n {self.color}\n  {self.horn_style}\n'
    
    
class Model2(Car):
    def __init__(self):
        self.color = 'Red'
        self.horn_style = 'honk honk'
    
    def getColor(self) -> str:
        return self.color
    
    def __str__(self):
        return f'Model_2:\n +{self.color}\n + {self.horn_style}\n'