def is_balanced(s):
    stack = []
    
    # Iterate through the string
    for char in s:
        # If it's an opening bracket, push to stack
        if char in ["(", "{", "["]: 
            stack.append(char)
        elif char in [")","]","}"]:
            if stack[-1] == "(" and char != ")":
                return False
            elif stack[-1] == "{" and char != "}":
                return False
            elif stack[-1] == "[" and char != "]":
                return False
        # If it's a closing bracket, pop from stack
        else:
            stack.pop()
            
    # If the code finishes running, it must be valid
    # After the loop finishes:
    if len(stack) == 0:
        return True  # Empty stack means everything was matched!
    else:
        return False # Leftover items mean we have unclosed brackets.

print(is_balanced("(("))