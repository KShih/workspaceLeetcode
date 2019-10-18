def RepeatedWord(str):
    dic = dict()
    replacestr = ["-", ".", ",", ":", ";", "\t"]  # replace special character in response
    for i in replacestr:
        str = str.replace(i, "")
    print(str)
    li = str.split(" ")
    print(li)
    for l in li:
        if l == "":
            continue
        if l not in dic.keys():
            dic[l] = l
        else:
            return l

if __name__ == "__main__":
    print(RepeatedWord("We, work hard because hard work pays")) # hard
    print(RepeatedWord("We work Hard because hard work pays")) # ward
    print(RepeatedWord("that                 that occurs sometimes"))
