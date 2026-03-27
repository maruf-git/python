# Python None
# None is a special constant in Python that represents the absence of a value.

value = None
print(f"type of value is {type(value)} and value is: ",value)

# comaring to none
result = None
if result == None:
    print("No result yet")
else:
    print("Result is ready")
    
result = 5
if result!= None:
    print(f"Result is not none and it is:  {result}")
else:
    print(f"Result is none")
    
# True or False
# None evaluates to False in a boolean context.
print(bool(None))

# Functions returning None
# Functions that do not explicitly return a value return None by default.

def myFunc():
    x = 5;
    
x = myFunc()
print(x, type(x))
