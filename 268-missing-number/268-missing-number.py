class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        nums.sort()
        if 0 not in nums:
            return 0
        for n in nums:
            if n+1 not in nums:
                return n+1