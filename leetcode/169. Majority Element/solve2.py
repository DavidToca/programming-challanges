class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        
        current_count = 0
        current_numb = nums[0]
        max_element_count = 0
        max_number = nums[0]

        for num in nums:
            if num == current_numb:
                current_count+=1
            else:
                current_count = 1
                current_numb = num
            
            if max_element_count < current_count:
                max_element_count = current_count
                max_number = num
        return max_number