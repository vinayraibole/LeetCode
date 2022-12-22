class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max_elem = arr[-1]
        arr[-1] = -1
        for i in range(len(arr)-2,-1,-1):
            temp = max_elem
            if arr[i]>max_elem:
                temp = arr[i]
            arr[i] = max_elem
            max_elem = temp
        return arr