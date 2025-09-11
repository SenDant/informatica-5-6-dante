def main():         #I finished the assignment before its instructions were changed, so it's different..
    n = 0           #So, I deleted the function that asked the user to create their list, and moved that stuff
    print("------Create a list.------") #to main so the other functions have access to that user's list.
    print("----Type '0' when done----")
    user_list = []
    while True:
        n += 1
        elements = int(input(f"Please enter the element #{n} of the list: "))
        user_list.append(elements)
        if elements == 0:
            user_list.remove(0)
            print(f"here's your list: {user_list}")
            print(f"here's your sorted list: {sorted(user_list)}")
            break
    length(user_list)
    mean(user_list)
    range_of_list(user_list)
    
def length(lista):
    #lista = ["ichi", "ni", "san", "yon", "go", "roku", "nana"] //list that was before
    print(f"the length of your list is of: {len(lista)}")
def mean(int_list):
    #int_list = [1, 3, 5, 2, 7, 8] //list that was before
    sum_list = sum(int_list)
    len_list = len(int_list)
    res = (sum_list / len_list)
    print(f"the mean in your list is: {res}")
def range_of_list(nums):
    #nums = [2, 3, 8, 10, 20] //list that was before
    min_num = min(nums)
    max_num = max(nums)
    res = (max_num - min_num)
    print(f"the range of your list is: {res}")
main()