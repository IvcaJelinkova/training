# codefinity5_loops.py

# 1) for loop
# 1.1) in range(start, end, step) 
# Decreasing --> negative step :-)
# Printing numbers from 10 to 0
for i in range(10, -1, -1):
  print(i)
print()

numbers = [2, 3, 4, 8, 11]
counter = 0
for i in reversed(numbers):     # Printing all elements of the reversed list
    counter += i
    print(i)
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
  print(i)
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




