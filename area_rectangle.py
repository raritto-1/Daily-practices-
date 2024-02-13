class rectangle:
    def __init__(self,length ,  breadth):
        self.length = length
        self.breadth = breadth
    
    def area(self):
        return self.length * self.breadth
    def para (self):
        return 2 *(self.length+self.breadth)
    
length = int(input('enter the length of rectangel : - '))
breadth = int(input('entr the breadth of rectangle: - '))
area__rectangle = rectangle(length , breadth)
print('Area of rectangle = ',area__rectangle.area())
print('peramiter of the rectangle =',area__rectangle.para())