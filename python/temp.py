def smallest(li):
    ans = li[0]
    for i in range(1,len(li)):
        if ans > li[i]:
            ans = li[i]
    return ans


if __name__ == "__main__":
    print(smallest([-1,1,-2,2]))
    print(smallest([1,2,3,0,-5]))
