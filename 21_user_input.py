# name = input("Input your name: ")
# print(f"Welcome {name}")

# age = int(input("Enter your age: "))
# print(f"Your age is: {age}")
# print(f"type of age is: {type(age)}")


# validate input

mark = input("Enter your mark: ")

try:
    mark = int(mark)
    # add extra five as bonous
    mark += 5
    print(f"Your final mark with bonous is: {mark}")
except:
    print("Invalid Input")