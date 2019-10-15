from collections import Counter

def MostCommonSubstring(str1, nl, xl, xu):
    dic = Counter()
    n = len(str1)
    for i in range(n):

        if nl < n-i:
            maxB = xl
        else:
            maxB = n-1

        for j in range(nl,maxB+1):
            if i+j <= n:
                substring = str1[i:i+j]
                distinctCount = len(set(substring))

                if len(substring) >= nl and len(substring) <= xl and distinctCount <= xu:
                    if substring in dic.keys():
                        dic[substring] += 1
                    else:
                        dic[substring] = 1
    print(dic)
    return dic.most_common(1)[0][1]


if __name__ == "__main__":
    print(MostCommonSubstring("abcde", 2, 4, 3))
    print(MostCommonSubstring("abcde", 2, 4, 26))
    print(MostCommonSubstring("ababab", 2, 3, 4))
