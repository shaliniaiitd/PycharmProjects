# x = 1
# def func(x):
#     x=2
#
# print(x)
# func(x)
# print(x)

# tup = (1,2,3)
#
# tup = tup + tuple((4,5,6))
#
# print(len(tup))
#
# x = [1,2,3]
# y  = [1,2,3]
# z = x
# print(x is y)
# print (x!= z)
#
#
# def mutate_string(string, position, character):
#     n_str = string[0:position] + character + string[position + 1 ::]
#     return n_str
#
#
# if __name__ == '__main__':
#     s = input()
#     i, c = input().split()
#     s_new = mutate_string(s, int(i), c)
#     print(s_new)


# def count_substring(string, sub_string):
#
#     count = string.count(sub_string)
#     return count
#
# print(count_substring("abcdcdc", "cdc"))

def count_substring(string, sub_string):
    count = 0
    start_index = 0
    while True:
        index = string.find(sub_string, start_index)
        if index == -1:
            break
        count += 1
        start_index = index + 1
    return count

print(count_substring("abcdcdc", "cdc"))
