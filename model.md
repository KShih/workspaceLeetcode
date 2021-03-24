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
2. 快慢指針找 List 中點 <LC109>
    1. 寫法1: head 多先走一步，就可以不需要用到 dum
    2. 寫法2: 遇到需要切割 fast 宣告成 head.next.next，就可以直接用 slow.next 去切
        ```py
        slow, fast = head, head.next.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        mid = slow.next # <- center
        slow.next = None # <- cut the front
        right = mid.next # <- new head of right
        ```
2. Doubly LinkedList
    1. Insert, Delete: O(1)
    2. Example: LRU cache <LC146>
3. 在某個節點前插入新結點
    1. 修改current dummy 的值
    2. 插入新的dummy 並指向舊的dummy
    3. Example: <LC445>
4. 快慢指針存取*倒數第 n 個*節點
    1. 快指針先走 n 步, 再讓兩者同時前進
    2. 當快指針走到底時，慢指針的位置即為所求
5. 旋轉 LinkedList
    1. 頭尾相接，然後做兩件事：找出新頭, 斷尾
6. 跳者走訪 LinkedList
    1. 用兩個指標 first, second
    2. first.next = second.next, second.next = first.next.next
7. Reverse list
    1. stack 協助
    2. reverse in place
        ```py
        revHead = None # started of the reverse list

        while ptr:
            nxt = ptr.next
            ptr.next = revHead
            revHead = ptr
            ptr = nxt
        ```
    3. Recursively
        ```py
        if not head or not head.next: # use not head.next to stand previously
            return head

        revHead = self.reverseList(head.next) # should not do any modify to it
        head.next.next = head # modify the second's next to first
        head.next = None # release the original pointer
        return revHead
        ```
---

## Bit manipulate

1. https://medium.com/techie-delight/bit-manipulation-interview-questions-and-practice-problems-27c0e71412e7

---

## Binary Tree Traversal

- One line python(Pretty useful!)
    - ![](assets/markdown-img-paste-2020090620195401.png)

    精簡版
    ```py
    def inorder(root):
        return inorder(root.left) + [root.val] + inorder(root.right) if root else []
    ```

    可拓展版 (可用於對於 node 需要進行的不同操作)
    ```py
    def inorder(root):
        if root:
            left_list = inorder(root.left)
            node_list = [root.val]
            right_list = inorder(root.right)

            return left_list + node_list + right_list
        else:
            return []
    ```

- 使用Iterative 避免 stackoverflow
- Note:
    - 遇到 preorder 可解的優先採用 iterative 寫法 (高效)

1. Iterative 版 inorder (左中右)
    ```py
    def inorder(root):
        stack = []
        inorder = []
        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            inorder.append(root.val)
            root = root.right
        return inorder
    ```

2. Iterative 版 preorder (中左右)
    ```py
    def preorderTraversal(self, root):
        if root is None:
            return []
        stack = [root]
        preorder = []
        while stack:
            node = stack.pop()
            preorder.append(node.val)
            if node.right:
               stack.append(node.right)
            if node.left:
               stack.append(node.left)
        return preorder
    ```

3. Iterative 版 postorder (左右中)
    ```py
    # 1. Push root to first stack.
    # 2. Loop while first stack is not empty
    #    2.1 Pop a node from first stack and push it to second stack
    #    2.2 Push left and right children of the popped node to first
    #        stack
    # 3. Print contents of second stack
    def postOrder(self, root):
        if root is None:
            return

        s1 = []
        s2 = []
        postOrder = []

        s1.append(root)

        while s1: # append 到 s2 的順序 中左右
            node = s1.pop()
            s2.append(node)

            if node.left:
                s1.append(node.left)
            if node.right:
                s1.append(node.right)

        while s2:
            node = s2.pop()
            postOrder.append(node.val)
        return postOrder
    ```
- Optimal Traversal strategy: Morris Traversal (not required)
    - see article: https://leetcode.com/problems/recover-binary-search-tree/solution/

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

1. 一次拜訪整層 => 可用於 BFS 求最短路徑 (LC126. Word Ladder II)
2. p.s. 額外展示 Set 反向操作技巧，如果已經知道哪些點會出現在 set 時
```py
canVisit = set(wordList)
while layer:
    next_layer = []
    for var in layer:
        more_nodes = self.gen_more_node(var)
        for next_node in more_nodes:
            if next_node in canVisit:
                next_layer.append(next_node)

    canVisit -= set(next_layer)
    layer = next_layer
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

## Backtrack
1. 先得到三要素
    1. Goal (終止條件)
    2. Constraint and Choice
    3. 模板
    ```py
    def main():
        def helper(states):
            if Goal:
                # do terminatation e.g. add to result
            for c in Choice:
                if Constraint:
                    helper(states + c)
    ```
2. Combination 中不重複的 Trick
    1. <Basic> Choice 無重複:
        - 加入 idx 進 states 去遞迴, 在找 choice 時只往 idx 後面的看
    2. <Advance> Choice 會重複:
        1. Counter + Frequency Backtrack *(Better)*
        2. Sort + If
        3. 例題:
            1. LC40 Combination Sum II
            2. LC90 Subsets II
3. Time complexity:
    - O( (bn)^d ) *bn 的 d 次方*
        - b (base): 為一層的節點數, 也就是 choice的數量
        - n : 為每個節點內所需操作的時間(通常為 constant time)
        - d : 為此 recursion tree 的深度(最大)
4. Recursive 加入 Memorization 的範例:
    1. LC131
        1. Goal 的狀況要先改成 base case
        2. 在 Choice 中去拿 `子recursive` 的總結果
        3. 把總結果加上 Choice 並更新到 res
        4. 更新 Memo
    2. LC140 (LC139 follow-up)
        -  Memorization 的項目由單個結果轉換成 Combination
        -  DP 儲存的內容由單個結果轉換成 Combination

---

## Graph
1. 圖找環
    1. 建立連結 (node -> list[node])
    2. 走訪所有節點
        1. backtrack 其子節點
        2. 如果出現在 visited 中, 表示有走過了 -> 找到環
    3. Note: 可用 cache 來剪枝
    4. Example: LC207

---

## DP
1. TopDown
    1. 可以從 Recursive 的解法演化而來
    2. 缺點: 依舊存在 recursive 過多的問題
    3. 題目: LC10, LC44
2. BottonUp
    1. 需直接思考到`如何定義子問題`
    2. `子問題的狀態如何轉移`
    3. 大部分的題

---

## Heap

```py
# LeetCode 218
from heapq import heappush, heappop
class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # 1. define sources
        events = [(L, -H, R) for L, R, H in buildings]
        events += [(R, 0, 0) for _, R, _ in buildings]
        events = sorted(events)

        # 2. initialize heap -> try to keep at least one elem in heap, in order not to out of range in step4
        live = [(0, float(inf))]

        # 3. iterate over sources
        for pos, negH, R in events:

            # 4. pop-out useless elem in heap
            while live[0][1] <= pos:
                heappop(live)

            # 5. push new elem into heap
            if negH:
                heappush(live, (negH, R))

            # 6. decide if it's the right elem to output
            if -live[0][0] != res[-1][1]:
                res.append([pos, -live[0][0]])
        return res[1:]
```

---

## Prefix Sum

- Good question:
    - LC930. Binary Subarrays With Sum
    - LC437. Path Sum III
    - LC560. Subarray Sum Equals K
- Array 類型的可用 sliding window 來解

https://leetcode.com/discuss/general-discussion/563022/prefix-sum-problems
