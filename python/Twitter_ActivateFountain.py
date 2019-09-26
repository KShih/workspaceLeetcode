
def activateFountains(fountain):
    n = len(fountain)
    waterArea = [[0,0] for _ in range(n)]

    # calculate the most left and right this fountain can be
    for i in range(1,n+1):
        waterArea[i-1][0] = max(i - fountain[i-1], 1) # left-most of waterArea
        waterArea[i-1][1] = min(i+ fountain[i-1], n) # right-most of waterArea

    # two condition,
    # 1. try to have most right
    # 2. must have included the least one, cuz we will not update our left then
    # so we should let our 'must do', become the last sort
    waterArea.sort(key = lambda x: x[1],reverse = True)
    waterArea.sort(key = lambda x: x[0])

    # turn on the 'least left' but also with 'max right'
    minLeft = waterArea[0][0]
    maxRight= waterArea[0][1]
    neededFountain = 1  # cuz we turn it on, we should count from 1

    for i in range(1,n):
        thisLeft = waterArea[i][0]
        thisRight= waterArea[i][1]
        if thisLeft <= minLeft and thisRight >= maxRight:
            continue
        else:
            if thisRight > maxRight:
                maxRight = thisRight
                neededFountain += 1

    return neededFountain

if __name__ == '__main__':
    print(activateFountains([0,0,0,3,0,0,2,0,0]), 2)
    print(activateFountains([2,1,2,1,2,4]), 2)
    print(activateFountains([3,0,2,0,1,0]), 2)
    print(activateFountains([3,0,1,0,1,0]), 2)
    print(activateFountains([3,0,1,0,0,1]), 2)
    print(activateFountains([2,0,2,0,1,0]), 2)
    print(activateFountains([2,0,0,0,0]), 3)
    print(activateFountains([0,0,0,0,0]), 5)
    print(activateFountains([1,2,1]), 1)
    print(activateFountains([0,1,0]), 1)
