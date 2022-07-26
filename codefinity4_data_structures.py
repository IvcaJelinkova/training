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














