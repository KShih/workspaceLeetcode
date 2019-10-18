from collections import Counter

def MostCommonSubstring(s, minLength, maxLength, maxUnique):
    dic = Counter()
    n = len(s)
    for i in range(n):

        if minLength < n-i:
            maxB = maxLength
        else:
            maxB = n-1

        for j in range(minLength,maxB+1):
            if i+j <= n:
                substring = s[i:i+j]
                distinctCount = len(set(substring))

                if len(substring) >= minLength and len(substring) <= maxLength and distinctCount <= maxUnique:
                    if substring in dic.keys():
                        dic[substring] += 1
                    else:
                        dic[substring] = 1
    if len(dic) == 0:
        return 0
    return dic.most_common(1)[0][1]


if __name__ == "__main__":
    print(MostCommonSubstring("abcde", 2, 4, 3))
    print(MostCommonSubstring("abcde", 2, 4, 26))
    print(MostCommonSubstring("ababab", 2, 3, 4))
    print(MostCommonSubstring("aaaaaa", 2, 3, 4))
