def nextGreaterElement(nums1, nums2):
  
        # Find the next greatest element for all elements in nums2 using monotonic stack concept
        # And store it in the dictionary d
        great = []
        d = {}
        great.append(nums2[0])
        d[great[0]] = -1
        for i in range(1, len(nums2)):
            if nums2[i] < great[-1]:
                great.append(nums2[i])
                d[nums2[i]] = -1
            else:
                while great and nums2[i] > great[-1]:
                    last = great.pop()
                    d[last] = nums2[i]
                great.append(nums2[i])
                d[nums2[i]] = -1
                
        # Find the next greatest element for all elements in nums1 from the dictionary above
        # Hence O(nums1.length + nums2.length) solution
        ans = []
        for j in range(len(nums1)):
            ans.append(d[nums1[j]])
        return ans
