import math

class area :
    def __init__(self,raidos):
        self.radios = raidos
    
    def area(self):
        return math.pi*raidos**2
    
    def circumference(self):
        return math.pi * 2 *raidos
    
raidos = int(input('enter the radios of give circle:- '))

data_area = area.area(raidos)
data_circumference = area.circumference(raidos)

print(f"Area of the circle: {data_area:.2f}")
print(f"Circumference of the circle: {data_circumference:.2f}")