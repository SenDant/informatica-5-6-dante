def main():
    x = int(input("Please, type in a positive number: "))
    factorial_calc(x)

def factorial_calc(n):  # 4! = 24
    if n < 0:
        raise ValueError(f"ERROR, NEGATIVE INPUT: {n}.")
    factorial = 1

    for i in range(1, n + 1):
        factorial *= i
    print(f"{n}! = {factorial}")
main()