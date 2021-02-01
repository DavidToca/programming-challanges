class Solution:

    def findKthPositive(self, arr: List[int], k: int) -> int:
        response = 0
        j = 0
        i=1
        while k!=0:
            if(j >= len(arr) or i != arr[j]):
                response = i
                k-=1
            else:
                j+=1
            i+=1
        return response
            
