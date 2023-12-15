# '''
# Assignment 6
# Write a simple function that returns a person's net worth. Here are your requirements:
# Docstring which includes what function does and information on your parameters (brief)
# Function name - net_worth
# parameters - assets, liabilities
# Must contain type hinting for the parameters as well as what the function will be returning
# Call the function in a print statement with needed arguments
# '''

def net_worth (assets, liabilities:int) -> int:
  '''
  function returns a person's net worth; assets subtract liabilities 
  '''
  return assets - liabilities

print(net_worth(500000, 85000))