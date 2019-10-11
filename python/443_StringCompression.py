class Solution:
    def compress(self, chars):
        count = 1
        res = 0
        cur = chars[0]
        n = len(chars)
        for i in range(n-1):
            if chars[i+1] != cur or i == n-2:
                if i == n-2:
                    count += 1
                chars[res] = cur
                res += 1
                cur = chars[i+1]

                if count == 1:
                    continue
                numField = count//10 +1
                print (count)
                for j in range(numField):
                    chars[res + numField - j-1] = str(count%10)
                    count //= 10
                res += numField
                count = 1
            else:
                count += 1
        print(chars)
        print(res)
        return res

if __name__ == "__main__":
    s = Solution()
    s.compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"])
