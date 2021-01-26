# @param {String} s
# @return {Integer}
def roman_to_int(s)
    equivalence = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000,
    }
     
    s = s.reverse
    last_number = -1
    response = 0
    s.split('').each { |c|
        roman = equivalence[c.to_sym]
        
        if last_number > roman then
            response -=roman
        else
            response += roman
        end
        last_number = roman
    }
    return response
    
end