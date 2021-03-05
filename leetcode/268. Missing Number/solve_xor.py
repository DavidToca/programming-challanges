class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        missing_number = len(nums)
        for i in range(len(nums)):
            missing_number ^= nums[i] ^ i
    
        return missing_number