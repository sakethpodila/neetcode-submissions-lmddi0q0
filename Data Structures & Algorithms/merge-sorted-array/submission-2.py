class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # zero_p = m
        # i = j = 0
        # while i < len(nums1) and j < len(nums2):
        #     if nums2[j] > nums1[i] and nums1[i] != 0:
        #         i += 1
        #         continue
        #     elif nums1[i] == 0:
        #         nums1[i] = nums2[j]
        #     else:
        #         first_i = i 
        #         for t in range(zero_p - i):
        #             nums1[zero_p], nums1[i] = nums1[i], nums1[zero_p]
        #             i += 1
        #         print(f'{nums1} after swapping the zeros')
        #         nums1[first_i] = nums2[j]
        #         zero_p += 1
        #         print(f'{nums1} after changing the index')
        #     i = 0
        #     j += 1

        r1 = len(nums1) - 1
        l1= m - 1 
        r2 = len(nums2) - 1

        while r2 >= 0 and l1 >= -1:
            if l1 == -1 or nums2[r2] >= nums1[l1]:
                nums1[r1] = nums2[r2]
                r1 -= 1
                r2 -= 1
            else:
                nums1[r1] = nums1[l1]
                l1 -= 1
                r1 -= 1
                
            
        


            


