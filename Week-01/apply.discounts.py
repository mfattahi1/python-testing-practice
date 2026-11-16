products = [
    {"name": "Laptop", "price": 1000, "discount": 10},
    {"name": "Mouse", "price": 50, "discount": 20},
    {"name": "Keyboard", "price": 80, "discount": 0}
]
def apply_discounts(products):
    result = []
    for item in products:
        my_dict={}
        my_dict["name"]= item["name"]
        my_dict["final_price"] = item["price"] * (1-item["discount"]/100)
        result.append(my_dict)
        
    return result


result = apply_discounts(products)

assert result == [
    {"name": "Laptop", "final_price": 900},
    {"name": "Mouse", "final_price": 40},
    {"name": "Keyboard", "final_price": 80}
]

assert products[0]["price"] == 1000
assert apply_discounts([]) == []

print("All tests passed!")