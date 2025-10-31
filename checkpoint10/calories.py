def main():
    food = {"milk": 73, "watermelon": 11, "almond milk": 30, "yogurt with fruit, fat free": 107.5,
            "sour cream, fat free": 9, "egg": 75, "egg white": 16, "cottage cheese, low fat": 20, "american pausterized cheese": 79,
            "lentils, boiled": 115, "edamame, boiled": 127, "almonds, dry roasted": 170, "peanuts, roasted": 166,
            "shrimp, boiled": 28, "chicken deli": 20, "celery": 1, "tomato": 8, "pears": 20, "ranch": 73, "quinoa, cooked": 56}
    print("Please, type in two foods: ")
    x = input("-")
    y = input("-")
    calculate_calories(food, x, y)
def calculate_calories(food, x, y):
    try:
        if x == "watermelon" and y == "milk":
            raise BaseException ("EW! you CANNOT mix watermelon and milk!")
        if x == "milk" and y == "watermelon":
            raise BaseException ("EW! you CANNOT mix watermelon and milk!")
        calories = 0
        calories = food[x] + food[y]
        print(f"total calories: {calories}")
    except KeyError:
        print("Invalid input(s)!")
main()