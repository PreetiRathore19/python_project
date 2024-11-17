# Menu dictionary
menu = {
    "pizza": 40,
    "coffee": 50,
    "burger": 70,
    "icecream": 60,
}

# Welcome message
print("Welcome to my restaurant")
print("Menu:\npizza: 40\ncoffee: 50\nburger: 70\nicecream: 60")

# Initialize the total
order_total = 0

# First order
item_1 = input("Enter the name of the item you want to order: ")

if item_1 in menu:
    order_total += menu[item_1]
    print(f"Your {item_1} has been added to your order.")
else:
    print(f"Sorry, {item_1} is not available.")

# Check if the user wants to order more
another_order = input("Do you want to add another item? (Yes/No): ")

if another_order.lower() == "yes":
    item_2 = input("Enter the name of the second item: ")
    if item_2 in menu:
        order_total += menu[item_2]
        print(f"Your {item_2} has been added to your order.")
    else:
        print(f"Sorry, {item_2} is not available.")

# Print total
print(f"The total amount to pay is: {order_total}")
