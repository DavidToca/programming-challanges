class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        if len(nums) == 0:
            return 0

        iterator = 1
        while (iterator - 1) >= 0 and iterator < len(nums):
            if nums[iterator - 1] == nums[iterator]:
                del nums[iterator]
            else:
                iterator += 1

        return len(nums)