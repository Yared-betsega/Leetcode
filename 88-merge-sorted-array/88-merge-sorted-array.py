class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        
        # # Solution using sorting
        # for i in range(len(nums2)):
        #     nums1.pop()
        # for i in range(len(nums2)):
        #     nums1.append(nums2[i])
        # nums1.sort()
        
        # O(m+n) Solution or optimum solution
        nums1_last, nums2_last = m-1, n-1
        if n != 0:
            for i in range(m + n - 1, -1, -1):
                if nums1[nums1_last] >= nums2[nums2_last]:
                    nums1[i] = nums1[nums1_last]
                    nums1_last -= 1
                elif nums1[nums1_last] < nums2[nums2_last]:
                    nums1[i] = nums2[nums2_last]
                    nums2_last -= 1
                if nums1_last < 0 or nums2_last < 0:
                    break  

            if nums1_last < 0:
                for i in range(nums2_last, -1, -1):
                    nums1[i] = nums2[i]  
