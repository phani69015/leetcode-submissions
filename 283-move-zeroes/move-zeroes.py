class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = None
        for i in range(len(nums)):
            if nums[i]==0:
                j = i
                break 
        if j is None:
            return
        for k in range(j+1,len(nums)):
            if nums[k]!=0:
                nums[j],nums[k]=nums[k],nums[j] 
                j+=1
        
        

            
        
        