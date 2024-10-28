menu = {"Pizza": 3.00,
        "Nachos": 4.50,
        "Popcorn": 6.00,
        "Fries": 2.50,
        "Chips": 1.00,
        "Pretzels": 3.50,
        "Soda": 3.00,
        "Lemonade": 4.25}
cart = []
total = 0

print("--------MENU--------")
for key, value in menu.items():
    print(f"{key:10}: ${value:.2f}")
print("--------------------")

while True:
    food = input("Select an item (q to quit): ").title()
    if food == "Q":
        break
    elif food in menu:
        cart.append(food)
    else:
        print("***Item not found on the menu.***")
print("--------YOUR ORDER--------")
print("Your cart items:")
for food in cart:
    print(food, end=" ")
    total += menu[food]
print()
print(f"Total: ${total:.2f}")
