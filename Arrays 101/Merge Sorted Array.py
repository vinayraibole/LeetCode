class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if not n:
            pass
        elif not m:
            for i in range(n):
                nums1[i]=nums2[i]
        else:
            x = sorted(nums1[:m]+nums2)
            for i in range(len(x)):
                nums1[i]=x[i]