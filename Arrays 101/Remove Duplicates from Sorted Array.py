class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        d = {}
        for i in nums:
            d[i]=''
        nums.clear()
        nums.extend(d.keys())
        return len(nums)