class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        counters = Counter(s)
        countert = Counter(t)
        if counters == countert:
            return True
        else:
            return False