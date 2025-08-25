import random
print("WELCOME TO THE GOBLIN GAME")
print("The best game EVER!")
playername = input(("Insert your name: "))
print(f"{playername}, can you find the goblin?")
print("|_|"*5)
goblinposition = random.randint(1, 5)
keeptrying = True
while keeptrying:
    guessposition = int(input("Can you guess where the goblin is? "))
    if guessposition == goblinposition:
        print("Well done! You found the goblin!!!")
        keeptrying = False
    else:
        print("WRONG. AGAIN!!!")
