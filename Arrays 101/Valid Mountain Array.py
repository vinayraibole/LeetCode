class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr)<3:
            return False
        elif arr[-1] == max(arr) or arr[0] == max(arr):
            return False
        else:
            m = arr[0]
            flag = 1
            for i in arr[1:]:
                if flag == 1 and i>m:
                    m = i
                elif flag == 1 and i<m:
                    flag = 0
                    m = i
                elif flag == 0 and i<m:
                    m = i
                else:
                    return False
            return True