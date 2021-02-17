# @param {Integer} num
# @return {Integer}
def number_of_steps (num)
    steps = 0
    
    while num != 0
        
        if num%2==0 then
            num /=2
        else
            num -=1
        end
        steps+=1
    end
    return steps
end