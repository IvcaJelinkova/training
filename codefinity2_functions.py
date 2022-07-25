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



# 7) recursion: 
#You have to implement a function, named sum_of_numbers, which calculates the sum of natural numbers from 1 to n. For example:
# if number = 5, you will get such a result 5 + 4 + 3 + 2 + 1 = 15
# To check, take number = 7
# Write your code below
def sum_of_numbers(number):
    if number == 1:
        return 1
    else:
        return number + sum_of_numbers(number - 1) 

# Testing 
result = sum_of_numbers(7)
print(result)


# 8) sum of numbers in list: 
# You need to implement a function, named sum_of_elements, that calculates the sum of the items from a list.
# Write your code below
def sum_of_elements(list):
    if len(list) == 1:
        return list[0]
    else:
        return sum_of_elements(list[:-1]) + list[-1]

# Testing 
result = sum_of_elements([54, 3, 21, 67, 43, 1])
print(result)



