def countingSort(arr):
    newArr = [0] * 100
    length = len(arr)
    for i in range(length):
        newArr[arr[i]]=newArr[arr[i]]+1
    return newArr