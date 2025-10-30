n = int(input())
if n < 0:
    raise ValueError(f"This is not possible with {n}.")
factorial = 1
for i in range(1, n + 1):
    factorial *= i
print(n,"! = ",factorial)