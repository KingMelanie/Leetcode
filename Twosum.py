class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        dictionary = {}
        
        for i in range(len(nums)):
            secondNumber = target-nums[i]
            if(secondNumber in dictionary.keys()):
                secondIndex = nums.index(secondNumber)
                if(i != secondIndex):
                    return sorted([i, secondIndex])
                
            dictionary.update({nums[i]: i})



# Step 1: Test twoSum() with 
#             Input: nums = [2,7,11,15], target = 9
input_list = [2,7,11,15]
ob1 = Solution()
print(ob1.twoSum(input_list, 9))

#  Step2 : Test twoSum() with 
#             Input: nums = [3,2,4], target = 6
input_list = [3,2,4]
ob1 = Solution()
print(ob1.twoSum(input_list, 6))

# Step 3: Test twoSum() with
#             nums = [3,3], target = 6
input_list = [3, 3]
ob1 = Solution()
print(ob1.twoSum(input_list, 6))

