class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        se = set()
        l = 0
        maxl = 0
        for r in range(len(s)):
            while s[r] in se:
                se.remove(s[l])
                l+=1
            se.add(s[r])
            maxl = max(maxl,r-l+1)
        return maxl

        