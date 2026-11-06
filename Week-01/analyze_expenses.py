

def analyze_expenses(filename):
    total = 0
    count = 0

    with open(filename, "r") as file:
        for line in file:
            if not line.strip():
                continue
            number = float(line.strip())
            total += number
            count +=1
    if count == 0:
        average = 0
    else:
        average = total / count
    my_dict={"total": total, "average": average, "count": count}
    return my_dict

print(analyze_expenses("expenses.txt"))

        