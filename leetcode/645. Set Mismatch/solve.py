class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        repeat_number = None
        seen_numbers = {}
        
        nums.sort()
        for i in range(len(nums)-1):
            seen_numbers[nums[i]] = True
            seen_numbers[nums[i+1]] = True
            if(nums[i] == nums[i+1]):
                repeat_number = nums[i]
        
        for i in range(1, len(nums)+1):
            if i not in seen_numbers:
                return [repeat_number, i]
        return []
