def upsidedown(A):
    astr = str(A)
    for i in range(len((astr))):
        if astr[i] == "6":
            astr = astr[:i] + '9' + astr[i+1:]
            return int(astr)
    return A


if __name__ == '__main__':
    print(upsidedown(99666)) # 99966
    print(upsidedown(696)) # 996
    print(upsidedown(699999999999999999)) # 99999999999999
