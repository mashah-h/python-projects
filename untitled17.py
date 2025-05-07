age = int(input("Enter your age: "))
if age > 0:
    if age <=12 :
        print("Child")
    elif age > 12 and age < 19:
        print("Teen")
    else:
        print("Adult")
else:
    print("Enter valid number for age")
    

