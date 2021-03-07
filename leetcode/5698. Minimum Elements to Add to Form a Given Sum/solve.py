class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        so_far = sum(nums)
        
        if so_far == goal:
            return 0
        
        left = goal - so_far
        
        times = int(abs(left) // limit)
        
        if abs(left) % limit == 0:
            times = int(abs(left) // limit)
        else:
            times = int(abs(left) // limit) + 1

        return times