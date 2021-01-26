# @param {Integer} x
# @return {Boolean}
def is_palindrome(x)
    return x.to_s == x.to_s.reverse
end