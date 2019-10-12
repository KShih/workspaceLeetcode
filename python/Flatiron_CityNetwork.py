from collections import deque
def network(city):
    res = [0] * (len(city) -1)
    q = deque()
    for i in range(len(city)):
        if city[i] == i:
            q.append(i)
            res[0] = 1

    dis = 1
    while dis < len(city)-2:
        # 設定這次的目標城市(首都)
        num = []
        while q:
            num = num + [q.pop()]

        # 找出與此目標相連的城市(9)
        count = 0
        for i in range(len(num)):
            for j in range(len(city)):
                if city[j] == num[i] and j != num[i]:
                    count += 1 # 計算這個距離的城市個數
                    q.append(j) # 設定下一輪的目標 (9)

        res[dis] = count
        dis += 1
    return res



if __name__ == "__main__":
    print(network([9,1,4,9,0,4,8,9,0,1]))
