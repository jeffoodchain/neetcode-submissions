# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def mergeSort(self, pairs: List[Pair]) -> List[Pair]:
        # inner function for recursion

        def _mergeSort(arr: List[Pair], start: int, end: int):
            # while e == s
            if end - start + 1 <= 1:
                return arr # basic case
            mid = (start + end) // 2

            # This part separate the arr in to left and right
            _mergeSort(arr, start, mid)
            _mergeSort(arr, mid + 1, end)

            # This part merges and sorts the arr
            merge(arr, start, mid, end)

            return arr

        def merge(arr: List[Pair], s: int, m: int, e: int):
            L = arr[s : m + 1]
            R = arr[m + 1 : e + 1]

            i, j = 0, 0 # pointers pointing to curr ele
            k = s       # index of original array
            
            while i < len(L) and j < len(R):
                if L[i].key <= R[j].key:
                    arr[k] = L[i]
                    i += 1
                else:
                    arr[k] = R[j]
                    j += 1
                k += 1
            
            while i < len(L):
                arr[k] = L[i]
                i += 1
                k += 1
            
            while j < len(R):
                arr[k] = R[j]
                j += 1
                k += 1
            
            return arr

        return _mergeSort(pairs, 0, len(pairs)-1)