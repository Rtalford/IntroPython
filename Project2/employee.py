from datetime import datetime

class Employee: 

  #constructor with __init__

  def __init__(self, name = "", job_title = "", department = "", salary = 0, hire_year = 0): 
    self.name = name 
    self.job_title = job_title
    self.department = department
    self.salary = salary
    self.hire_year = hire_year


  
  my_first_employee = ("Florence", "Software Engineer", "Python Developer", 195,000, 2023)