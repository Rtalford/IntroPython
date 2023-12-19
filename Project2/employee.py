# from datetime import datetime

class Employee: 

  #constructor with __init__

  def __init__(self, name = "", job_title = "", department = "", salary = 0, hire_year = 0): 
    self.name = name 
    self.job_title = job_title
    self.department = department
    self.salary = salary
    self.hire_year = hire_year


  #class instance or object created 
    
  first_employee = ("Florence", "Software Engineer", "Python Developer", 195000, 2023)
  second_employee = ("Thelma", "Chemist", "Food & Drug Adminstration", 585000, 1990)

  print(first_employee)
  print(second_employee)