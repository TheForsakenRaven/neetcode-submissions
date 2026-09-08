class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        max = 0
        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[j] > max:
                    max = arr[j]
            arr[i] = max
            max = 0
        arr[-1] = -1

        return arr