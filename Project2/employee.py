from datetime import datetime

class Employee: 

  #constructor(initializer method) with __init__: builds class

  def __init__(self, name = "", job_title = "", department = "", salary = 0, hire_year = 0): 
    self.name = name 
    self.job_title = job_title
    self.department = department
    self.salary = salary
    self.hire_year = hire_year

  #def__str__(self):
    #return f'({self.name}, {self.job_title}, {self.department}, {self.salary}, 
    #{self.hire_year})'

  #def__years_worked__(self, other):
    #return Employee(current_year - self.hire_year)
    
  #def__total_expense__()

  #add Accessor method
    
  #add Mutator method 

  #class instance or creating objects / class objects
    
first_employee = Employee("Florence", "Software Engineer", "Python Developer", 195000, 2023)
second_employee = Employee("Thelma", "Chemist", "Food & Drug Adminstration", 585000, 1990)

  #printing after adding __str__ magic method 
print(first_employee)
print(second_employee)

  #Subtraction __sub__
#years_worked = current_year - hire_year