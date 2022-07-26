# codefinity3_data_types.py

# 1) Format method
Earth_to_Moon = 238855
Sun_to_Venus = 67000000
# Present in scientific notation including 4 digits after the decimal point
Earth_to_Moon_e = "{:.4e}".format(Earth_to_Moon)
# Present in scientific notation including 2 digits after the decimal point
Sun_to_Venus_e = '{:.2e}'.format(Sun_to_Venus)

print("The regular distance between the Eart and the Moon is:", Earth_to_Moon)
print("The distance between the Eart and the Moon in scientific notation is:", Earth_to_Moon_e)
print("The regular distance between the Venus and the Sun is:", Sun_to_Venus)
print("The distance between the Venus and the Sun in scientific notation is:", Sun_to_Venus_e)


# 2) Scientific notation:
# Define the mass on Earth m1 = 5.972 * 10^24 using scientific notation.
m1 = 5.972e24

# 2) Complex numbers: 
number1 = 167 - 98j
number2 = 67 + 9j
number3 = 186282

# Print the real part of the number1 variable
print("The real part of the number1 =", number1.real)
# Print the imaginary part of the number2 variable
print("The imaginary part of the number2 =", number2.imag)
# Print the number 3 variable in a complex form
print("The speed of light =", number3.real + number3.imag * 1j)



# 3) Boolean, not X: 
# This statement equals False
statement1 = not True or False
# This statement equals True
statement2 = True and not False

# Print the first statement
print(statement1)
# Print the second statement
print(statement2)


# 4) 
# Make these statements equal True
statement1 = True or (True and False)       # wrote the first True
statement2 = (False and (True and True)) or True    # wrote the last True
statement3 = ((False or False) or True) and True    # wrote the last True

# Print the first statement
print(statement1)
# Print the second statement
print(statement2)
# Print the third statement
print(statement3)


# 5) step in slicing, methods find and index, slicing the word
string = "Life is like riding a bicycle. To keep your balance, you must keep moving"
sliced_string = string[1:11:4]
print(sliced_string)    # print "iii" – it takes the first and other fourth symbol
print('The last symbol:', string[len(string)-1])
print(string.find('L'))     # find the index of the letter
print(string.index('is'))   # find the index of the word (otherwise throws an exeptation)
print(string[string.index('riding'):string.index('riding')+6])   # print word "riding"
new_string1 = string.replace('bicycle','horse')     # replace the word "bicycle" to "horse"
print(new_string1)


# 6) Boolean: 
# This statement equals True
True_statement1 = bool(-90)
# This statement equals True
True_statement2 = bool("La vie est belle")

# This statement equals False
False_statement1 = bool(0j)
# This statement equals False
False_statement2 = bool(None)

print(True_statement1,True_statement2)
print(False_statement1,False_statement2)

# Make this statement equals False
print('C'>'D')  # it compares words by the first letters that different 

# Make this statement equals False
print("Codefinity"<"Art")

# Make this statement equals True
print("Programming">"Data")
