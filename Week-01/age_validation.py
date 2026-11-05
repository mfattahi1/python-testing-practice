def validate_age(age):
    try:
        
        if (age >= 18 and age <= 65) and isinstance(age,int):
            return True
        else:
            return False

        
    except TypeError:
        return False


assert validate_age(18) is True
assert validate_age(65) is True
assert validate_age(30) is True

assert validate_age(17) is False
assert validate_age(66) is False
assert validate_age(0) is False

assert validate_age("25") is False
assert validate_age(18.5) is False
assert validate_age(None) is False
assert validate_age(True) is False

print("All tests passed!")