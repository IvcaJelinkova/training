"""
Codefinity:
Recreate list (name as people) with people names and ages into two-dimensional. Note, that two entries are missing (these are Alex and Peter)
Print the second element of the list.
Print age of the fifth person.
"""

# 1) Recreate list in two-dimensional
people = [["Alex", 23], ["Noah", 34], ["Peter", 29], ["John", 41],
["Michelle", 35]]
# Print the second element of the list
print(people[1])
# Print age of the fifth person
print(people[4][1])



# 2) Create two-dimensional tuple
two_d_tuple = (('Alex', 23, 178), ('Noah', 34, 189), ('Peter', 29, 175),
('John', 41, 185), ('Michelle', 35, 165))
# Information about Peter
print(two_d_tuple[2])
# Height of John
print(two_d_tuple[3][2])
# Print converted into list tuple
print(list(two_d_tuple))


# 3) Update your dictionary with people so it will contain information for the next two people, and then print the whole dictionary: 
# Old dictionary
people_d = {'Alex': (23, 178), 'Noah': (34, 189), 'Peter': (29, 175)}
# Add new people to dictionary
people_d['John'] = (41, 185)
people_d['Michelle'] = (35, 165)
# Print the dictionary
print(people_d)


# 4) Iteration over indexes and geting elements by their indexes
# People list
people = ['Alex', (23, 178), 'Noah', (34, 189), 'Peter', (29, 175),
'John', (41, 185), 'Michelle', (35, 165)]

# Construct new for loop
# It will iterate over all indices 
for i in range(len(people)): 
  # Check if our element is tuple
  if type(people[i]) is tuple: 
    print('Age:', people[i][0], "y.o.")
    print('Height:', people[i][1], "cm")
    # Please, do not delete the delimiter below
    print('--------------')
  else:
    print('Name:', people[i])


# 5) Iterate over people_dict keys to output the following information – name, age, height:
# People dictionary
people_dict = {'Alex': (23, 178), 'Noah': (34, 189), 'Peter': (29, 175)}
people_dict["John"] = (41, 185)
people_dict["Michelle"] = (35, 165)

# Construct for loop to print information about people
for i in people_dict.keys():
  print("Name:", i)
  print("Age:", people_dict[i][0])
  print("Height:", people_dict[i][1])
  # Please, do not delete the delimiter below
  print("---------")


# 6) iterate two-dimensional list: In the people list, all the heights are in cm. Convert them to inches (divide by 2.54), round off the result to 2 digits 
# and print message "Name has height of x inches".
# # Data
people = [["Alex", 178], ["Noah", 189], ["Peter", 175], ["John", 185], ["Michelle", 165]]
# Print all the heights in inches with names
for i in range(len(people)):
    if type(people[i]) is list:
     	print(people[i][0], 'has height of', round(people[i][1]/2.54, 2) , 'inches')


# 7) Define a function people_information with one argument d (this will be people_d dictionary!) and name (which will be the name 
# of the person - key in this dictionary), which prints the following output – Name, Age, Height:
# People dictionary
people_d = {'Alex': (23, 178), 'Noah': (34, 189), 'Peter': (29, 175)}
people_d["John"] = (41, 185)
people_d["Michelle"] = (35, 165)

def people_information_mod(d, name):
  if name not in people_d.keys():
    print("There is no information about", name)
  else:
    print("Name:", name)
    print("Age:", people_d[name][0], "y.o.")
    print("Height:", people_d[name][1], "cm")

# Test your function
people_information_mod(people_d, "Alex")
people_information_mod(people_d, "Richard")


# 8) Define a lambda function doing the same as in Chapter 2 (function with three arguments which returns the sum of the first number 
# multiplied by 3, the second multiplied by 2, and the third one and their sum raised to the second power.).
#For example, for numbers 10, 20, 30 the result should be: (10*3 + 20*2 + 30)² = 100² = 10000
# Define a lambda function
fun = lambda a, b, c: (3 * a + 2 * b + c)**2
# Test it
print(fun(1,2,3))
print(fun(3,2,1))





