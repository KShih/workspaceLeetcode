def universityCareerFair(arrival, duration):
    aux = sorted(
        list(zip(arrival, duration)),       # bind same index in two list into a pair
        key=lambda p: (p[0]+p[1], p[1])     # sort by 1. leave time 2. duration time
    )
    print(aux)
    ans, end = 0, -float('inf')
    for arr, dur in aux:
        if arr >= end:
            ans = ans + 1
            end = arr + dur # 更新時間
    return ans


print(universityCareerFair([1, 3, 3, 5, 7], [2, 2, 1, 2, 1])) # 4
print(universityCareerFair([1, 2], [7, 3])) # 1
print(universityCareerFair([1, 3, 4, 6], [4, 3, 3, 2])) # 2
print(universityCareerFair([1, 2,3,4,5], [3,1,1,1,1])) # 4
