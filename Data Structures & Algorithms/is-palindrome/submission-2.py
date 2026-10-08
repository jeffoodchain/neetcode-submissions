class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = ""
        res = res.join(c for c in s if c.isalnum())
        l,r = 0, len(res) - 1
        while l < r:
            if res[l].lower() != res[r].lower():
                return False
            l += 1
            r -= 1
        return True