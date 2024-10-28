# Concession Stand Ordering System

## Description
This Python program allows users to place an order from a predefined menu of snacks and drinks. Users can select items one by one, and the program calculates and displays the total cost of the items in their cart. The program also verifies each item to ensure it’s on the menu, providing a helpful prompt if an invalid item is selected.

## Features
- Displays a menu of available items and their prices.
- Allows users to add items to their cart by typing in the item name.
- Ensures each selected item is on the menu, displaying a message if the item is not found.
- Calculates and displays the total cost of items in the cart.
- Users can exit the selection process by typing 'q' or 'Q'.

## How to Use
1. **Clone or download this repository** to your local machine.
2. **Run the program** in a Python environment.
3. The program will display a menu with available items and prices.
4. Follow the prompt to:
   - Enter the name of the item you want to add to your cart (case-insensitive).
   - Type 'q' or 'Q' to finish your order and see the total.
5. **The program will display the items in your cart** and the total cost.

## Example Usage
```bash
--------MENU--------
Pizza     : $3.00
Nachos    : $4.50
Popcorn   : $6.00
Fries     : $2.50
Chips     : $1.00
Pretzels  : $3.50
Soda      : $3.00
Lemonade  : $4.25
--------------------
Select an item (q to quit): Pizza
Select an item (q to quit): Soda
Select an item (q to quit): Burger
***Item not found on the menu.***
Select an item (q to quit): Fries
Select an item (q to quit): q
--------YOUR ORDER--------
Your cart items:
Pizza Soda Fries 
Total: $8.50
