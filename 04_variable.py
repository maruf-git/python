# variables
x = 5
y = "maruf"
print(type(x), x)
print(type(y),y)

# type casting
x = str(x)
print(type(x), x)

x = float(x)
print(type(x), x)

# Variable Names
# A variable can have a short name (like x and y) or a more descriptive name (age, carname, total_volume).

# Rules for Python variables:

# A variable name must start with a letter or the underscore character
# A variable name cannot start with a number
# A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# Variable names are case-sensitive (age, Age and AGE are three different variables)
# A variable name cannot be any of the Python keywords.

# Many Values to Multiple Variables
# Python allows you to assign values to multiple variables in one line:

fruit1, fruit2, fruit3 = "orange", "banana", "cherry"
print(fruit1,fruit2,fruit3)

# One Value to Multiple Variables
# And you can assign the same value to multiple variables in one line:

x = y = z = "orange"
print(x,y,z)

# Unpack a Collection
# If you have a collection of values in a list, tuple etc. Python allows you to extract the values into variables. This is called unpacking.

fruits = ["apple", "banana", "cherry"]
# x,y,z = fruits
print(x,y,z)


# output multiple variables
print(x,y,z) #or
print(x +" "+ y +" "+ z)

# The global Keyword
# Normally, when you create a variable inside a function, that variable is local, and can only be used inside that function.

# To create a global variable inside a function, you can use the global keyword.


def myfunc():
    global name
    name = "maruf"
    print("my name is: ",name)
    
myfunc()
print("from global scope accessing name variable, ", name)