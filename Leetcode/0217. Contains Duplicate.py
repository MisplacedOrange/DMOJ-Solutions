class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        counter = Counter(nums)
        for count in counter.values():
            if count > 1:
                return True
        return False
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return Counter(nums).most_common(1)[0][1]>1