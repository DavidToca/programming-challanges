class Solution:
    def __init__(self):
        self.translation = {
            1: 'I',
            5: 'V',
            10: 'X',
            50: 'L',
            100: 'C',
            500: 'D',
            1000: 'M',
            4: 'IV',
            9: 'IX',
            40: 'XL',
            90: 'XC',
            400: 'CD',
            900: 'CM',
        }
        self.denominations = [1000,900,500,400,100,90,50,40, 10,9, 5,4,1]

    def intToRoman(self, num: int) -> str:        
        if num in self.translation:
            return self.translation[num]
        
        for d in self.denominations:
            
            if num - d == 0:
                num = num - d
                response = self.translation[d]
                return response
            if num - d > 0:
                num = num - d
                return self.translation[d] + self.intToRoman(num)
        return ""
