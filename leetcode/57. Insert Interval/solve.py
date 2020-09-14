class Solution:
    
    def is_collision(self, current: List[int], new_interval: List[int]):
        a, b = current
        c, d = new_interval
        
        return c <= b and d >= a
    
    def is_behind(self, current: List[int], new_interval: List[int]):
        a, b = current
        c, d = new_interval
        
        return a > c and a > d
        
    def merge(self, current: List[int], new_interval: List[int]):
        minimum = min(current[0], new_interval[0])
        maximum = max(current[1], new_interval[1])
        return [minimum, maximum]

    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        i = 0
        inserted = False
        while(i < len(intervals)):
            current = intervals[i]

            if not self.is_collision(current, newInterval):
                if self.is_behind(current, newInterval):
                    intervals.insert(i, newInterval)
                    inserted = True
                    break
                i+=1
            else:
                while(i < len(intervals)):
                    current = intervals[i]
                    if self.is_collision(current, newInterval):
                        newInterval = self.merge(current, newInterval)
                        del intervals[i]
                    else:
                        break
                intervals.insert(i, newInterval)
                inserted = True
                break
        
        if not inserted:
            intervals.append(newInterval) 

        return intervals
