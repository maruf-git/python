# lambda function
# a lambda function is a small annonymous function
# a lambda function can take any number of arguments but can only have on expression


# syntax:
# lambda arguments: expression
# the expression is executed and the result is returned

addTen = lambda a: a+ 10;
print(addTen(5))


multiply = lambda a,b: a*b;
print(multiply(2,3))

def myfunc(n):
  return lambda a : a * n
mydoubler = myfunc(2)
print(mydoubler(11))

# lambda with buil-in functions
# lambda functions are commonly used with built-in functions like map(), filter() and sorted()

