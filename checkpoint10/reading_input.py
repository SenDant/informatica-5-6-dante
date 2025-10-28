def main():
  number = read_input("Please type in a number: ", 5, 10)
  print("You typed in:", number)

def read_input(message, pmeter1, pmeter2):
    while True:
        try:
            x = int(input(message))
            if x > pmeter1 and x < pmeter2:
                return x
            else:
                print(f"please, type a number BETWEEN {pmeter1} and {pmeter2}.")
                continue
        except ValueError:
            print(f"please, type a NUMBER between {pmeter1} and {pmeter2}.")

main()