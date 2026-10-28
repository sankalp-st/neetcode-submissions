class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_h = {}
        t_h = {}
        for i in s:
            if i in s_h:
                s_h[i]+=1
            else:
                s_h[i] = 1

        for i in t:
            if i in t_h:
                t_h[i]+=1
            else:
                t_h[i] = 1

        return s_h == t_h 