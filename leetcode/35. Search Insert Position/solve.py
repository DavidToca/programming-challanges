class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        for index, numb in enumerate(nums):
            if numb >= target:
                return index

        return len(nums)
