# Kirana Store Calculator Program

# Initial Total Price
total_price = 0

# Store Name
store_name = "kirana store"

# Infinite Loop for Multiple Items
while True:
    userinput = input("Enter Your price (or press 'q' to quit): ")
    
    # Exit Condition
    if userinput.lower() == 'q':
        print(f"Final total price: ₹{total_price}")
        print(f"Thank you for shopping at {store_name}!")
        break

    # Validate Input
    if userinput.isdigit():
        total_price += int(userinput)
        print(f"Your total is now: ₹{total_price}\n")
    else:
        print("❌ Invalid input! Please enter a valid number or 'q' to quit.\n")
