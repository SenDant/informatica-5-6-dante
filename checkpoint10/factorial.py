def main():
    print("-------Factorial Calculator-------")
    print("Please, type in a positive number: ")
    x = int(input())
    factorial_calc(x)

def factorial_calc(n):  # 4! = 24
    if n < 0:
        raise ValueError(f"ERROR, NEGATIVE INPUT: {n}.")
    factorial = 1
    for i in range(1, n + 1):
        factorial *= i
    print("-"*34)
    print(f"{n}! = {factorial}")

main()