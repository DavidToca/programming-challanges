class Solution:
    def romanToInt(self, s: str) -> int:
        equivalence = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }
        
        numbers = list(s)
        
        last_number = None
        response = 0
        for numb in reversed(numbers):
            roman = equivalence.get(numb)
            
            if not last_number:
                response = roman
            elif last_number > roman:
                response -= roman
            else:
                response += roman
                
            last_number = roman
        return response