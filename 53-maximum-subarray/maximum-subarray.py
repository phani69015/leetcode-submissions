class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currSum = 0
        maxSum = -inf
        for i in range(0,len(nums)):
            currSum = max(nums[i] , currSum+nums[i])
            maxSum = max(currSum,maxSum)
        return maxSum 

            
        