
def update_stock(inventory, product_name, quantity):
    for i in range(len(inventory)):
        if product_name == inventory[i]["name"]:
        
            if (inventory[i]["stock"] + quantity) >= 0:
                inventory[i]["stock"] = inventory[i]["stock"] + quantity
                return True
            else:
                return False
    return False

inventory = [
    {"name": "Laptop", "stock": 5},
    {"name": "Mouse", "stock": 12},
    {"name": "Keyboard", "stock": 8}
]

assert update_stock(inventory, "Laptop", -2) is True
assert inventory[0]["stock"] == 3

assert update_stock(inventory, "Mouse", 5) is True
assert inventory[1]["stock"] == 17

assert update_stock(inventory, "Keyboard", -20) is False
assert inventory[2]["stock"] == 8

assert update_stock(inventory, "Monitor", 3) is False

assert update_stock(inventory, "Laptop", -3) is True
assert inventory[0]["stock"] == 0
inventory = [{"name": "Mouse", "stock": 5}]

assert update_stock(inventory, "Mouse", -10) is False
assert inventory[0]["stock"] == 5

print("All tests passed!")