class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        l = 1
        r = max(piles)
        ans = r
        while l<=r:
            mid = (l+r)//2
            ch = sum([ceil(p/mid) for p in piles])
            if ch <= h:
                ans = mid
                r = mid - 1
            else:
                l = mid+1
        return ans

             
                






        