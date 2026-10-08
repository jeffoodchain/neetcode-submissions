class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_list = []
        t_list = []
        if len(s) != len(t):
            return False
        for char in s:
            s_list.append(char)
        for char in t:
            t_list.append(char)
        s_list = sorted(s_list)
        t_list = sorted(t_list)
        return s_list == t_list