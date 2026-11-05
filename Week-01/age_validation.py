def validate_test_result(result):
    if type(result) is not dict:
        return False
    elif "status" not in result or "time" not in result:
        return False
    elif result["status"] in ("PASS", "FAIL", "TIMEOUT") and type(result["time"]) is int and result["time"] >=0:
        return True
    return False

assert validate_test_result({"status": "PASS", "time": 100}) is True
assert validate_test_result({"status": "FAIL", "time": 0}) is True
assert validate_test_result({"status": "ERROR", "time": 100}) is False
assert validate_test_result({"status": "PASS"}) is False
assert validate_test_result({"status": "PASS", "time": -5}) is False
assert validate_test_result({"status": "PASS", "time": "100"}) is False
assert validate_test_result({"status": "PASS", "time": True}) is False
assert validate_test_result([]) is False
print("All clear!")