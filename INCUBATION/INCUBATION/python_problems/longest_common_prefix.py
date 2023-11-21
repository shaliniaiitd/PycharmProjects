def lcp(str_list):
    result = ''
    for ch,*rest in map(set,zip(*str_list)):
        if not rest:
            result += ch
    return result

print(lcp(['flower', 'floor','flight']))

# Write a Python function to find the second-largest number in a given list of integers.

def sln(int_list):
 print(int_list)
 int_list.sort()
 print(int_list[-2])

print(sln([4,7,-2,-3,5,9]))