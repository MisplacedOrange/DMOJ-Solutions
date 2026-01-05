class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:

        subt= 0
        subs = 0

        while subs < len(s) and subt < len(t):
            if s[subs] == t[subt]:
                subs += 1
            subt += 1
        return subs == len(s)
        # REVIEW THIS ONE
        