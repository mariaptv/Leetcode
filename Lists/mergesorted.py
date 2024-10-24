def mergesorted(arr1, arr2):
    result = []
    i = 0
    j = 0
    while i < len(arr1) or j < len(arr2):
        if i == len(arr1):
            result.append(arr2[j])
            j += 1
        elif j == len(arr2):
            result.append(arr1[i])
            i += 1
        elif arr1[i] <= arr2[j]:
            result.append(arr1[i])
            i += 1
        else:
            result.append(arr2[j])
            j += 1

    return result



print(mergesorted([1,2,2,3,4,5,7,9,10],[1,2,3,4,10]))