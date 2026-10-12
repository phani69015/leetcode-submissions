class Solution:
    def reorganizeString(self, s: str) -> str:
        freq = [0] * 26
        n = len(s)
        for i in s:
            idx = ord(i) - ord('a')
            freq[idx]+=1
        max_f = max(freq)
        max_fi = freq.index(max_f)
        max_c = chr(max_fi + ord('a'))
        
        if max_f > (n+1) // 2:
            return ""

        res = [""]*n

        pos = 0
        while freq[max_fi] > 0:
            res[pos]=max_c
            pos+=2
            freq[max_fi]-=1

        for ci in range(26):
            while freq[ci] > 0:
                if pos >=n:
                    pos= 1
                res[pos] = chr(ci+ord('a'))
                pos+=2
                freq[ci]-=1

        return "".join(res)

        