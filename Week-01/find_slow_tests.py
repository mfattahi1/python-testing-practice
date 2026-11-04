tests = [
    {"id": "T01", "time": 100},
    {"id": "T02", "time": 250},
    {"id": "T03", "time": 180},
    {"id": "T04", "time": 300}
]

def find_slow_tests(tests, threshold):
    slow_tests = []
    for i in tests:
        if i["time"] > threshold:
            slow_tests.append(i["id"])

    return slow_tests

assert find_slow_tests(tests, 200) == ["T02", "T04"]
assert find_slow_tests(tests, 300) == []
assert find_slow_tests([], 200) == []
assert find_slow_tests(tests, 100) == ["T02", "T03", "T04"]
print("All fine!")