from datetime import datetime

class Employee: 

  #constructor(initializer method) with __init__: builds class

  def __init__(self, name = "", job_title = "", department = "", salary = 0, hire_year = 0): 
    self.name = name 
    self.job_title = job_title
    self.department = department
    self.salary = salary
    self.hire_year = hire_year

  def__str__(self):
    return f'({self.name}, {self.job_title}, {self.department}, {self.salary}, 
    {self.hire_year})'
   
  #? Do we need to use the other build-in class methods; __eq__, __add__,

  #def__years_worked__(self, other):   #__sub__ ?
    #return Employee(current_year - self.hire_year)
    
  #def__total_expense__()
    

  #Accessor method : returns an attribute to the user/ access attributes 
    
  def get_name(self): 
    return self.name

  def get_job_title(self): 
    return self.job_title

  def get_department(self): 
    return self.department 

  def get_salary(self): 
    return self.salary

  def get_hire_year(self): 
    return self.hire_year 
  
    
  #Mutator method : lets the user change the attribute
    
  def set_name(self, new_name):
    self.name = new_name

  def set_job_title(self, new_job_title):
    self.job_title = new_job_title

  def set_department(self, new_department):
    self.department = new_department

  def set_salary(self, new_salary):
    self.salary = new_salary

  def set_hire_year(self, new_hire_year):
    self.hire_year = new_hire_year
    

  #class instance or creating objects / class objects
    
first_employee = Employee("Florence", "Software Engineer", "Python Developer", 195000, 2023)
second_employee = Employee("Thelma", "Chemist", "Food & Drug Adminstration", 585000, 1990)

  #printing after adding __str__ magic method 
print(first_employee)
print(second_employee)

  #Subtraction __sub__ ? not sure how to write the code below. should be different from the __sub__ code above. 
#years_worked_employee_1 = current_year - hire_year
#print(years_worked)

  #Subtraction __sub__
#total_expense

  #Accessor method 

#print(first_employee.get_name())
#print(first_employee.get_job_title())
#print(first_employee.get_department())
#print(first_employee.get_salary())
#print(first_employee.get_hire_year())

#print(second_employee.get_name())
#print(second_employee.get_job_title())
#print(second_employee.get_department())
#print(second_employee.get_salary())
#print(second_employee.get_hire_year())

  #Mutator Method 

#print(first_employee)
#first_employee.set_name(insert value?) #mutator method changes name
#print(first_employee)

#print(first_employee)
#first_employee.set_job_title()
#print(first_employee)

#print(first_employee)
#first_employee.set_department()
#print(first_employee)

#print(first_employee)
#first_employee.set_salary()
#print(first_employee)

#print(first_employee)
#first_employee.set_hire_year()
#print(first_employee)

#print(second_employee)
#second_employee.set_name()
#print(second_employee)

#print(second_employee)
#second_employee.set_job_title()
#print(second_employee)

#print(second_employee)
#second_employee.set_department()
#print(second_employee)

#print(second_employee)
#second_employee.set_salary()
#print(second_employee)

#print(second_employee)
#second_employee.set_hire_year()
#print(second_employee)