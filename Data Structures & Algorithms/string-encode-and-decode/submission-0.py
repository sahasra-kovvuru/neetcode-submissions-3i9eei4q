class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ''
        for s in strs:
            leng = str(len(s))
            res += leng + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            length = ''
            for k in range(i,len(s)):
                if s[k]=='#':
                    break
                length+=s[k] 
            size = int(length)
            start = k + 1
            word = ""
            for j in range(start, size+start):
                word+=s[j]
            res.append(word)
            i = (size+start)
        return res

                


