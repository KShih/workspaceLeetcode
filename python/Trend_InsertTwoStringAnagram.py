"""
https://www.geeksforgeeks.org/minimum-number-of-manipulations-required-to-make-two-strings-anagram-without-deletion-of-character/
Given two strings s1 and s2, we need to find the minimum number of manipulations required to make two strings anagram without deleting any character.
Note:- The anagram strings have same set of characters, sequence of characters can be different.

(Allow to change char, if cannot change char and only allow to insert, then use two dict)
"""

def func(str1, str2):
    char_table = [0] * 26
    count = 0
    for c in str1:
        char_table[ ord(c)-ord('a') ] += 1

    for c in str2:
        char_table[ ord(c)-ord('a') ] -= 1
        if char_table[ ord(c)-ord('a') ] < 0:
            count += 1

    return count

if __name__ == '__main__':
    print(func("aab", "baa"))
    print(func("abc", "abd"))
