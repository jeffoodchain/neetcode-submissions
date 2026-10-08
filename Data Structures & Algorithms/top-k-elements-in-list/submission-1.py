class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(int)
        for i, n in enumerate(nums):
            freq[n] += 1

        res = [0] * k
        # find the maximum of the value
        def getMaxKey(fq: dict) -> int:
            maxK = 0
            maxVal = 0
            for key in fq:
                val = fq[key]
                if val > maxVal:
                    maxK = key
                    maxVal = val
            return maxK
        
        for i in range(k-1, -1, -1):
            print(i)
            res[i] = getMaxKey(freq)
            freq[res[i]] = 0
        return res