a = [4, 1, 3, 9, 7]
for i in range(len(a)):
    min = i
    for j in range(i+1,len(a)):
        if a[j] < a[min]:
            min = j
    a[i],a[min] = a[min], a[i]


class Solution: 
   def select(self, arr, i):
       min = i
       for i in range(i, len(arr)):
           if arr[i] < arr[min]:
               min = i
       return arr[min]
   def selectionSort(self, arr,n):
       #code here
       n=len(arr)
       for i in range(n-1):
           min_ind=i
           print(i)
           for j in range(i+1,n):
               if arr[j]<arr[min_ind]:
                   arr[min_ind],arr[j]=arr[j],arr[min_ind]
           return arr


x = Solution()
print(x.selectionSort(a, len(a)))