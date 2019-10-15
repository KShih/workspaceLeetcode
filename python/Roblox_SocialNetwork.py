def socialnetwork(arr):
    dic = dict()
    out = []
    for i in range(len(arr)):
        size = str(arr[i])
        if size in dic.keys():
            # 如果該group已滿，重新創一個group
            if len(dic[size][-1]) >= arr[i]:
                dic[size].append([i])
            else:
                dic[size][-1].append(i)
        else:
            dic[size] = [] # 二維list初始化
            dic[size].append([i])

        # 如果group已滿，加入輸出list中
        if len(dic[size][-1]) >= arr[i]:
            out.append(dic[size][-1])

    print(sorted(out))


if __name__ == '__main__':
    socialnetwork([2,1,1,2,1]) # 0 3 /n 1 /n 2 /n 4
    print("----")
    socialnetwork([3,3,3,3,3,1,3]) # 0 1 2 /n 3 4 6 /n 5
    print("----")
    socialnetwork([2,2,1,2,2]) # 0 1 /n 3 4 /n 2
