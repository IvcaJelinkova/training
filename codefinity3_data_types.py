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




