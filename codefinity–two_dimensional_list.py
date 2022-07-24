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



