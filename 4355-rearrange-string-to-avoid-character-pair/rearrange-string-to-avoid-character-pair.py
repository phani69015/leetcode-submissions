from itertools import permutations

class Solution:

    #bruteforce  -> failed tests
    # def get_unique_permutations(self, text):
    #     return list({''.join(p) for p in permutations(text)})

    def rearrangeString(self, s: str, x: str, y: str) -> str:
    #     arr = self.get_unique_permutations(s)

    #     for perm in arr:
    #         seen_x = False
    #         valid = True

    #         for ch in perm:
    #             if ch == x:
    #                 seen_x = True
    #             elif seen_x and ch == y:
    #                 valid = False
    #                 break

    #         if valid:
    #             return perm

    #optimal - > 
        left = ""
        right = ""
        middle = ""

        for i in s:
            if i == x:
                right+=i
            elif i==y:
                left+=i
            else:
                middle+=i


        return left+middle+right


