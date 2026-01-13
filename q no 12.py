# Inventory Management System using List of Dictionaries

# Initial inventory
inventory = [
    {'name': 'Laptop', 'price': 50000, 'quantity': 5}
]

# Function to add a new product
def add_product():
    name = input("Enter product name: ")

    # Check for duplicate product
    for product in inventory:
        if product['name'].lower() == name.lower():
            print("Product already exists!")
            return

    price = float(input("Enter price: "))
    quantity = int(input("Enter quantity: "))

    if price <= 0 or quantity <= 0:
        print("Price and quantity must be positive numbers!")
        return

    inventory.append({'name': name, 'price': price, 'quantity': quantity})
    print("Product added successfully!")

# Function to view all products
def view_products():
    if len(inventory) == 0:
        print("Inventory is empty!")
        return

    print("\nName\t\tPrice\tQuantity")
    print("-" * 30)
    for product in inventory:
        print(f"{product['name']}\t{product['price']}\t{product['quantity']}")

# Function to up