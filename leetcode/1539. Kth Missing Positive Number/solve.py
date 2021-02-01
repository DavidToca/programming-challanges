def infinite():
    n = 0
    while True:
        n+=1
        yield n


class Solution:

    def findKthPositive(self, arr: List[int], k: int) -> int:
        response = 0
        j = 0
        for i in infinite():
            if(j >= len(arr) or i != arr[j]):
                response = i
                k-=1
            else:
                j+=1

            if(k == 0):
                return response
            
