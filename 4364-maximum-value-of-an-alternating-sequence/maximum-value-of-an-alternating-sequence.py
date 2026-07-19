class Solution:
    def maximumValue(self, n: int, s: int, m: int) -> int:
        # #bruteforce
        # self.ans = s

        # def dfs(index, prev, curr_max, expect_greater):
        #     if index == n:
        #         self.ans = max(self.ans,curr_max)
        #         return 

        #     for nxt in range(prev-m,prev+m+1):
        #         if expect_greater:
        #             if nxt<=prev:
        #                 continue
        #         else:
        #             if nxt>=prev:
        #                 continue
        #         dfs(
        #             index +1,
        #             nxt,
        #             max(curr_max,nxt),
        #             not expect_greater
        #         )
        
        # dfs(1,s,s,True)
        # dfs(1,s,s,False)
        # return self.ans

        if n<2:
            return s
        else:
            return s+m+(((n//2)-1)*(m-1))
        
