from collections import Counter
def steps(binary):
    lead = 0
    for i in range(len(binary)):
        if binary[i] == "1":
            lead = i
            break
        if i == len(binary)-1: # input = 00000
            return 0

    li = list(binary[lead:])
    dic = Counter(li)
    return dic['1']*2 + dic['0'] - 1


if __name__ == "__main__":
    print(steps("010100"))
