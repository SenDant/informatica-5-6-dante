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
while True:
    try:
        x = int(input("What's x?: "))
    except ValueError:
        print(("that is NOT a number."))
    else:
        break
print(f"x is equal to {x}.")