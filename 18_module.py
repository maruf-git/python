# we will be importing 19_moudle_export file and use its variables, functions etc

# directly importing the module by its file name
# import module_export as testImport
# print(testImport.fruits)
# print(testImport.person["name"])


# importing specific variable from a module
from module_export import person as student
print(student)
print(student["name"])