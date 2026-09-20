class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        l = 0
        currs = 0
        mini = float("inf")

        for r in range(len(nums)):

            currs += nums[r]

            while currs >= target:

                mini = min(mini,r-l+1)
                currs-=nums[l]
                l+=1

        if mini == float("inf"):
            return 0
        return mini
        