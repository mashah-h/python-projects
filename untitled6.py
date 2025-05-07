num1 = int(input("Enter your first number: "))
num2 = int(input("Enter your second number: "))
num3 = int(input("Enter your third number: "))


if num1 < num2 and num1 < num3:
    print("Smallest: ", num1)
elif num2 < num1 and num2 < num3:
    print("Smallest: ", num2)
elif num3 < num1 and num3 < num2:
    print("Smallest: ", num3)
else:
    print("Please enter different numbers")
    