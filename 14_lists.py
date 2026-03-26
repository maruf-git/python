# list are changeable in python
# The list is changeable, meaning that we can change, add, and remove items in a list after it has been created.

thislist = ["banana", "apple", "litchi"];
print(thislist)

print(len(thislist))

thislist = [1,2,3,4,5];
print(thislist)

print(type(thislist))


# list constructor
newList = list((2,4,6,8,10))
print(newList,type(newList))
print(type((2,4,6,8,10)))


# accessing list
print(newList[1:3]) # 4,6
print(newList[:3]) # 2,4,6


# Check if Item Exists
fruits =  ["banana", "mango", "litchi", "orange"]
if "litchi" in fruits:
    print("Yes 'litchi' is in the fruits list")
    
    
# Change a Range of Item Values
fruits[1:] = ['guava','jackfruit','watermelon']
print(fruits)

# Insert Items
fruits.insert(1,"mango")
print(fruits)

# Append Items
fruits.append("lemon")
print(fruits)


# Extend List
fruits.extend(thislist)
print(fruits)