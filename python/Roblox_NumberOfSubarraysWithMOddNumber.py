def getSubarrayCount(a, m):
    start = 0
    end = 0
    cnt = 0
    total = 0
    while end < len(a):

        if a[end] % 2 != 0:
            cnt += 1
        end += 1
        while cnt > m:
            if a[start] % 2 != 0:
                cnt -= 1
            start += 1
        print("start = ", start)
        print("end = ", end)
        print("array: ", a[start:end])
        print("----")
        if cnt == m:
            print("in coming!")
            total += getSubcount(a, start, end, m)
            print(total)
            print("----")
    return total

def getSubcount(a, start, end, m):
    total_so_far = 0 if m == 0 else 1
    while start<end and a[start] %2 == 0:
        total_so_far += 1
        start += 1
    return total_so_far

if __name__ == '__main__':
    print(getSubarrayCount([2,5,6,9], 2))
    print(getSubarrayCount([2,2,5,6,9,2,11], 2))
