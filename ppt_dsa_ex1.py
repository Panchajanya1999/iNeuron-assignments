class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """
        low = 0
        high = x
        mid = (low + high) // 2

        while low <= high:
            if mid * mid == x:
                return mid
            elif mid * mid < x:
                low = mid + 1
            else:
                high = mid - 1
            mid = (low + high) // 2
        return int(math.floor(mid))

import math
sol = Solution()

# write assert checks to verify if your code is working correctly.
assert sol.mySqrt(4) == 2, "Test case failed"
assert sol.mySqrt(8) == 2, "Test case failed"