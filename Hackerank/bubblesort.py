def countSwaps(a):
    length = len(a)
    numSwaps = 0 
    for i in range(length):
        for j in range(length - 1):
            #Swap adjacent elements if they are in decreasing order
            if (a[j] > a[j + 1]):
                a[j],a[j+1] = a[j+1],a[j]
                numSwaps += 1
    print(f"Array is sorted in {numSwaps} swaps.\nFirst Element: {a[0]}\nLast Element: {a[-1]}")
