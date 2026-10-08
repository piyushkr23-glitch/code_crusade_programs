# Shopping Bill Calculator
Customer_name = input("Enter your name:")
Item_Price = float(input("Enter the price of the item:"))
Quantity = int(input("Enter the quantity of the item:"))
Discount = float(input("Enter the discount percentage:"))

Total_Price = Item_Price * Quantity

Discount_Amount = Discount / 100 * Total_Price

Final_Bill = Total_Price - Discount_Amount

# Output

# Printing _ Type

print("Customer Name:", (Customer_name))
print("Item_Price:", (Item_Price))
print("Quantity:", (Quantity))
print("Discount:", (Discount))
print("Total_Price:", (Total_Price))
print("Discount_Amount:", (Discount_Amount))
print("Final_Bill:", (Final_Bill))   