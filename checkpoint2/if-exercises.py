def main():     #Difficulty: Medium 🧅🧅🧅🧅🧅
    x = int(input("Please enter the value of x: "))
    y = int(input("Please enter the value of y: "))
    o = input("Please enter the icon for the type of operation you wish to execute: ")
    operation(o, x, y)
    
def operation(op, ex, why):
    if op == "+" or "-" or "*" or "/":
        if op == "+":
            calculate = ex + why
            print(f"{ex} + {why}: {calculate}")
        if op == "-":
            calculate = ex - why
            print(f"{ex} - {why}: {calculate}")
        if op == "*":
            calculate = ex * why
            print(f"{ex} * {why}: {calculate}")
        if op == "/":
            calculate = ex / why
            print(f"{ex} / {why}: {calculate}")
    else: print("Error.")

main()