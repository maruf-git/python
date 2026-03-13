greet = "hello world"

# uppercase
print(greet.upper())

# lowercase
print(greet.lower())

# remove white space from start or end of a string
greet = " Hello, World! "
print(greet.strip())
print(greet) # python strings are immutable

# replace
print(greet.replace('H','J'))

# split string
print(greet.split(',')) # gives a list


# *****************************************************
# formatting strings
# F-Strings
# F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.

# To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.

age = 36
text = f"my age is {age}"
print(text)

price = 59
txt = f"The price is {price:.2f} dollars"
print(txt)

# text center
name = "maruf"
print(name.center(20))
print(name.center(20,"*"))