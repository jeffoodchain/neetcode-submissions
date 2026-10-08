class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        ptr_1 = 0
        ptr_2 = 1
        n = len(numbers)
        print(n)
        while (ptr_1 <= n-1):
            while (ptr_2 <= n-1):
                if (numbers[ptr_1] + numbers[ptr_2] == target):
                    return [ptr_1 + 1, ptr_2 + 1]
                ptr_2 += 1
            ptr_1 += 1
            ptr_2 = ptr_1 + 1