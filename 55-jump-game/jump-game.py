class Solution:
    def canJump(self, nums: List[int]) -> bool:
        gas = nums[0]
        for i in range(1,len(nums)):
            gas-=1
            if gas < 0:
                return False
            if nums[i]>gas:
                gas = nums[i]
        return True

        #plain dfs

        # def dfs(i):
        #     if i >= len(nums)-1:
        #         return True
        #     for jump in range(1,nums[i]+1):
        #         if dfs(i+jump):
        #             return True
        #     return False
        # return dfs(0)

        #dfs with memoization
        # memo = {}
        # def dfs(i):
        #     if i >= len(nums)-1:
        #         return True
        #     if i in memo:
        #         return memo[i]
        #     for jump in range(1,nums[i]+1):
        #         if dfs(i+jump):
        #             memo[i]=True
        #             return True
        #     memo[i]=False
        #     return False
        # return dfs(0)

        