class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        s = sorted(list(set(nums)))
        if len(s)<3:
            return s[-1]
        return s[-3]