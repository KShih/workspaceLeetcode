# https://leetcode.com/discuss/interview-question/352459/
# if every elem in A is distinct
# if there is duplicate

def largest_subarray_nodup(A, k):
    n = len(A)
    if n == 0 or k <= 0 or k > n:
        return {}
    if k == n:
        return A
    cand = A[:n-k+1]
    start = A.index(max(cand))
    end = start + k
    print(A[start:start+k])

def largest_subarray_wtdup(A, k):
    n = len(A)
    if n == 0 or k <= 0 or k > n:
        return {}
    if k == n:
        return A
    idx, max, = -1, 0
    i = 0
    while i <= n-k:
        if A[i] > max:
            max, idx = A[i], i
        elif A[i] == max:
            # comparing the rest, see if there is bigger elem in subarr start from A[i]
            newidx = i
            oldidx = idx
            while newidx < i+k:
                if A[newidx] > A[oldidx]:
                    idx = i
                    break
                newidx, oldidx = newidx+1, oldidx+1
        i += 1
    print(A[idx:idx+k])


if __name__ == '__main__':
    largest_subarray_nodup([1,4,3,2,5,1], 4) # [4,3,2,5]
    largest_subarray_wtdup([1, 4, 3, 2, 1, 4, 5, 6, 7],4) # [4,5,6,7]
    largest_subarray_wtdup([8,7,6,5,4,3,2,1],4) # [8,7,6,5]
    largest_subarray_wtdup([1,1,1,1,1,1,1],4)
