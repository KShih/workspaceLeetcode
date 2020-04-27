"""
We want to make an array sorted in non-decreasing order by deleting exactly one item from it. How many ways can we do that ?

For example, if the input array is [3, 4, 5, 4], the answer will 2, as we can delete either 5 or the second 4.

If the array is [3, 4, 5, 2] the answer will be 1, as we can delete 2.

If the array is [1, 2, 3, 4, 5] the answer will be 5, as we can delete any one of the elements.
"""


def func(array):
    options = 0
    for i in range(1, len(array)):
        if array[i-1] > array[i]:
            if options is not 0:
                return 0
            if i == 1 or array[i-2] <= array[i]:
                options += 1
            if i == len(array)-1 or array[i-1] <= array[i+1]:
                options += 1
            if options == 0: #[2,2,1,1]
                return 0
    return len(array) if options == 0 else options

if __name__ == '__main__':
    arrays = [[1,2,3,4],[1,3,2,4],[1,2,4,3],[1,3,4,2],[2,4,1,3],[2,2,1,1],[3,4,5,4],[3,4,5,2],[9,8,7,1,6,5]]
    for arr in arrays:
        print(func(arr))
