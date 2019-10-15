def RepeatedWord(str):
    dic = dict()
    li = str.split(" ")
    for l in li:
        if l not in dic.keys():
            dic[l] = l
        else:
            return l

if __name__ == "__main__":
    print(RepeatedWord("We work hard because hard work pays")) # hard
    print(RepeatedWord("We work Hard because hard work pays")) # ward
