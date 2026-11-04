statuses = [
    " PASS ",
    "Fail",
    " TIMEOUT",
    "  passed TEST  ",
    "",
    "   ",
    "ERROR "
]
def normalize_statuses(statuses):
    final_list = []
    for text in statuses:
            clear_text = text.strip().lower()
            if clear_text == "":
                  final_list.append("unknown")
            else:
                final_list.append(clear_text)
   
    return final_list
    
assert normalize_statuses([" PASS ", "Fail"]) == [
    "pass", "fail"
]

assert normalize_statuses(["", "   "]) == [
    "unknown", "unknown"
]

assert normalize_statuses([" Hello WORLD "]) == [
    "hello world"
]

assert normalize_statuses([]) == []

assert normalize_statuses(["  TIMEOUT  ", "Error"]) == [
    "timeout", "error"
]

print("All tests passed!")