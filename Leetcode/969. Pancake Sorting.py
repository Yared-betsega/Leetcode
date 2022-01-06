def pancakeSort(arr):
        sortedArr = sorted(arr)
        ans = []
        i = len(arr)
        
        while arr != sortedArr:
            flipped = []
            maxIndex = arr.index(max(arr[:i]))
                                         
            if maxIndex == 0:
                ans.append(len(arr[:i]))
                flipped.extend(arr[:i][::-1])
                flipped.extend(arr[i:])
            
            elif maxIndex == len(arr[:i])-1:
                flipped = copy.deepcopy(arr)
                                         
            else:
                ans.append(maxIndex + 1)
                x = arr[:maxIndex + 1]
                flipped.extend(x[::-1])
                flipped.extend(arr[maxIndex+1:])

                ans.append(len(arr[:i]))
                arr = copy.deepcopy(flipped)
                flipped = []
                flipped.extend(arr[:i][::-1])
                flipped.extend(arr[i:])
                                         
            
            arr = copy.deepcopy(flipped)
            i -= 1

        return ans
