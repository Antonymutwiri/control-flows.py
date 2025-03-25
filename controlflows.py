def calculate_discount(price, discount_percent):
    """
    Calculates the final price after applying a discount if the discount is 20% or higher.
    
    Parameters:
    price (float): Original price of the item
    discount_percent (float): Discount percentage to apply
    
    Returns:
    float: Final price after discount (or original price if discount < 20%)
    """
    if discount_percent >= 20:
        discount_amount = price * (discount_percent / 100)
        final_price = price - discount_amount
        return final_price
    else:
        return price

# Get user input
original_price = float(input("Enter the original price of the item: "))
discount = float(input("Enter the discount percentage: "))

# Calculate and display the result
final_price = calculate_discount(original_price, discount)

if discount >= 20:
    print(f"Original price: ${original_price:.2f}")
    print(f"Discount applied: {discount}%")
    print(f"Final price after discount: ${final_price:.2f}")
else:
    print(f"No discount applied (needs to be 20% or higher). Original price: ${original_price:.2f}")