class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen = {}

        for i, current in enumerate(nums):
            needed = target - current
            if needed in seen:
                return [seen[needed], i]
            seen[current] = i

# enumerate() indice, value
# seen dictionary/hashmap