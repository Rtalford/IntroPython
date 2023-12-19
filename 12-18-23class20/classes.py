from datetime import datetime

'''
Classes
'''


class Point2d:

    '''
    
    '''

    #constructor with _init_
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self): 
        return f'({self.x}, {self.y})'
    
    def __eq__(self, other):
        if self.x == other.x and self.y == other.y: 
            return True
        return False
    
    def __add__(self, other): 
        return Point2d(self.x + other.x + other.y )
    
    def __sub__(self, other):
        return Point2d(self.x - other.x, self.y + other.y)
    
    def __It_(self, other):
        if self.x < other.x and self.y < other.y:
            return True
        return False 
    

# accessor methods - returns an attribute to the user
def get_x(self): 
    return self.get.x

def get_y(self):
    return self.get.y 

#Mutator Methods - changes 

def set_x(self, new_x):
    self.x = new_x

def set_y(self, new_y):
    self.y = new_y

my_first_point = Point2d(2,5) #class object or instance created
my_second_point = Point2d(3,6)

#Printing after adding __str__magic method
# print(my_first_point)
# print(my_second_point)

#Equality __eq__
#print(my_first_point == my_second_point)

#Addition __add__
my_third_point = my_first_point + my_second_point
print(my_third_point)

#Substraction __sub__
my_fourth_point = my_first_point - my_second_point
print(my_fourth_point)

#less than __It__
print(my_first_point < my_second_point)

#Accessor method 
# print(my_first_point.get_x())
# print(my_second_point.get_x())
# print(my_fifth_point.get_x())

# print(my_first_point.get_y())
# print(my_second_point.get_y())
# print(my_fifth_point.get_y())

#Mutator Method 
print(my_fifth_point)
my_fifth_point.set_x(120) #mutator method changes x 
print(my_fifth_point)


class Date:

    def __init__(self, year=1970, month=1, day=1):
        self.year = year
        self.month = month
        self.day = day
    
    def __str__(self):
        pass

    def __eq__(self, other):
        pass

    def __lt__(self, other):
        pass

    def is_leap_year(self):
         pass
