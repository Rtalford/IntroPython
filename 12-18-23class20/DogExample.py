from datetime import datetime

class Dog:

  #Our constructor
  def __init__(self, name, birth_year, breed):
    self.name = name 
    self.birth_year = birth_year
    self.breed = breed 

  #String representation, this is what happens 
  def __str__(self):
    return f'Name: {self.name}\nBirth year: {self.birth_year}\nBreed: {self.breed}'
  
  #This function will calculate the dog's human age
  def human_age(self):
    today = datetime.datetime.now()
    year = today.year
    return year - self.birth_year
  
  def show_results_from_another_function(self):
    return 100 *self.birth_year
    

dog1 = Dog('fluffy', 2020, 'chihuha')
dog2 = Dog('chino', 2015, 'japanese chin')
dog3 = Dog('fido', 2018, 'doberman')

print(dog1)
print(dog2)
print(dog3)

#Human age
print(dog1.human_age()) 


today = datetime.datetime.now()
year = today.year
month = today.month
day = today.day

print(year)
print(month)
print(day)