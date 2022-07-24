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
