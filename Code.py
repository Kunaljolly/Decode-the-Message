class Solution:
    def decodeMessage(self, key: str, message: str) -> str:
        t = ""
        r = ""
        l = {}
        for x in key:
            if x == " ":
                continue
            if x not in t:
                t += x
        c = 0
        for _ in list(t):
            if c < 26:
                l[_] = ascii_lowercase[c]
                c += 1
        l[" "] = " "
        for _ in message:
            r += l[_]
        return r


            
