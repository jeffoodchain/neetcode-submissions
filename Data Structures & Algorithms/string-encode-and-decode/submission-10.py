class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0: return "0#"
        elif len(strs) == 1: return strs[0]
        out = ""
        for i, s in enumerate(strs):
            out += f"{len(s)}#"
            out += s
        # print(out)
        return out
    def decode(self, s: str) -> List[str]:
        if s == "0#":
            return []
        elif "#" not in s:
            return [s]
        elif len(s) == 1:
            return [s]
        res = []
        i = 0
        while i < len(s):
            last_pos = i
            while s[last_pos] != '#':
                last_pos += 1
            word_len = int(s[i:last_pos])
            # print(word_len)
            res.append(s[last_pos + 1: last_pos + word_len + 1])
            # print(last_pos)
            i = last_pos + 1 + word_len
        return res
