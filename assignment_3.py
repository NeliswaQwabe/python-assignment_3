# Main program
# Prompt user for input
price = float(input("Enter the price: "))
discount_percent = float(input("Enter the discount (%): "))

# Function to calculate final price after discount
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        final_price = price - (price * discount_percent / 100)
        return final_price
    else:
        return price  # Return the original price if discount is less than 20%

# Call the function and print the result
print("Final price:", calculate_discount(price, discount_percent))