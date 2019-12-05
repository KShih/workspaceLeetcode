class Solution(object):
    def merge(self, nums1, m, nums2, n):
        res = []
        cur1, cur2 = 0, 0
        for i in range(m+n):
            if cur1 == m:
                self.append_rest(cur2, nums2, res, n)
                break
            if cur2 == n:
                self.append_rest(cur1, nums1, res, m)
                break
            if nums1[cur1] <= nums2[cur2]:
                res.append(nums1[cur1])
                cur1 += 1
            else:
                res.append(nums2[cur2])
                cur2 += 1
        return res

    def append_rest(self,cur, nums, res, bound):
        for j in range(cur, bound):
            res.append(nums[j])

if __name__ == '__main__':
    s = Solution()
    print(s.merge([1,2,3,0,0,0],3,[2,5,6],3))
