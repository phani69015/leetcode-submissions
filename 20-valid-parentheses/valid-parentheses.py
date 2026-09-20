class Solution:
    def isValid(self, s: str) -> bool:
        st = []
        d = {
            "}" : "{",
            "]" : "[",
            ")" : "("
        }

        for c in s:
            if c in d.values():
                st.append(c)
            elif c in d.keys():
                if not st or d[c]!=st.pop():
                    return False
        return not st
        