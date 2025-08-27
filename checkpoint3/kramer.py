print("Stranger: Greetings! ♪(^∇^*)")
while True:
    greeting = input("You: ").strip().title()
    if greeting.startswith("Hello"):
        print("You won nothing. ಥ_ಥ")
    elif greeting.startswith("H"):
        print("You won $20. ^_^")
    else:
        print("Stranger: YOU JUST WON $100!!! (/≧▽≦)/")
        break