class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        if n == 1 or n == 2:
            return n
        
        prevPrev = 1
        prev = 2
        current = 0
        
        for step in range(3, n+1):
            # Calculate Number of Ways to Reach Current Step
            current = prevPrev + prev
            # Update Pointers for Next Step
            prevPrev = prev
            prev = current
        return current
    

#Test 1
#Input: n = 2
#Output: 2
n = 2
ob1 = Solution()
print("How many ways to climb to the top if steps taken = 2? ", ob1.climbStairs(n))

#Test 2
#Input: n = 3
#Output: 3
n = 3
ob1 = Solution()
print("How many ways to climb to the top if steps taken = 3? ", ob1.climbStairs(n))