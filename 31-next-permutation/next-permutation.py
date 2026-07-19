class Solution:
    def nextPermutation(self, nums: List[int]) -> None:

        n = len(nums)

        pivot = -1

        # find pivot
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i+1]:
                pivot = i
                break

        # no pivot means descending order
        if pivot == -1:
            nums.reverse()
            return

        # find next greater element
        for i in range(n-1, pivot, -1):
            if nums[i] > nums[pivot]:
                nums[i], nums[pivot] = nums[pivot], nums[i]
                break

        # reverse suffix
        nums[pivot+1:] = reversed(nums[pivot+1:])