a = int(input("Enter your number 1: "))
b = int(input("Enter your number 2: "))
c = int(input("Enter your number 3: "))
d = int(input("Enter your number 4: "))

if a>b and a>c and a>d:
    print("Largest number: ",a)
elif b>a and b>c and b>d:
    print("Largest number: ",b)
elif c>b and c>a and c>d:
    print("Largest number: ",c)
elif d>b and d>c and d>a:
    print("Largest number: ",d)
else:
    print("Enter valid number")
    
    print("Largest number: ",a)


        