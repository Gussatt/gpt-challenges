# Here is a problem that challenges you to use both a Stack and a Queue together. This is very common in interview questions.
# The Problem: Reverse the First k Elements
# You have a Queue of numbers. Your task is to reverse the order of the first k elements of the queue, while leaving the rest of the elements in their original order.
# Constraint: You can only use standard Stack and Queue operations. No using index access (like queue[0]) or slicing!
# Example:

#     Input Queue: [10, 20, 30, 40, 50]
#     k: 3
#     Expected Output: [30, 20, 10, 40, 50] (Notice: 10, 20, 30 reversed to 30, 20, 10. The 40 and 50 stayed the same.)

# Why this is tricky
# A Queue is FIFO (First In, First Out). If you just pull items out and put them back in, they stay in the same order. A Stack is LIFO (Last In, First Out). It naturally reverses things.
# Hint:
#     Dequeue the first k items and put them into a Stack.
#     ... (What do you do with the stack now?)
#     ... (What about the remaining items in the queue?)
# Can you write the logic for this? (You can use a Python list to simulate the Queue using pop(0) for dequeue and append() for enqueue).


def reverse(queue,k):
    if k > len(queue) or k < 0:
        return queue 
    
    stack = []
    cnt = len(queue) - k

    for i in range (0,k):
        stack.append(queue.pop(0))
    
    for j in range (0,len(stack)):
        queue.append(stack.pop())
    
    for r in range (0,cnt):
        val = queue.pop(0)
        queue.append(val)

    return queue
    
list = [10, 20, 30, 40, 50]
print(reverse(list, 3))