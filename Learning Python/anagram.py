with open("data_file", 'r') as f:

    for line in f:
        tup1 = eval(line)    #to read tuple input as tuple
        str1 = tup1[0]
        str2 = tup1[1]
        print(str1, str2)



str1 = list("shalini")
str2 = list("anlisih")

for el in str1:
    if el not in str2 :
        print("Not anagram")
        break
    else:
        str2.remove(el)
else:
    print("Strings are anagrams")
