class Solution:
    def trap(self, height: List[int]) -> int:
        #bruteforce 
        # k = len(height)
        # lm = [0]*k
        # rm = [0]*k
        # w = 0
        # lmkey = 0
        # rmkey = 0
        # for i in range(len(height)-1):
        #     var = max(lmkey,height[i]) 
        #     lmkey = var 
        #     lm[i] = var 
        
        # for i in range(len(height)-1,-1,-1):
        #     var2 = max(rmkey,height[i]) 
        #     rmkey = var2 
        #     rm[i] = var2 

        # for i in range(len(height)-1):
        #     w+=(min(lm[i],rm[i])-height[i]) 
        # return w

        #optimal 

        lm = rm = 0
        k = len(height)
        i = 0
        j = k - 1 
        w = 0

        while i<j:
            lm = max(lm , height[i])
            rm = max(rm, height[j])

            if lm < rm :
                w += lm - height[i] 
                i+=1
            else:
                w+= rm - height[j]
                j-=1
        return w










        