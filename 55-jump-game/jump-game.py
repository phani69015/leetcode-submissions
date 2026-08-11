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
        