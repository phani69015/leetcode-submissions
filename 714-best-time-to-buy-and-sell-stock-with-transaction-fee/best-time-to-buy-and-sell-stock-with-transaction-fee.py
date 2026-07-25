class Solution:
    def maxProfit(self, prices: List[int], fee: int) -> int:
        d={}
        def dfs(day,holding):
            if (day,holding) in d:
                return d[(day,holding)]
            if day==len(prices):
                return 0
            if holding:
                sell = (prices[day]-fee)+dfs(day+1,False)
                keep = dfs(day+1,True)
                ans = max(sell,keep)
            else:
                buy = -prices[day]+dfs(day+1,True)
                skip = dfs(day+1,False)
                ans =  max(buy,skip)
            d[(day,holding)] = ans
            return ans
        return dfs(0,False)
        