def save_names(filename, names):
    number_of_names=0
    with open(filename, "w") as file:
        for name in names:
            if not name.strip():
                continue
            else:
                clean_name = name.strip().lower()
                file.write(clean_name +"\n")
                number_of_names +=1
    return number_of_names

names = [" Anna ", "JOHN", "  ", "Sara "]

count = save_names("names.txt", names)

print(count)  # 3
assert save_names("names.txt", names) == 3

with open("names.txt", "r") as file:
    assert file.read() == "anna\njohn\nsara\n"