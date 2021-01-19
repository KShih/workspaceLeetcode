Solution Model
===
## Calculator
- for `224`, `227`, `772`, `770`
- ![](assets/markdown-img-paste-20200414144532950.png)

### model
```py

while i < len(s):
    c = s[i]
    if isdigit():
        # build-digit()
    elif c == '(':
        cnt = 0
        for j in range(i, len(s)):
            if s[j] == '(':
                cnt += 1
            if s[j] == ')':
                cnt -= 1
            if cnt == 0:
                break
        num = self.calculate(s[i+1:j])
        i = j

    if c is not digit or i is last digit:
        switch(op) to update curRes
        update res if c is + or -
            init curRes
        update op and init num
    inc i
```

### example:
```py
    def calculate(self, s: str) -> int:
        res, curRes, num, op = 0, 0, 0, '+'
        i = 0

        while i < len(s):
            c = s[i]
            if c.isdigit():
                num = num*10 + int(c)
            elif c == '(':
                cnt = 0
                for j in range(i, len(s)):
                    if s[j] == '(':
                        cnt += 1
                    if s[j] == ')':
                        cnt -= 1
                    if cnt == 0:
                        break
                num = self.calculate(s[i+1:j])
                i = j


            if c in ['+', '-', '*', '/'] or i == len(s)-1:
                # update curRes
                if op == '+':
                    curRes += num
                elif op == '-':
                    curRes -= num
                elif op == '*':
                    curRes *= num
                elif op == '/':
                    curRes = int(curRes / num)

                # determine whether update res from curRes
                if c in ['+', '-'] or i == len(s)-1:
                    res += curRes
                    curRes = 0

                # update
                op, num = c, 0

            i += 1
        return res
```

---

## Accumulated Sum

- 累積陣列值的技巧

### 技巧變形1: +1 -1

- `525`
- binary array:
    - 遇到0: sum-1
    - 遇到1: sum+1

---

## Sliding Window

1. Sliding 的對象 arrray 必須是非負陣列，否則會破壞 window
2. 題型總和
    0. 209. Minimum Size Subarray Sum
    1. 1248. Count Number of Nice Subarrays
    2. 1234. Replace the Substring for Balanced String
    3. 1004. Max Consecutive Ones III
    4. 930. Binary Subarrays With Sum
    5. 992. Subarrays with K Different Integers
    6. 904. Fruit Into Baskets
    7. 862. Shortest Subarray with Sum at Least K

---

## Binary Search

1. Always use right = len(nums) -1, because you may want to access arr[right]!
    - 在宣告時就已經朝著 "l" 跟 "r" 都有可能是可能解的方向, 所以在限縮左右邊界時也要保持這個特性
2. 最單純的binary search, 查找特定的值:
    - l <= r
    - mid == target: break
    - l = mid + 1
    - r = mid - 1
3. 查找左邊界:
    - l < r
    - l = mid +1
    - **r = mid**
        - 其所屬的條件及為言語上的所求，例如 LC34 的第一個 bs
        - 我想找『大於等於 target 的左邊界』=> 就要想到
            1. 我要 return r
            2. r = mid，並且進入此表達式的條件要是『大於等於 target』
    - **return r**
4. 查找右邊界:
    - l < r
    - **mid = l + (r-l)//2 + 1**
    - **l = mid**
        - 同上，其所屬的條件及為言語上的所求，例如 LC34 的第二個 bs
    - r = mid - 1
    - **return l**
5. 注意查找左右邊界的if判斷式寫法:
    - **if 判斷式均要放 >= or <= 的情形 (因配合我們宣告 r = len(nums)-1)**
    - 不見得！用一些 testcase 去帶去思考
    - 詳見LC34三刷code

6. 實作 bisect_left (使用查找特定值模板)
    ```py
    def bisect_left(self, arr, target):
        i = 0
        j = len(arr)-1
        while i <= j:
            mid = i + (j-i)//2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                i = mid+1
            else:
                j = mid-1
        return i
    ```


---

## LIS

```py
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        inc = [float(inf)]*(n) # 優化: 使用下面 res 動態擴展的方式
        res = 0

        for num in nums:
            x = bisect.bisect_left(inc, num)
            inc[x] = num
            res = max(res, x+1)

        return res
```

---

## LinkedList
1. 快慢指針找環
    1. phase1: 快慢指針找出重合點
    2. phase2: 另一個指針從起始點出發, 與慢指針一步步前進, 重合處即是環的開始
    3. 見 LC142, 287
2. Doubly LinkedList
    1. Insert, Delete: O(1)
    2. Example: LRU cache <LC146>

---

## Bit manipulate

1. https://medium.com/techie-delight/bit-manipulation-interview-questions-and-practice-problems-27c0e71412e7

---

## Binary Tree Traversal

- One line python(Pretty useful!)
    - ![](assets/markdown-img-paste-2020090620195401.png)
    -

---

## BFS

```py
def bfs():
    # initialize
    visited, queue = {}, []

    while queue:
        # process current node
        var = queue.pop(0)

        # gen more node
        more_nodes = self.gen_more_node(var)

        # check visited
        for next_node in more_nodes:
            if next_node not in visited:
                queue.append(next_node)
                visited.add(next_node)
```

## DFS

Recursive:
```py
visited = set()

def dfs(node, visited):
    if node in visited:
        return # already visited, terminated

    # process current node here

    # gen more node
    more_nodes = self.gen_more_node(node)

    for next_node in more_nodes:
        if not next_node in visted:
            dfs(next_node, visited)
```

Iterative:
```py

def DFS(tree):
    visited, stack = [], [tree.root]

    while stack:
        node = stack.pop()

        # process current node

        # gen more node
        more_nodes = self.gen_more_node(node)

        for next_node in more_nodes:
            if not next_node in visted:
                stack.append(next_node)
                visited.add(next_node)
```

## 總結 BFS, DFS 五部曲
1. 建立 queue/stack, visited set
2. while queue/stack not empty {
3.       處理當前節點
4.       擴展節點
5.       入 queue/stack, 更新 visited
6. }

---
