# @param {Integer} x
# @return {Integer}
def reverse(x)
    
    min_int = -(2**31)
    max_int = 2**31 - 1
    
    a = x.to_s

    sign = ""

    if a.start_with?("-")
        a = a[1..-1]
        sign = "-"
    end

    a = a.reverse

    a = sign + a

    response = a.to_i

    if response.between?(min_int, max_int)
        return response
    end
    return 0

    
end