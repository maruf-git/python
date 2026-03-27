def myFunction():
    pass

print("Hello world!")
myFunction()
print("Hello world 2!")

def myFunction():
    print("This is my function")
    
myFunction()


# arguuments

def printAny(*args):
    for arg in args:
        print(arg)
        
printAny("maruf", "rifat", 24)
print(printAny.__name__)