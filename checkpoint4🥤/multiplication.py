def main():
    num = int(input("Please, enter a positive number: "))
    table(num)

def table(num):
    i = 0
    if num < 0:
        print("You bastard. (ㆆ_ㆆ)")
    else:
        while i < 10:
            i += 1
            result = (num * i)
            print(f"{num} x {i}: {result}")
main()
