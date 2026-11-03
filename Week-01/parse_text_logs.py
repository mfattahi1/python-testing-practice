logs = [
    "T01,PASS,120",
    "T02,FAIL,250",
    "T03,PASS,90",
    "T04,TIMEOUT,500"
]

def parse_test_logs(logs):
    result = []
    
    
    for line in logs:
        parts = line.split(",")
        my_dict= {"id": parts[0], "status": parts[1], "time": int(parts[2])}
        result.append(my_dict)
    return result

assert parse_test_logs(["T01,PASS,120"]) == [
    {"id": "T01", "status": "PASS", "time": 120}
]

assert parse_test_logs([]) == []

assert parse_test_logs(["T02,FAIL,250"]) == [
    {"id": "T02", "status": "FAIL", "time": 250}
]
assert parse_test_logs([
    "T01,PASS,100",
    "T02,FAIL,200"
]) == [
    {"id": "T01", "status": "PASS", "time": 100},
    {"id": "T02", "status": "FAIL", "time": 200}
]
print("All tests passed!")