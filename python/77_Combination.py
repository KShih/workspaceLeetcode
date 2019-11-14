class Solution:
    def combine(self, n: int, k: int):
        def find_comb(idx, comb):
            if len(comb) == k:
                ret.append(comb[:])
                return

            for i in range(idx, n + 1):
                comb.append(i)
                find_comb(i + 1, comb)
                comb.pop()

        ret = []
        for i in range(1, n + 1):
            find_comb(i+1, [i])

        return ret

if __name__ == "__main__":
    s = Solution()
    print(s.combine(3,3))