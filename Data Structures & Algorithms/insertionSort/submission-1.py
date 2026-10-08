# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:
        res = []
        if len(pairs) == 0:
            return res

        for i in range(1, len(pairs)):
            cur = []
            for p in pairs:
                cur.append(p)
            res.append(cur)
            j = i - 1
            while j >= 0 and pairs[j+1].key < pairs[j].key:
                pairs[j+1], pairs[j] = pairs[j], pairs[j+1] 
                j -= 1
        res.append(pairs)
        return res