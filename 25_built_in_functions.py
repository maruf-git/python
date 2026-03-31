# map
# filter
# sorted
# enumerate -> index + value together



# map -> applies a function on each element
nums = [1,2,3,4]

# map with normal function
def makeDouble(val):
    return val * 2
output = list(map(makeDouble,nums))
print(f"output is: ",output)

# map with lambda function
result = list(map(lambda x: x*2,nums))
print(nums)
print(result)


# filter the even numbers
# way 1 using for loop
print(f"array filter and store in even array");
even = []
for i in range(len(nums)):
    if nums[i]%2==0:
        even.append(nums[i])
print(f"even array is: {even}")

# using filter and lambda function
newEven = list(filter(lambda x: x%2==0,nums));
print(f"new newEven array: {newEven}")

# calculate sum using sum() function
total = sum(nums);
print(f"sum is: {total}")

print(f"max is: {max(nums)}")
print(f"min is: {min(nums)}")

# sorted
print(f"sorted nums array: {sorted(nums)}");
# reverse sorted nums array
print(f"reverse sorted nums array: {sorted(nums,reverse=True)}")

# map() – is used for data transformation

# filter() - is used for condition apply

# zip() - is used for combining multiple lists

nums2 = [2,5,7,9,0,100,5,3]
newList = list(zip(nums,nums2))
print(f"new list after zipping: {newList}")

# enumerate() – Index + value পাওয়া
# used index is need in loop

person ={
    "name":"maruf",
    "roll":25,
    "age":24
}

for key,value in enumerate(person):
    print(key,value)
    
# dir() - used to learn and explore an object
print(f"details of person: {dir(person)}")

# any()
# all()


# real life example

names = ["rifat", "shifat", "maruf"]
scores = [70,85,90]

# print the names of the students how got more than or equal 80 in uppercase

students = list(map(lambda x: x[0].upper(),filter(lambda x: x[1]>=80,zip(names,scores))))
print("Student got 80 or more: ",students);