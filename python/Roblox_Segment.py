def segment(arr, x):
    cand = []
    for i in range(len(arr)-x+1):
        cand.append(arr[i:i+x])

    minCand = []
    for can in cand:
        minCand.append(min(can))
    return max(minCand)

if __name__ == "__main__":
    print(segment([8,2,4,3],2))
