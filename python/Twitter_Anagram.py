from collections import Counter

# the misunderstand one
def anagram(input):
    if len(input)%2 != 0:
        return -1

    li = list(input)
    dic = Counter(li)
    count = 0
    for i in range(len(dic)):
        count += (dic.most_common()[i][1]) % 2
    return count//2

# the correct one
def anagram2(input):
    s = input
    l = len(s)
    if l % 2 == 1:
        return -1
    else:
        count = 0
        s1, s2 = Counter(s[:l//2]), Counter(s[l//2:])
        for char in s2:
            current = s2[char] - s1.get(char,0)
            if current > 0:
                count += current
        print(count)



if __name__ == '__main__':
#    print(anagram("aaabbbcc"))#1
    print(anagram("aaaabbbccd"))#1
    print(anagram("xaxbbbxx"))#1
    print(anagram("xxxbba"))#1
    print(anagram("aaabbb")) #1
    print(anagram("mnop")) #2
    print(anagram("ab")) #1
    print(anagram("xyyx")) #0
