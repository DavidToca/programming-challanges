from collections import defaultdict
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        answer = []
        if len(s) <=10:
            return answer
             
        options = (len(s) - 10) + 1
        
        d = defaultdict(lambda:0)
        
        for i in range(options):
            substring = s[i:i+10]
            d[substring] +=1
        
        for key, value in d.items():
            if(value > 1):
                answer.append(key)
        return answer
