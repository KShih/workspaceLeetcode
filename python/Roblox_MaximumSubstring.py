def maxSubstring(s):
    mxChar = sorted(s, reverse=True)[0]
    cand = []
    for i in range(len(s)):
        if s[i] == mxChar:
            cand.append(s[i:])
    return(sorted(cand, reverse=True)[0])

if __name__ == "__main__":
    print(maxSubstring("banana"))
    print(maxSubstring("cacbcbcb"))
    print(maxSubstring("baca"))
