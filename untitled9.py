a = int(input("Enter dimension 1: "))
b = int(input("Enter dimension 2: "))
c = int(input("Enter dimension 3: "))

if (a + b) > c or (b + c) > a or (a + c) > b:
    print("Number can be a triangle")
else:
    print("Number cannot be a triangle")




