from collections import Counter

def getUniqueUserIdSum(arr):
    idTable = Counter(arr)
    lowestNum = 1
    returnSum = 0
    for i in arr:
        if idTable[i] > 1:
            lowestNum = i + 1
            while idTable[lowestNum] > 0:
                lowestNum += 1
            idTable[lowestNum] += 1
            idTable[i] -= 1
            returnSum += lowestNum
            print lowestNum
        else:
            returnSum += i
            print i
    return returnSum


if __name__ == '__main__':
    #print(getUniqueUserIdSum([3,2,1,2,7]))
    #print(getUniqueUserIdSum([1,1,1,1,1]))
    #print(getUniqueUserIdSum([1,2,3,4,5]))
    #print(getUniqueUserIdSum([1,100,1,1]))
    print(getUniqueUserIdSum([12,11,12,11]))
