class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = 0
        for elem in nums:
            if elem:
                nums[index]=elem
                index+=1
        for i in range(index,len(nums)):
            nums[i]=0