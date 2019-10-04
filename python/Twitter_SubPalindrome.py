class Solution:
    def countSubstrings(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        ret = set()
        def checkLR(s, l, r, ret):
            count = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                count += 1
                l -= 1; r += 1
                ret.add(s[l+1:r])

        for i in range(len(s)):

            # odd case
            checkLR(s,i,i,ret)

            # even case
            checkLR(s,i,i+1,ret)

        return ret

if __name__ == "__main__":
    s = Solution()
    print(s.countSubstrings("aabaa"))
    print(s.countSubstrings("aabbaa"))
