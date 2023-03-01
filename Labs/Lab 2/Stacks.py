def makeStack():
    return 'stack', []

def contents(stk):
    return stk[1]

def isStack(obj):
    return isinstance(obj, tuple) and obj[0] == 'stack' and isinstance(obj[1], list)

def push(stk, el):
    stk[1].insert(0, el)

def pop(stk):
    return stk[1].pop(0) if len(stk[1]) > 0 else None

def top(stk):
    return stk[1][0] if len(stk[1]) > 0 else None

def isStackEmpty(stk):
    return len(stk[1]) == 0

# Create a new stack
s = makeStack()

# Push some elements onto the stack
push(s, 1)
push(s, 2)
push(s, 3)

# Check the contents of the stack
print(contents(s))  # Output: [3, 2, 1]

# Check if s is a stack
print(isStack(s))   # Output: True

# Pop an element from the stack
pop(s)
print(contents(s))  # Output: [2, 1]

# Check the top element of the stack
print(top(s))       # Output: 2

# Check if the stack is empty
print(isStackEmpty(s))  # Output: False

