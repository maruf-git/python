# Strings
# Strings in python are surrounded by either single quotation marks, or double quotation marks.


# Quotes Inside Quotes
# You can use quotes inside a string, as long as they don't match the quotes surrounding the string:

# Example
print("It's alright")
print("He is called 'Johnny'")
print('He is called "Johnny"')

# multiline string

news = """news about education.
education is free for everyone.
but it is not available to everyone till now.
"""
print(news)

# strings are array;
print(news[0])

# string length
print("news string length is: ", len(news))

# check in strings
# if we want to see if a string has certain substring or character
if("education" in news):
    print("education is present in news")
    
# check if not
if("money" not in news):
    print("money is not presented in news")
