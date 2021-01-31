# @param {String} s
# @return {Boolean}
def is_valid(s)
    

    stack = []

    brackets = {
        ')' => '(',
        '}' => '{', 
        ']' => '['
    }

    s.each_char do |c|
        
        if brackets.include? c
            
            if stack.empty?
                return false
            end

            top = stack.pop

            if brackets[c] != top
                return false
            end

        else
            stack << c
        end 

    end

    stack.empty?
end