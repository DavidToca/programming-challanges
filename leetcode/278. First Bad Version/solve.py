# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        left = 0
        right = n - 1
        while right - left > 1:
            middle = left + (right - left) // 2
            if isBadVersion(middle + 1):
                right = middle
            else:
                left = middle
        if isBadVersion(left + 1):
            return left + 1
        return right + 1
