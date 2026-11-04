results = [
    {"id": "T01", "status": "PASS"},
    {"id": "T02", "status": "FAIL"},
    {"id": "T03", "status": "PASS"},
    {"id": "T04", "status": "TIMEOUT"},
    {"id": "T05", "status": "FAIL"}
]

def group_tests_by_status(results):
    grouped = {}

    for test in results:
        status = test["status"]
        test_id = test["id"]

        if status not in grouped:
            grouped[status] = []

        grouped[status].append(test_id)

    return grouped
    
assert group_tests_by_status(results) == {
    "PASS": ["T01", "T03"],
    "FAIL": ["T02", "T05"],
    "TIMEOUT": ["T04"]
}

assert group_tests_by_status([]) == {}

print("All tests passed!")

print(group_tests_by_status(results))