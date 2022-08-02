class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        arr = set(nums)
        result = []
        counter = 1
        for i in range(len(nums)):
            if counter not in arr:
                result.append(counter)
            counter += 1
        return result