#Given a list of words in Python, the task is to remove the Nth occurrence of the given word in that list.

lst = ["can", "you",  "can", "a", "can" "?"]
target = 'can'
n  = 1
print(lst)
def find_nth_occurence(inpt,target,n):
    flag = 0; index = 0
    for word in inpt:
        print(index, word,target)
        if word == target:
            flag = flag +1
            print(flag)
            if flag == n:
                return inpt[index+1::]
               # lst.pop(index)
        index += 1

    #print (inpt)

#Extract String after Nth occurrence of K character
N=3
K = 's'
inpt = "consistent is finally successful"
print(find_nth_occurence(inpt,'s',3))






