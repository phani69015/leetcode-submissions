class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        # #bruteforce
        # for i in range(len(nums)):
        #     left = float("-inf") if i == 0 else nums[i-1]
        #     right = float("inf") if i == len(nums)-1 else nums[i+1]
        #     if left < nums[i] and right < nums[i]:
        #         return i
        # return len(nums)-1

        #optimal binary search 

        i = 0 
        j = len(nums) - 1
        while i < j:
            mid = (i+j)//2
            if i == j :
                return i
            if nums[mid] < nums[mid+1]:
                i = mid + 1
            else:
                j = mid 
        return i







        