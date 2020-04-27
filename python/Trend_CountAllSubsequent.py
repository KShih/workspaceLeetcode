"""
https://www.geeksforgeeks.org/minimum-number-of-manipulations-required-to-make-two-strings-anagram-without-deletion-of-character/

Count all increasing subsequences
We are given an array of digits (values lie in range from 0 to 9).
The task is to count all the sub sequences possible in array such that in each subsequence every digit is greater than its previous digits in the subsequence.

Input : arr[] = {1, 2, 3, 4}
Output: 15
There are total increasing subsequences
{1}, {2}, {3}, {4}, {1,2}, {1,3}, {1,4},
{2,3}, {2,4}, {3,4}, {1,2,3}, {1,2,4},
{1,3,4}, {2,3,4}, {1,2,3,4}

Input : arr[] = {4, 3, 6, 5}
Output: 8
Sub-sequences are {4}, {3}, {6}, {5},
{4,6}, {4,5}, {3,6}, {3,5}
"""

def count_sub(arr):
    def countSub(arr, n):

    # count[] array is used to store all
    # sub-sequences possible using that
    # digit count[] array covers all the
    # digit from 0 to 9
    count = [0 for i in range(10)]
  
    # scan each digit in arr[]
    for i in range(n):

        # count all possible sub-sequences by
        # the digits less than arr[i] digit
        for j in range(arr[i] - 1, -1, -1):
            count[arr[i]] += count[j]

        # store sum of all sub-sequences
        # plus 1 in count[] array
        count[arr[i]] += 1


    # Now sum up the all sequences
    # possible in count[] array
    result = 0
    for i in range(10):
        result += count[i]

    return result
