sales = [
    {"product": "Mouse", "quantity": 2, "price": 25},
    {"product": "Keyboard", "quantity": 1, "price": 80},
    {"product": "Mouse", "quantity": 3, "price": 25},
    {"product": "Monitor", "quantity": 1, "price": 200}
]
def summarize_sales(sales):
    my_dict = {}

    for item in sales:
        product = item["product"]
        revenue = item["quantity"] * item["price"]

        if product not in my_dict:
            my_dict[product] = revenue
        else:
            my_dict[product]+= revenue
    print(my_dict)
    return my_dict

assert summarize_sales(sales) == {
    "Mouse": 125,
    "Keyboard": 80,
    "Monitor": 200
}

assert summarize_sales([]) == {}

assert summarize_sales([
    {"product": "Book", "quantity": 2, "price": 10},
    {"product": "Book", "quantity": 1, "price": 15}
]) == {"Book": 35}

print("All tests passed!")