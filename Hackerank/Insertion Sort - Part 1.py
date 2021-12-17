length = len(arr)-1
cur = arr[length]
while length >= 0:
    if length == 0:
        arr[length] = cur
        print(" ".join(list(map(str, arr))))
        break
    if arr[length - 1] > cur:
        arr[length] = arr[length - 1]
        print(" ".join(list(map(str, arr))))
    elif arr[length - 1] <= cur:
        arr[length] = cur
        print(" ".join(list(map(str, arr))))
        break
    length -=1

