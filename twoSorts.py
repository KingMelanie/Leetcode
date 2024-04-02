class Solution:
    def sortColors(a, nums: list[int]) -> None:
        low = 0
        mid = 0
        high = len(nums) - 1
       
        # Iterate 
        while mid <= high:
            # If the element is 0
            if nums[mid] == 0:
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            # If the element is 1
            elif nums[mid] == 1:
                mid += 1
            # If the element is 2
            else:
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
        return nums

def main():

    arr = Solution()

    print(arr.sortColors([2, 0, 2, 1, 1, 0]))

if __name__ == "__main__":
    main()
