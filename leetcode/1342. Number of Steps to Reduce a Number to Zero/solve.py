class Solution:
    def pre_calculate(self):
        max_number = 10**6
        
        solutions = {
            0: 0,
            1: 1,
        }
        
        for numb in range(2, max_number+1):
            
            reduce_numb = numb
            ops = 0
            while(numb not in solutions):
                
                if reduce_numb%2==0:
                    reduce_numb /= 2
                else:
                    reduce_numb -= 1
                ops+=1
                
                if reduce_numb in solutions:
                    solutions[numb] = solutions[reduce_numb] + ops
        return solutions       

    # def __init__(self):
        #self.solutions = self.pre_calculate()
        
    def numberOfSteps (self, num: int) -> int:
        steps = 0
        while(num != 0):
            if num%2 == 0:
                num/=2
            else:
                num-=1
            steps+=1
        return steps