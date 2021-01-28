# @param {String[]} strs
# @return {String}
def longest_common_prefix(strs)
    if strs.length == 0 then
        return ""
    end

    if strs.length == 1 then
        return strs[0]
    end

    response = ""

    first_word = strs[0]

    first_word.split("").each_with_index do | letter, index|
        
        strs.each do |word| 
            if index >= word.length then
                return response
            end
            if letter != word[index] then
                return response
            end
        end

        response += letter

    end
    return response

end