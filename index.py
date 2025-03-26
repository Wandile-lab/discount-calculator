def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        return(price * (1-discount_percent / 100))
    else:
        return(price)
    
price = int(input("Place the initial price here: "))
discount_percent = int(input("Place the discount percentage here: "))

finalPrice = calculate_discount(price, discount_percent)
print(f"Your final price is:{finalPrice}")