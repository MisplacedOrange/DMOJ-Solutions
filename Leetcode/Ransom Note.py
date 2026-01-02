class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        counterM = Counter(magazine)
        counterR = Counter(ransomNote)

        if counterM >= counterR:
            return True
        else:
            return False

