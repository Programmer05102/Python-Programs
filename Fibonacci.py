
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

nums = int(input("Enter Number Of Terms: "))
seq = [fibonacci(i) for i in range(nums)]
print(seq)