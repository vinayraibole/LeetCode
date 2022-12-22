class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        if 0 in arr:
            i=0
            while i<=len(arr)-1:
                if not arr[i]:
                    arr.insert(i,0)
                    i+=1
                    arr.pop()
                i+=1