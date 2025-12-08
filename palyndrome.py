def is_palyndrome(s):
    stack = []
    r = len(s)

    for char in s:
        stack.append(char)

    for i in range(len(stack) - 1, -1, -1):
        if stack[i] != s[r - i - 1]:
            return False

    return True

print(is_palyndrome("level"))