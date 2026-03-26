# The built-in range() function returns an immutable sequence of numbers, commonly used for looping a specific number of times.
# This set of numbers has its own data type called range.

print("type of range is: ",type(range));
print("type of range(5) is: ", type(range(5)))
print("value of range(5) is: ", range(5))
val = range(5)
print(f"val is: {val}, type of val is: {type(val)}")

# Using List to Display Ranges
print("what val has:")
for i in val:
    print(i)
print(range(5,10,2))


# Slicing Ranges
# Like other sequences, ranges can be sliced to extract a subsequence.


# Membership Testing
# Ranges support membership testing with the in operator.


# Length
# Ranges support the len() function to get the number of elements in the range.