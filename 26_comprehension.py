# comprehesion meaning
# loop the data
# transform the data (like map)
# filter the data if needed (like filter)


# syntax
# [expression for item in iterable condition]

# list comprehesion is used most
nums = [1,2,3,4]
result = [x*2 for x in nums]
print(f"after list comprehension result: {result}")

# dictionary comprehesion
resultDict = {x:x*2 for x in nums}
print(f"resultDict: {resultDict}")

# set comprehesion
nums = [1,2,2,3]
resultSet = {x for x in nums}
print(f"resultset: {resultSet}")


# nested comprehesion
# এটা internally এমন:
# প্রথমে কিছু calculate করে না ❌
# শুধু “formula” store করে ✔
nums = [1, 2, 3]
gen = (x * 2 for x in nums)
print(type(gen))
print(list(gen))  # [2,4,6]
print(list(gen))  # []

# 👉 দ্বিতীয়বার empty 😲
# 🧠 কেন?
# 👉 Generator একবার use হলে শেষ হয়ে যায় (exhausted)

