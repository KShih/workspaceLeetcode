def repeated3ormore(str):
    ret, i = [], 1
    while i < len(str):
        if str[i] == str[i-1]:
            start = i-1
            count = 1
            while i < len(str) and str[i] == str[i-1]:
                count, i = count+1, i+1
            end = i-1
            if count >= 3:
                ret.append((start, end))
        else:
            i += 1
    return ret

if __name__ == '__main__':
    print(repeated3ormore("abbbcccc"))
    print(repeated3ormore("a"))
    print(repeated3ormore("bbb"))
    print(repeated3ormore("abbccccbccc"))
    print(repeated3ormore(""))
