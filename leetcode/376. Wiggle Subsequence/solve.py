class Solution:
    def wiggleMaxLength(self, nums: List[int]) -> int:
        max_length = 1
        last_symbol = ''

        for i in range(len(nums) - 1):
            if nums[i] == nums[i + 1]:
                continue
            elif nums[i] > nums[i + 1]:
                current_symbol = '>'
            else:
                current_symbol = '<'

            if last_symbol != current_symbol:
                max_length += 1

            last_symbol = current_symbol

        return max_length