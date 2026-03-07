per_product_price=1000
quantity=int(input("Enter quantity: "))
total_price=quantity*per_product_price
print(f"Price: {total_price}")
discount=int(input("Enter discount: "))
discount_price=total_price*(discount/100)
print(f"Discount: {discount_price} Taka")
after_discount=total_price-discount_price
print(f"After discount: {after_discount}")