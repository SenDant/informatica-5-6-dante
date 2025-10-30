def main():
    while True:
        try:
            user = input("Enter the fraction of your fuel: ").split("/")
            x = int(user[0])
            y = int(user[1])
            result = x / y * 100
            if x > y:
                print("Invalid input.")
                continue
            else:
                if result >= 99:
                    print("F")
                    break
                elif result <= 1:
                    print("E")
                    break
                else:
                    print(f"{result}%")
                    break
        except (ZeroDivisionError, ValueError, UnboundLocalError):
            print("Invalid input. Please try again.")
            continue
main()