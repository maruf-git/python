# match is like switch case

mark = 50

match mark:
    case x if x>=80:
        print("A++")
    case x if x >=70:
        print("A")
    case x if x>=60:
        print("A-")
    case _:
        print("Pass")
        
        
print("Alternative better way:")

match mark:
    case _ if mark >= 80:
        print("A++")
    case _ if mark >= 70:
        print("A")
    case _ if mark >= 60:
        print("A-")
    case _:
        print("Pass")