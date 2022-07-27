# codefinity5_loops.py

# 1) for loop
# 1.1) in range(start, end, step) 
# Decreasing --> negative step :-)
# Printing numbers from 10 to 0
for i in range(10, -1, -1):
  print(i, end=' ')
print()

numbers = [2, 3, 4, 8, 11]
counter = 0
for i in reversed(numbers):     # Printing all elements of the reversed list
    counter += i
    print(i, end=' ')
print('Count:' + str(counter) + '\n')

# 1.2) break, continue, pass of loop 
# The continue statement skips a block of code in the loop for the current iteration only.

numbers = [2, 3, 8, 5, 8]
# Printing all elements of the list
for i in numbers:
  if i > 5:
        print(i, 'is greater than 5')
  else:
    # Fill the gap
    pass
else:   # the else block, which will be executed when the loop terminates normally.
  print('Done')
print()

# 1.3) Enumerate():   wanted to access both value and its index number
# Count the number of numbers which are multiples of three in the list
numbers = [2, 3, 8, 5, 6, 7]
counter = 0

# Set 'for' loop with 'enumerate()' to work with 'numbers'
for index, value in enumerate(numbers):
  # Set condition *a number need to be multiple of three*
  if value % 3 == 0:
    # Print message
    print('Numbers[', index, '] =', value, 'is multiple of three')
    # Increase the 'counter'
    counter += 1
  else:
    continue
    
# Print the 'counter'
print(counter)



print('_______________________________________________________________')
# 2) while loop: 
# Print numbers from 5 to 0.
i = 5

while i > -1:
  print(i, end=' ')
  # Decrease 'i'
  i -= 1


# 2.1) Print the sum of squares of numbers in the list:
numbers = [1, 2, 4, 5, 7]
counter = 0
i = 0

# Set 'while' loop to work with 'numbers'
while i < len(numbers):
  # Add squares of numbers to the 'counter'
  counter += numbers[i] ** 2
  i += 1

print(counter)
print()


# 2.2) Print numbers from the list. Stop printing, if you meet a negative value: 
numbers = [2, 3, 4, -11, 5]
i = -1

while i < len(numbers)-1: 
  # Increase 'i'
  i += 1
  if numbers[i] < 0:
    # Print a negative element
    print('Negative number was found!: ', numbers[i])
    break       # Finish the loop
  else:
    continue        # Continue searching


# 2.3) Print alphabets only: 
# Here you have a song name. But it is messed with numbers. Remove numbers from these song names
song_name = 'C233om443123eT9439og4343e77t3484h77e566r'
i = -1

# Set 'while' loop to work with 'song_name'
while i < len(song_name)-1:
  # Increase 'i'
  i += 1
  # Check if an element is not alpha
  if not song_name[i].isalpha():
    continue
  else:
    # Print an element
    print(song_name[i], end=' ')


print('\n_______________________________________________________________')
# 3) Nested loops: 
# 3.1) invert triangle: 
# Set outer loop for the number of rows
for i in range(4, 0, -1):
  # Set inner loop for the number of elements in the row
  for j in range(1, i + 1):
    # Print '*'
    print('*', end=' ')
  print('')
print()

# 3.2) MATRIX with for: 
# You need to sum all elements of the matrix.
matrix = [ [1, 2, 4, 29],
           [3, 4, 6, 1] ]

counter = 0
# Set outer loop to work with the number of rows
for i in range(len(matrix)):
  # Inner loop to work with the number of element in the row
  for j in range(len(matrix[i])):
    counter += matrix[i][j]

print(counter)


# MATRIX with while: 
# Add 1 to every element of the matrix.
matrix = [ [1, 2, 4, 29],
           [3, 4, 6, 1],
          [10, -5, 0]]

# Set outer 'while' loop to work with the number of rows
i = 0
while i < len(matrix):
  # Set inner 'while' loop to work with the number of elements in the row
  j = 0
  while j < len(matrix[i]):
    # Change an element
    matrix[i][j] += 1
    # Print an element
    print(matrix[i][j], end = ' ')
    j +=1
  i += 1
  print('')


# Print all letters from the 'text' which are vowels.
text = 'ofsddsfadfjfojnanjinjudfninvjunjee'
vowels = 'aeiou'

# Set 'i'
i = 0
# Set 'while' loop to work with elements of the 'text'
while i < len(text):
  # Set 'for' loop to work with the elements of the 'vowels'
  for j in range(len(vowels)):
    # If an element in the 'text' is one of the elements in 'vowels'
    if text[i] == vowels[j]:
      # Print an element
      print(text[i], end=' ')
  i += 1

print('\n_________')
# my little bit shorter solution: :-) 
for character in text: 
  if character in vowels: 
    print(character, end=' ')
print()



# You need to clean the list given from symbols and numbers. 
matrix = [[' L', '#', 'o', 'o', '#', 's', 'i', 'n', 'g', ' ', '#', 'm', 'y '],
  ['r', 'e', '#', 'l', 'i','#', 'g', 'i', 'o', '#', 'n', '!', 'apspsasd']]

# Set 'for' loop to work with the number of rows 
for i in range(len(matrix)):
  # Set 'for' loop to work with the number of elements of the row
  for j in range(len(matrix[i])):
    # Set condition if an element is '#'
    if matrix[i][j] == '#':
      continue
    # Set condition if an element is '!'
    elif matrix[i][j] == '!':
      break
    else:
      # Print an element
      print(matrix[i][j], end=' ')
print()


# Clasify to vowels, consonants and symbols: 
text = 'aew$^&hg32yy8wer3$#^*@#7ds983hn'
vowels = 'aeiou'

text_vowels = ''
text_consonants = ''
text_symbols = ''

# Set 'i'
i = 0
# Set outer *while* loop to work with 'text'
while i < len(text):
  # Set 'u'
  u = 0
  # Set condition *if an element is a letter*
  if text[i].isalpha():
    # Set inner *while* loop to work with 'vowels'
    while u < len(vowels):
      # Set condition *if a letter from the 'text' is in the vowels'* 
      if text[i] == vowels[u]:
        # Add the letter to the 'text_vowels'
        text_vowels += text[i]
        break
      # Increase 'u'
      u += 1
    else:
      # Add the letter to the 'text_consonants'
      text_consonants += text[i]
  else:
    # Add the letter to the 'text_symbols'
    text_symbols += text[i]
  i += 1
  
print('Vowels from the text: ', text_vowels)
print('Consonants from the text: ', text_consonants)
print('Symbols from the text: ', text_symbols)




