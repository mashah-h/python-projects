costPrice = int(input("Enter the cost: "))
sellingPrice = int(input("Enter the selling price: "))
if costPrice > 0 and sellingPrice > 0:
    if sellingPrice > costPrice:
        profit = sellingPrice - costPrice
        print("Profit:",profit)
        
    elif costPrice > sellingPrice:
        loss = costPrice - sellingPrice
        print("Loss:",loss)
        
    else:
        print("You can't use same amount")
else:
    print("Enter valid amounts")
    


