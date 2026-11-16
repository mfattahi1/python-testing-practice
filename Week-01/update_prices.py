def update_prices(prices, increase):
    new_list=[]
    for item in prices:
        new_list.append(round(item*(1+increase/100),2))
        
    return new_list

assert update_prices([100, 200, 50], 10) == [110, 220, 55]
assert update_prices([100, 200], 0) == [100, 200]
assert update_prices([], 15) == []

prices = [100, 200, 50]
updated = update_prices(prices, 10)

assert prices == [100, 200, 50]

print("All tests passed!")