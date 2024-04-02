class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                left = mid + 1
            else:
                right = mid - 1
        
        return left
        

# Test 1
# Input: nums = [1,3,5,6], target = 5
input_list = [1,3,5,6]
ob1 = Solution()
print("The first test result is: ", ob1.searchInsert(input_list, 5))

# Test 2
# Input: nums = [1,3,5,6], target = 2
input_list = [1,3,5,6]
ob1 = Solution()
print("The second test result is: ", ob1.searchInsert(input_list, 2))

# Test 3
# Input: nums = [1,3,5,6], target = 7
input_list = [1,3,5,6]
ob1 = Solution()
print("The third test result is: ", ob1.searchInsert(input_list, 7))