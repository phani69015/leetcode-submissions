class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums)==1:
            return [nums]

        permutations = []

        for i,value in enumerate(nums):
            sending_array = nums[:i] + nums[i+1:]

            for next_value in self.permute(sending_array):
                permutations.append([value]+next_value) 
        return permutations
        