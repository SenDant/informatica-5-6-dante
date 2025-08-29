num = int(input("Please enter an integer: "))
if num % 5 == 0 and num % 3 == 0:
    print("FizzBuzz")
elif num % 3 == 0:
    print("Fizz")
elif num % 5 == 0:
    print("Buzz")
if num % 3 != 0 and num % 5 != 0:
    print(num)
#if num % 1 == 0 and num % num == 0:
    #print("Prime")