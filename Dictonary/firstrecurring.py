def first_recurring(arr):
    new_dict = {}

    for i in arr:
        if i not in new_dict:
            new_dict[i] = 0
        elif i in new_dict:
            return i

    return 0

def printdict(dict):
    for i in dict.items():
        print(i)




print(first_recurring([1,2,3,4,5,1]))
printdict({1:2,3:4})

