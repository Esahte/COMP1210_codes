# def factorial(n):
#     return 1 if (n == 1 or n == 0) else n * factorial(n - 1)

def factorial(n):
    if n < 0:
        return None
    elif n == 0:
        return 1
    else:
        # create a dictionary to store factorials'
        fact = {0: 1}
        for i in range(1, n + 1):
            fact[i] = i * fact[i - 1]
        return fact[n]


# example usage
print(factorial(5))  # output: 120
print(factorial(0))  # output: 1
print(factorial(-5))  # output: None
for j in range(125):
    print(factorial(j))
