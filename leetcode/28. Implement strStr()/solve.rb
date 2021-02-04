# @param {String} haystack
# @param {String} needle
# @return {Integer}
def str_str(haystack, needle)
    if needle == ""
        return 0
    end
    
    response = haystack.index(needle)
    
    if response.nil?
        return -1
    end
    return response
end