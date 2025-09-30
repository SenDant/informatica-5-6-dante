def main():
    print("Please, type in a message")
    message = input()
    dictionary = {}
    c_count(message, dictionary)
def c_count(m, d):
    for keys in m:
        d.setdefault(keys, 0)
        d[keys] += 1
    print(d)
    print(len(m))
    #print
main()