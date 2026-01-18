class Solution:
    def appendCharacters(self, s: str, t: str) -> int:

        foo = 0
        ree = 0

        while foo < len(s) and ree < len(t):
            if s[foo] == t[ree]:
                ree +=1
            foo += 1
        return len(t) - ree

# first medium,