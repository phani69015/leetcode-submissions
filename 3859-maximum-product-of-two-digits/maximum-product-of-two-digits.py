class Solution:
    def maxProduct(self, n: int) -> int:
        digits = []
        while n>0:
            digits.append(n%10)
            n = n//10
        
        if len(digits)==2:
            return digits[0]*digits[1]

        if len(digits)==1:
            return n
        digits.sort()

        return digits[-1]*digits[-2]



        