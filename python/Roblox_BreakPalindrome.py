def breakPalind(str):
    i = 0
    while isPalind(str):
        ch = chr(ord(str[i]) + 1)
        str = ch + str[1:]
        if not isPalind(str):
            return str
        elif ch == 'z':
            i += 1
            if i >= len(str):
                return "Unable to find the way to Break Palind"

def isPalind(str):
    return str == str[::-1]

if __name__ == "__main__":
    print(breakPalind("aabbaa"))
    print(breakPalind("aabaa"))
