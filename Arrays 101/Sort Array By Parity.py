class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        l1 = []
        l2 = []
        for i in nums:
            if not i%2:
                l1.append(i)
            else:
                l2.append(i)
        
        return l1+l2