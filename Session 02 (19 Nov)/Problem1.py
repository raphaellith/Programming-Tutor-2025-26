# Approach 1: Uses a hash set

def has_no_repeating_chars1(string: str) -> bool:
    seen_chars = set()

    for char in string:
        if char in seen_chars:
            return False
        seen_chars.add(char)

    return True


# Approach 2: Uses an array, assuming the string contains only ASCII characters

def has_no_repeating_chars2(string: str) -> bool:
    char_has_appeared = [False for _ in range(128)]

    for char in string:
        ascii_code = ord(char)
        if char_has_appeared[ascii_code]:
            return False
        char_has_appeared[ascii_code] = True

    return True