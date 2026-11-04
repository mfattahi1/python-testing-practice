test_names = [
    "  Login Test  ",
    "PASSWORD Check",
    "  ECU Security TEST ",
    "   ",
    "Connection  Timeout"
]
def clean_test_names(test_names):
    our_list=[]
    for text in test_names:
        clean_name = text.strip().lower().replace(" ", "_")
        if clean_name =="":
            our_list.append("unnamed")
        else:
            our_list.append(clean_name)
    return our_list

assert clean_test_names([" Hello World "]) == ["hello_world"]
assert clean_test_names(["   "]) == ["unnamed"]
assert clean_test_names(["A  B"]) == ["a__b"]
assert clean_test_names([]) == []
original = ["  Login TEST  ", "A  B", "   "]

assert clean_test_names(original) == [
    "login_test", "a__b", "unnamed"
]

assert original == ["  Login TEST  ", "A  B", "   "]
print("All fine!")