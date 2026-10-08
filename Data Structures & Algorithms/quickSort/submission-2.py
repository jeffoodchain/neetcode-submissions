# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def quickSort(self, pairs: List[Pair]) -> List[Pair]:
        def _quickSort(arr, s, e):
            if (e - s + 1) <= 1:
                return arr

            pivot = arr[e].key
            left = s

            for i in range(s, e+1):
                if arr[i].key < pivot:
                    arr[left], arr[i] = arr[i], arr[left]
                    left += 1
            
            arr[left], arr[e] = arr[e], arr[left]

            _quickSort(arr, s, left-1)
            _quickSort(arr, left+1, e)
            
            return arr
        return _quickSort(pairs, 0, len(pairs)-1)

