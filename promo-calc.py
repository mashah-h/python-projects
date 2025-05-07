promo = input("Enter your Promo: ")
price = int(input("Enter price of item: "))

if promo == "Karibu":
    if price >3000 and price < 9500:
        discount = 0.13 * price
    else:
        discount = 0
elif promo == "Nairobi":
    if price < 2900:
        discount = 0.25 * price
else:
    discount = 0

discountedPrice = price - discount
print("Discounted price: ",discountedPrice)






