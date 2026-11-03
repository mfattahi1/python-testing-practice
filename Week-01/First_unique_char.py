def first_unique_char(text):
    counts = {}

    for char in text:
        counts[char] = counts.get(char, 0) + 1

    for char, count in counts.items():
        if count == 1:
            return char

    return None

assert first_unique_char("aabbcde") == "c"
assert first_unique_char("aabbcc") is None
assert first_unique_char("swiss") == "w"
assert first_unique_char("") is None
assert first_unique_char("python") == "p"
assert first_unique_char("a") == "a"

print("All tests passed!")