def distinctpair(arr, k):
    res = set()
    for elem in arr:
        if elem > k:
            continue
        if k - elem in arr:
            if k - elem > elem:
                res.add((elem, k - elem))
            else:
                res.add((k - elem, elem))
    return len(res)


if __name__ == '__main__':
    print(distinctpair([5,7,9,13,11,6,6,3,3],12))
