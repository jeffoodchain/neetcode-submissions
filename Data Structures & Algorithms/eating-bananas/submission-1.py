class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l, r = 1, max(piles)
        res = r

        while l < r:
            k = (l + r) // 2

            totalHr = 0
            for pile in piles:
                totalHr += math.ceil(pile / k)
            
            if totalHr <= h:
                res = k
                r = k
            else:
                l = k + 1
        return res