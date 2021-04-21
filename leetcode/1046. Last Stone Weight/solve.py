from heapq import heapify, heappop, heappush
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [x * -1 for x in stones]
        
        heapify(stones)
        
        while(len(stones) > 1):
            y = heappop(stones)
            x = heappop(stones)
            
            if x != y:
                y-=x
                heappush(stones, y)
        if not stones:
            return 0
        return stones[0] * -1