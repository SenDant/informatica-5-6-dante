def main():
    while True:
        try:
            user = input("Enter the fraction of your fuel: ").split("/")
            result = (int(user[0]) / int(user[1])) * 100
            if int(user[0]) > int(user[1]):
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