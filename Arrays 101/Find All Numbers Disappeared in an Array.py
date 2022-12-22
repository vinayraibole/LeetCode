class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        result = [0]*len(nums)
        for i in nums:
            if not result[i-1]:
                result[i-1] = i
        return [i+1 for i in range(len(result)) if result[i]==0]