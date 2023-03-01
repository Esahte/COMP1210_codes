def fibonacci(n):
    if n < 0:
        return 'not fib'
    elif n in [1, 2]:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

print(fibonacci(7))

num = int(input('Enter a number: '))
for i in range(1, num+1):
    print(fibonacci(i), end=' ')