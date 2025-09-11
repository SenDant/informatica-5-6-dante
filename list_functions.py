my_list = [5, 2, 3 , 1, 4]

greatest = max(my_list) #max is used to find the greatest value element in a list.
print(f"the greatest number in the list is {greatest}")

smallest = min(my_list)
print(f"the smallest number in the list is {smallest}") #min is used to find the smallest value element in a list.

list_sum = sum(my_list)
print(f"the sum of all numbers on the list is {list_sum}") #sums ints.

list_length = len(my_list)
print(f"this list has {list_length} elements.") #gets the # of elements in a list.

in_order = sorted(my_list) # .sort is a method, sorted() is a function.
print(in_order)


def filter_price(price):
    if (price >= 400):
        return True #leave it as it is
    else:
        return False #filter it(?)

item_price = [230, 400, 450, 350, 370]
filtered_price = filter(filter_price, item_price) # filter must have a function inside its parenthesis, that's
print(list(filtered_price))                       # why we define a function that'll do the job(?)