def main():
    length()
    mean()
    range_of_list()
    user()
def length():
    lista = ["ichi", "ni", "san", "yon", "go", "roku", "nana"]
    print(len(lista)) #?
def mean():
    int_list = [1, 3, 5, 2, 7, 8]
    sum_list = sum(int_list)
    len_list = len(int_list)
    res = (sum_list / len_list)
    print(res)
def range_of_list():
    nums = [2, 3, 8, 10, 20]
    min_num = min(nums)
    max_num = max(nums)
    res = (max_num - min_num)
    print(res)
def user():
    n = 0
    print("------Create a list.------")
    print("-Type '0' to end the list-")
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
main()