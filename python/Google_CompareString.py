from collections import Counter

def better_compare_string(A, B):
    A, B = A.split(","), B.split(",")
    freq_count_of_A, cache = [0] * 11, [0] * 11   # count of freq 1~10, cache for sum of first i value in freq array
    ret = []

    for str in A:
        min_freq = str.count(min(str))
        freq_count_of_A[min_freq] += 1

    for str in B:
        min_freq = str.count(min(str))
        if cache[min_freq] == 0:
            sum_f = sum(freq_count_of_A[:min_freq])
            ret.append(sum_f)
            cache[min_freq] = sum_f
        else:
            ret.append(cache[min_freq])

    return ret


def compare_string(A, B):

    freq_count_of_A = [0] * 11 # count of freq 1~10
    res = []
    cache = [0] * 11 # cache for sum of first i value in freq_count_of_A
    A = A.split(",")
    for str in A:
        count = get_smallest_count(str)
        freq_count_of_A[count] += 1

    B = B.split(",")
    for str in B:
        count = get_smallest_count(str)

        if cache[count] == 0:
            sum = 0
            for i in range(1,count):
                sum += freq_count_of_A[i]
            cache[count] = sum
        else:
            sum = cache[count]

        res.append(sum)
    return res

def get_smallest_count(str):
    str = sorted(str)
    i, count = 1, 1
    while i < len(str) and str[i] == str[i-1]:
        count, i = count+1, i+1

    return count


if __name__ == '__main__':
    print(compare_string("abcd,aabc,bd", "aaa,aa"))
    print(better_compare_string("abcd,aabc,bd", "aaa,aa"))
    print(better_compare_string("bacd,baac,bd", "aaa,aa"))
