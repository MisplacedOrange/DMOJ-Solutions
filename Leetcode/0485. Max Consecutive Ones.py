class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        cnt = 0
        maxcons = 0

        for i in range(len(nums)):
            if nums[i] == 1:
                cnt += 1
                maxcons = max(maxcons, cnt)
            else:
                cnt = 0
        return max(maxcons, cnt)