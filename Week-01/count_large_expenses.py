def count_large_expenses(filename, threshold):
    with open(filename, "r") as file:
        count = 0
        
        for line in file:
            if not line.strip():
                continue
            number = float(line.strip())
            if number > threshold:
                count +=1
        
        return count

assert count_large_expenses("expenses.txt", 20) == 2
assert count_large_expenses("expenses.txt", 40) == 0
assert count_large_expenses("expenses.txt", 5) == 5
print("All fine!")
