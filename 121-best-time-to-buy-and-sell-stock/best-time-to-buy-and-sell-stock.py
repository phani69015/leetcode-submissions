class Solution:
    def maxProfit(self, arr: List[int]) -> int:
        if not arr:
            return 0
        minBuy = arr[0]
        profit = 0
        n=len(arr)
        for i in range(1,n):
            currProfit = arr[i]-minBuy
            minBuy = min(minBuy,arr[i])
            profit = max(profit,currProfit)
        return profit
        