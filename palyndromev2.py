def is_palyndrome(s):
    stack = []
    r = len(s)

    for char in s:
        stack.append(char)

    for char in s:
        if char != stack.pop():
            return False

    return True

print(is_palyndrome("level"))