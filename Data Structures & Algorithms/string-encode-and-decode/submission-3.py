class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0: return "*0"
        elif len(strs) == 1: return strs[0]

        out = ""
        for i, s in enumerate(strs):
            out += s
            if i != len(strs) - 1:
                out += '\|'
        return out
    def decode(self, s: str) -> List[str]:
        if "\|" in s:
            strs = s.split("\|")
            return strs
        elif s == "*0":
            return []
        else:
            return [s]
