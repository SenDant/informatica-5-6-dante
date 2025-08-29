import getpass

def main():
    print("---Sign in---")
    password = getpass.getpass("Set your password: ")
    input("Press enter to log in.")
    print("-------------")
    check_password(password)

def check_password(p):
    guess = input("Please enter your password: ")
    if p == guess:
        print("--Correct password.--")
    if p != guess:
        print("--Incorrect password, please try again later.--")
    print("The program has ended.")

main()