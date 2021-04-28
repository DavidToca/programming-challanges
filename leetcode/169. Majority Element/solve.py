class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        elements = defaultdict(lambda: 0)
        threshold = len(nums) // 2 + 1
        
        for num in nums:
            elements[num] += 1
        
        for element, count in elements.items():
            if count >= threshold:
                return element
        return None
