#codefinity2_functions.py

# 1) f-string: 
# Write your code below
def function():
    capital = 'London'
    print(f'{capital} is the capital and largest city of England and the United Kingdom')


# Testing
function()

# 2) def: saving return to the variable
# Write your code below
def function_adding():  # each of the numbers in parentheses is an argument
  a = 5
  b = 455
  c = 23
  sum = a + b + c
  return sum

# Testing
result = function_adding()  # A parameter is a variable that we specify in parentheses when we define the function.
                            # An argument is a value that we specify in parentheses when calling the function.    
print(result)


# 3) Show the value according to its key in dict, use a function: 
# You have to implement a function called function(), which takes the dictionary as an argument, goes through all the values 
# in the dictionary and displays the pair from the dictionary in which key = Canada
# Write your code below
def function(dict):
    for key, value in dict.items():
        if key == 'Canada':
            print(f'The capital of Canada is {value}')
        
# Testing
function({'France': 'Paris', 'Germany': 'Berlin', 'Canada': 'Ottawa'})


# 4) *args: 
# Write your code below
def multiply_elements(*numbers):
    product = 1
    for number in numbers:
        product = number * product
    print(product)

# Testing
multiply_elements(3, 6, 1, 2)


# 5) **kwargs
#Code a function, named function, that will take in an unknown number of named arguments. This function runs for each argument 
# using the for loop and prints only those longer than 6 characters.
# Write your code below
def function(**variables):
    for x in variables.values():
        if len(x) > 6:
            print(x)

# Testing
function(name="Max", town="London", language="English")


# 6) Outer and inner functions: 
# Write your code below
def outer_function():
    print('The perimeter of this square is equal to:')
    def inner_function(side_of_square):
        # Calculate the perimeter
        perimeter = 4*side_of_square
        print(perimeter)
    inner_function(7)

# Testing
outer_function()
