import random
# there are 3 types of numbers in python
# int
# float
# complex

x = 2
y = 2.5
z = 2j

print(type(x), x)
print(type(y), y)
print(type(z), z)


# Random Number
# Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:

print(random.randrange(1,10))