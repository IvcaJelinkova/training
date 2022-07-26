#codefinity4_data_structures.py

# 1) Insert method of list
# Creating a list
list_1 = ['ABBA', 'Aerosmith', 'The Animals', 'The Kinks']

# Adding new elements
# Write your code below
list_1.insert(0, 'Kraftwerk')
list_1.insert(4, 'New Order')   # before 'The Kinks'

del list_1[0]   #delete the first word
list_1.remove('New Order')      #remove 1 element


# 2) Dictionary: 
capitals = {'India': 'New Delhi', 'Latvia': 'Riga', 'Malta': 'Valletta', 'Netherlands': 'Amsterdam', 'Turkey': 'Ankara'}

# Testing
# Write your code below
print('The value of key Turkey is', capitals['Turkey'])
print('The value of key Malta is',  capitals['Malta'])
capitals['Czech'] = 'Prague'    # add new pair "key-value"
print(capitals) 
del capitals['India']   #delete the pair with key "India"
print('Popped element:', capitals.pop('Turkey'))    # removes and returns an item from the dictionary
capitals.popitem()  # delete the last pair in dict
capitals.clear()    # removes all elements in dict


# 3) Tuple: 

# Creating tuples – fixed data type
tuple_1 = (10, 20, 30, 40, 50)
tuple_2 = (60, 70, 80, 90, 100)
# second element of tuple_1
print(tuple_1[1])
# Concatenation of tuples
tuple_3 = tuple_1 + tuple_2
print(tuple_3)
del tuple_3

# deleting some elements from tuple:
fruits = ('apple', 'apricot', 'banana', 'grape', 'mango', 'peach', 'pineapple')
# Turn the tuple into a list
list_fruits = list(fruits)
print(list_fruits)
# Delete items
list_fruits.remove('banana')
list_fruits.remove('grape')
list_fruits.remove('peach')
list_fruits.append('kiwi')
# Return the list to the tuple
fruits = tuple(list_fruits)
another_tuple = ('orange', 'plum')
# Concatenate tuples
fruits += another_tuple     # concatenate the tuples
# Print the result
print(fruits)


# 4) Set:       Mutable, only unique elements, the order of elements is undefined (pořadí není), different types
# Creating a set which contains strings
set_1 = {'pineapple', 'pear', 'cherry'}
print(set_1)
# Creating a set which contains a mixed type of values 
set_2 = {'pear', 45, None, 'car', 'Joe', 12, 5}
set_2.add(22)       # add an element
print(set_2)
set_1.update([20, 25, 100])     # add more elements
print("lemon" in set_1)     # check if "lemon" is in set
set_2.remove(45)        # remove 5 from set
set_2.discard('Joe')
print(set_2)
set_1.clear()       # delete all the elements from set
print(set_1)






















