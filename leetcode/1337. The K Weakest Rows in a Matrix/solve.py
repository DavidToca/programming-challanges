class Solution:
    
    def sort(self, counts):
        response = [x for x in range(len(counts))]
        next = 0
        
        for next in range(len(counts)):
            top = next
            for i in range(next, len(counts)):
                if(counts[i] < counts[top]):
                    top = i
                if(counts[i] == counts[top] and response[i] < response[top]):
                    top = i
            counts[next], counts[top] = counts[top], counts[next]
            response[next], response[top] = response[top], response[next]
        return response

    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        weaks = []

        for index, row in enumerate(mat):
            count = 0
            for soldier in row:
                if soldier == 0:
                    break
                count+=1
            weaks.append(count)
        
        response = self.sort(weaks)

        return response[:k]
