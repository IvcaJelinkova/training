# codefinity5_loops.py

# 1) for loop
# 2) in range(start, end, step) 
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

# 3) break, continue, pass of loop 
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

# 4) Enumerate():   wanted to access both value and its index number
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

