class Solution(object):
    def merge(self, nums1, m, nums2, n) -> None:
        
        i: int = int(m - 1)
        j: int = int(n - 1)
        k: int = int(m + n - 1)
        
        while (k >= 0):
            if i>=0 and j>=0:
                if(nums2[j] > nums1[i]):
                    nums1[k] = nums2[j]
                    k -= 1
                    j -= 1
                else:
                    nums1[k] = nums1[i]
                    k -= 1
                    i -= 1
            elif j >= 0:
                nums1[k] = nums2[j]
                k -= 1
                j -= 1
            else:
                break
        return nums1

#test 1   
input1: list[int] = [1,2,3,0,0,0]
m = 3
input2: list[int] = [2,5,6]
n = 3
ob1: Solution = Solution()
result = ob1.merge(input1, m, input2, n)
print("First case is: ", result)
   

#test 2
input1 = [1]
m = 1
input2 = []
n = 0
ob1: Solution = Solution()
result = ob1.merge(input1, m, input2, n)
print("Second case is: ", result)

#test 3
input1 = [0]
m = 0
input2 = [1]
n = 1
ob1: Solution = Solution()
result = ob1.merge(input1, m, input2, n)
print("Third case is: ", result)
