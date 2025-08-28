def main():
    size = int(input("Please enter the size of the steps: "))
    num = size
    if size == 0:
        print("That's illegal.") #idk how to handle the user entering text
    else:
        limit = int(input("Please enter a limit: "))
        while True:
            print(size)
            size += num
            if size > limit:
                break
main()