def validate_password(password):
    has_uppercase = False
    has_lowercase = False
    has_digits= False
    has_spaces = False
    if type(password) is not str:
        return False
    if len(password)<8:
        return False
    for char in password:
        if char.isupper():
            has_uppercase = True
        elif char.islower():
            has_lowercase= True
        elif char.isdigit():
            has_digits= True
        elif char == " ":
            has_spaces = True

    if has_uppercase is True and has_lowercase is True and has_digits is True and has_spaces is False:
        return True
    else:
        return False

assert validate_password("Hello123") is True
assert validate_password("Python2026") is True

assert validate_password("hello123") is False
assert validate_password("HELLO123") is False
assert validate_password("Helloabc") is False
assert validate_password("Hi123") is False
assert validate_password("Hello 123") is False
assert validate_password(12345678) is False
assert validate_password("") is False
print("All fine!")