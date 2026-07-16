class Solution:
    def subarraySum(self, nums: List[int], target: int) -> int:
        #worst solution
        # k = len(nums)
        # res = 0
        # for i in range(k):
        #     currSum = 0
        #     for j in range(i,k):
        #         currSum+=nums[j]
        #         if currSum==target:
        #             res+=1 
        # return res

        #optimal 1 sliding window

        # i = 0
        # currSum = 0
        # count = 0

        # for j in range(len(nums)):
        #     currSum += nums[j]

        #     while currSum > target:
        #         currSum -= nums[i]
        #         i += 1

        #     if currSum == target:
        #         count += 1
        #         currSum -= nums[i]
        #         i += 1

        # return count
            

        #optimal 2 prefix sum and dict

        prefixCount = defaultdict(int)
        prefixCount[0] = 1

        currSum = 0
        count = 0

        for num in nums:
            currSum += num

            count += prefixCount[currSum - target]

            prefixCount[currSum] += 1

        return count



                
        