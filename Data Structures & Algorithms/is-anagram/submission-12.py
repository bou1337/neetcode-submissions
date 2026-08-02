class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        v1  = sorted(s)
        v2 = sorted(t)
        return v1==v2
    