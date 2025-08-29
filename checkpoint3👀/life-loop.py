import time
def main():
    print("-------Timer for exercising-------")
    print("Interval of 30 seconds per series.")
    print("Press Enter every time you end a set")
    print("----------------------------------")
    n = 0
    set = 1
    while True:
        n += set
        print(f"Set #{n}")
        print("Press Enter to rest for 30 seconds")
        cont = input("or type 'stop' to end the session...")
        if cont == "stop" and n == 1:
            print("What? You didn't do anything!")
            break
        if cont == "stop":
            print("Great Session! You're done now.")
            break
        print("Resting...")
        time.sleep(3)
        print("Time's up! Continue with your next set!")
        input("Press enter to continue")
        print("----------------------------------")
main()