"""
Given an unsorted array,
Output an array which let all even number before odd number
And return the min move

https://www.geeksforgeeks.org/segregate-even-and-odd-numbers/

"""

def even_before_odd(arr):
    print("original",arr)
    l, r = 0, len(arr)-1
    count = 0

    while l < r:

        while arr[l] % 2 == 0 and l < r:
            l += 1

        while arr[r] % 2 != 0 and l < r:
            r -= 1

        if r != l:
            count += 1
            arr[l], arr[r] = arr[r], arr[l]

    print(arr)
    print(count)
    print("---")

if __name__ == '__main__':
    even_before_odd([1,2,3]) # 1
    even_before_odd([1,2,3,4]) # 1
    even_before_odd([1,3,5]) # 0
    even_before_odd([1,3]) # 0
    even_before_odd([1]) # 0
    even_before_odd([2,4]) # 0
    even_before_odd([2,4,1,3]) # 0
    even_before_odd([]) # 0
    even_before_odd([2,4,1,3,6,8,10]) # 2
