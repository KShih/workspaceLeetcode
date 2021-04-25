Solution Model
===
## Python Trick
1. Dictionary
    1. iterate over keys:
        - `for k in list(dict.keys())`
        - Note: should listify!
    2. secure way to visit dict:
        - `dict.get(k)`
        - Benifit:
            - no need to initialize dict
            - no need to write `if k in dict: ...`
    3. add two dict:
        - `dict1.update(dict2)`
        - Note: cannot use `+`
    4. inline initialize:
        - `dict = {c: True for c in boolTable}`
2. Sort by key
    1. `intervals = sorted(intervals, key=lambda x: x[0])`
    2. `intervals = sorted(intervals, key=lambda x: (x[0], x[1], x[2], ...))`
3. 利用 tuple 的性質讓 unhashable type 變成 hashable
    1. `set.add(tuple(list))`

## Calculator
- for `224`, `227`, `772`
- 對於負整數也能解
- ![](assets/markdown-img-paste-20200414144532950.png)

### model
```py
    def __init__(self):
        self.i = 0

    def calculate(self, s: str) -> int:
        num, op, curSum, globalSum = 0, "+", 0, 0
        while self.i < len(s):
            c = s[self.i]
            self.i += 1 # note increase i here
            if c.isnumeric():
                num = num*10 + int(c)
            elif c == '(':
                num = self.calculate(s) # use global i to track progress
            elif c == ')':
                break # simply break and rely on return to update the correct global
            if c in ["+", "-", "*", "/"]:
                # update curSum
                # update globalSum and reset curSum if c is + or -
                # reset num and update op
        return globalSum + self.cal(curSum, num, op)

    def cal(self, curSum, num, op):
        if op == "+":
            curSum += num
        elif op == "-":
            curSum -= num
        elif op == "*":
            curSum *= num
        elif op == "/":
            curSum = int(curSum / num)
        return curSum
```

### example:
```py
class Solution:
    def __init__(self):
        self.i = 0

    def calculate(self, s: str) -> int:
        num, op, curSum, globalSum = 0, "+", 0, 0
        while self.i < len(s):
            c = s[self.i]
            self.i += 1
            if c.isnumeric():
                num = num*10 + int(c)
            elif c == '(':
                num = self.calculate(s)
            elif c == ')':
                break
            if c in ["+", "-", "*", "/"]:
                curSum = self.cal(curSum, num, op)
                if c in ["+", "-"]:
                    globalSum += curSum
                    curSum = 0
                num, op = 0, c
        return globalSum + self.cal(curSum, num, op)

    def cal(self, curSum, num, op):
        if op == "+":
            curSum += num
        elif op == "-":
            curSum -= num
        elif op == "*":
            curSum *= num
        elif op == "/":
            curSum = int(curSum / num)
        return curSum
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

0. 模板
    ```py
    # LC904
    for r, t in enumerate(tree):
        dic[t] += 1 # update條件
        while len(dic) > 2: # 檢查條件
            dic[tree[l]] -= 1 # 縮左邊
            if dic[tree[l]] == 0:
                del dic[tree[l]] # 更新條件
            l += 1
        res = max(res, r-l+1)
    ```
1. Window 形成一個合法的狀態，我們透過其他資料結構 (如dict, 變數) 去協助我們伸縮子集合的長度，如果不用此方法變成我們必須要去先取得所有可能的組合
2. Sliding window 求 subarray combination 的時候適合使用 atMost 的技巧, 如 LC930 求 =k 時, 用 atMost(k) - atMost(k-1)
    ```py
    def atMost(S):
        cnt, _sum, l = 0, 0, 0

        for r, a in enumerate(A):
            _sum += a
            while _sum > S:
                _sum -= A[l]
                l += 1
            cnt += (r-l+1)
        return cnt
    ```
3. Sliding 的對象 arrray 必須是非負陣列，否則會破壞 window
4. 題型總和
    0. 209. Minimum Size Subarray Sum
    1. 1248. Count Number of Nice Subarrays
    2. 1234. Replace the Substring for Balanced String
    3. 1004. Max Consecutive Ones III
    4. 930. Binary Subarrays With Sum
    5. 992. Subarrays with K Different Integers
    6. 904. Fruit Into Baskets
    7. 862. Shortest Subarray with Sum at Least K - too hard

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

## LIS (Longest Increasing Subsequence)

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
    - ![one line python recursive](assets/markdown-img-paste-2020090620195401.png)

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
    - ![model iterative for all](assets/markdown-img-paste-20210413082305301.png)
- Note:
    - 遇到 preorder 可解的優先採用 iterative 寫法 (高效)

1. Iterative 版 inorder (左中右)
    ```py
    # 左中右
    class Solution:
        def inorderTraversal(self, root: TreeNode):
            stack = []
            res = []
            p = root

            while p or stack:
                if p:
                    stack.append(p)
                    p = p.left
                else:
                    top = stack.pop()
                    res.append(top.val)
                    p = top.right
            return res
    ```

    一般版
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
    # 中左右
    class Solution:
        def preorderTraversal(self, root: TreeNode):
            stack = []
            res = []
            p = root

            while p or stack:
                if p:
                    res.append(p.val) # 中
                    stack.append(p)   # 左
                    p = p.left        # 左
                else:
                    top = stack.pop()
                    p = top.right
            return res
    ```

    一般版
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
    # 左右中 -> 中右左 -> return 時再反轉
    class Solution:
        def postorderTraversal(self, root: TreeNode):
            stack = []
            res = []
            p = root

            while p or stack:
                if p:
                    res.append(p.val)  # 中
                    stack.append(p)    # 右
                    p = p.right        # 右
                else:
                    top = stack.pop()  # 左
                    p = top.left       # 左
            return res[::-1]           # 反轉
    ```

    two stack version
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

1. 一次拜訪整層 => 可用於 BFS 求最短路徑 (LC126. Word Ladder II), (LC301. Remove Invalid Parentheses)
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

3. Two-ends BFS
    - 適用於終點也能擴展的題目 e.g.: LC752
    - 概念:
        - 用兩個 set, 每次選擇用小的去 extend 進 new_front
        - 檢查這個 extend 的有沒有存在 back 裡面, 有就找到了, 沒有就繼續
        - 整層都沒找到後, 判斷現在的 back 跟new_front誰小, 如果 back 比較小, 則做 swap
    - 模板:
        ```py
        seen = set()
        front, back = set(), set()
        while front:
            new_front = set()
            for e in front:
                new_e = process(e)
                if new_e in back:
                    return res
                elif new_e not in seen:
                    seen.add(new_e)
                    new_front.add(new_e)
            if len(back) < len(new_front):
                back, new_front = new_front, back
            front = new_front
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

## Mono Stack

1. 可以透過維持/破壞 stack 單調性來解題
2. 例題: LC42 trapping water
    - ![](assets/markdown-img-paste-20210411173458150.png)
        - 兩邊高、中間低，而我們對中間低窪的地區有興趣 -> 可以維持 遞減 stack
        - 當暴增的元素出現時，我們就可以把頂端元素弄出來處理了，因為我們找到右邊的封口了 (左邊的封口由遞減 stack 所自然形成)
    ```py
    class Solution:
        def trap(self, height: List[int]) -> int:
            stack = []
            res = 0
            for i, h in enumerate(height):
                while stack and h > height[stack[-1]]:
                    deal = stack.pop()
                    if stack:
                        # processing w/ deal, could be any logic
                        _height = min(h, height[stack[-1]]) - height[deal]
                        _width = i - stack[-1] -1
                        res += _height * _width
                stack.append(i)
            return res
    ```
3. 所有例題: LC42, LC84, LC85, LC255, LC739(典型), LC1130


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
1. 有向圖
    1. 有向圖找環 (黑白大法)
        1. 建立連結 (node -> list[node])
        2. 走訪所有節點
            1. backtrack 其子節點
            2. 如果出現在 visited 中, 表示有走過了 -> 找到環
        3. Note: 可用 cache 來剪枝
        4. Example: LC207. Course Schedule I
    2. 拓樸排序 (黑白灰大法)
        1. 從圖找環去改
            1. 額外多增加一個狀態 `visited but not circle`
            2. 額外多維護一個 stack 去 append path
                - Note: 更新的時機是確定當前點的所有鄰居都不會產生環時
        2. 差別詳見 LC210. Course Schedule II
        3. 視要求決定如何 loop (有可能出現孤島節點時):
            1. 如 LC269 要求輸出所有出現過的 char, 但無法排序的話任何順序都可以, 此時我們 loop 的對象應該是 "所有節點"
            2. 但像是如果單純找環, 那麼孤島節點肯定沒有環，因此也不需要去 loop 了
2. 無向圖
    0. Union Find
        ```py
        def init(self, node_cnt):
            self.root_map = [id for id in range(node_cnt)] # each node points to itself, (could also use dict)
            self.sizes = [1 for id in range(node_cnt)]

        def union(self, x, y):
            self.root_map[self.find(y)] = self.find(x) # for simplicity, didn't compare the size
            # # Size compare optimize:
            # root_x, root_y = self.find(x), self.find(y)
            # if self.sizes(root_x) < self.sizes(root_y):
            #     if self.sizes[root_x] < self.sizes[root_y]:
            #         self.root_map[root_x] = root_y
            #         self.sizes[root_y] += root_x
            #     else:
            #         self.root_map[root_y] = root_x
            #         self.sizes[root_x] += root_y

        def find(self, x):
            if self.root_map[x] != x:
                self.root_map[x] = self.find(self.root_map[x])
            return self.root_map[x]
        ```
    1. 無向圖找環
        1. UnionFind (找你爸法)
            0. Time:
                1. Naive: O(N^2)
                2. Path Compression: O(N⋅α) ~= O(N)
                3. Find 本身 ~= O(α(N)) ~= O(1)
            1. 初始化 root_map (每個點的root都是自己), 連續的點用 arr, 不連續的點用 dict
            2. 對每對 connected component, 分別找到其 root
            3. 如果他們的 root 相同, (如圖 [2,3] 為 connected component, 他們的root 都是1) -> 表示有環存在
                 ```
                 1 - 2
                   \ |
                     3
                 ```
            4. 如果不同, 則進行 union 的動作(把 `y的root` 連到 `x的root` 下)
            5. Example: LC261
            6. 優化: 此種簡單版，會變成 LinkedList, 但我們可以讓樹不要長這麼高
                1. Path Compression
                2. 在 找到 root 後, 把路途中的所有節點全部修正指向 root
                3. 在 union 的階段, 不直接 hard-code root_map[root_y] = root_x, 而是 phase3 先判斷各自樹的大小, 再把小的依附到大的下

    2. 無向圖找 connected component
        1. Union Find
            1. 可利用 UnionFind 找, **去算有多少節點的 root 還是本身** (LC323)
                `len([i for i in range(len(self.root_map)) if i == self.root_map[i]])`
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

## QuickSelect

- 針對尋找前 k sth 的題
- 快速回憶: divideAndConquer -> partition -> pivot -> swap with back -> iterate to find perfect index for pivot -> swap it back -> decide we need to add more elem in front or delete some -> divideAndConquer ...

1. QuickSelect k smallest
    1. 從 l, r 隨機找出一個 index 當 pivot
    2. 去進行 partition algorithm
    3. 如果回傳的 perfect pivot 位置 == k -> 即為所求
    4. 位置 < k -> 還需要補入更多數 -> 對右半邊運算, 反之左半邊
2. Partion Algorithm
    1. Work for unique elem
        1. 先紀錄 pivot index 所代表的意義 (frequency or sth)
        2. 把 p 跟 r 交換
        3. 初始化 store_idx 為 l
        4. 對區間 (l, r) 去 for-loop
            1. 如果 freq[i] < freq_p -> swap(i, store_idx++)
        5. 最後再把 r 跟 store_idx 調換 (p換回到 perfect index)
        6. return store_idx

```py
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        unique = list(count.keys())

        def partition(l, r, p):
            pivot_freq = count[unique[p]]
            unique[r], unique[p] = unique[p], unique[r]

            idx = l
            for i in range(l, r):
                if count[unique[i]] < pivot_freq:
                    unique[idx], unique[i] = unique[i], unique[idx]
                    idx += 1

            unique[r], unique[idx] = unique[idx], unique[r]
            return idx

        def quickselect(l, r, k_smallest):
            if l == r:
                return
            p = random.randint(l, r)
            p = partition(l, r, p)
            if p == k_smallest:
                return
            elif p < k_smallest:
                quickselect(p+1, r, k_smallest)
            else:
                quickselect(l, p-1, k_smallest)

        n = len(unique)
        quickselect(0, n-1, n-k)
        return unique[n-k: ]
```

---

## Prefix Sum

- Good question:
    - LC930. Binary Subarrays With Sum
    - LC437. Path Sum III
    - LC560. Subarray Sum Equals K
- Array 類型的可用 sliding window 來解

https://leetcode.com/discuss/general-discussion/563022/prefix-sum-problems
