        # SYNTAX ERROR
# print("Hello World :3) 

        # VALUE ERROR
# try:
#     x = int(input("What's x?: "))
#     print(f"x is equal to {x}.")
# except ValueError:
#     print(("that is NOT a number."))

        #ZERO DIVISION ERROR
# def span(divide_by):
#     try:
#         return 42 / divide_by
#     except ZeroDivisionError:
#         return "not possible."

# print(span(2))
# print(span(12))
# print(span(0))
# print(span(1))

        # ELSE
# while True:
#     try:
#         x = int(input("What's x?: "))
#     except ValueError:
#         print(("that is NOT a number."))
#     else:
#         break
# print(f"x is equal to {x}.")

        #
def read_small_integer():
    while True:
        try:
                input_str = input("Please type in an integer: ")
                number = int(input_str)
                if number < 100 and number >= 0:
                        return number
        except ValueError:
              pass      # to not do anything, just keep it.
        print("This input is invalid :3")
        
number = read_small_integer()
print(number, "to the power of three is: ", number**3) # ** means to the power of 