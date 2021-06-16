# Similar Problem

## Binary Tree Path Sum
### Questions
- LC112, LC113, LC437, LC124

1. LC112 Path Sum I
    1. 題目:
        - Given a binary tree and a sum, determine if the tree has a root-to-leaf path such that adding up all the values along the path equals the given sum.
    2. 分析:
        - 相對嚴格的條件從 root to leaf, 因此我們只需要維護一個 curSum 到 leaf 在判斷是否為 target 即可
    3. 解法:
        - 前序遍歷
2. LC113 Path Sum II
    1. 題目:
        - Given a binary tree and a sum, find all root-to-leaf paths where each path's sum equals the given sum.
    2. 分析:
        - 與上題一樣的條件，只是這題必須要求出所有路徑，因此只需要在上題的基礎上多維護一個 path arrays 去更新即可
    3. 解法:
        - 前序遍歷
3. LC437 Path Sum III
    1. 題目:
        - You are given a binary tree in which each node contains an integer value. Find the number of paths that sum to a given value. The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).
    2. 分析:
        - 因為不需要從 root 開始 Naive 的作法是維護 path, 並且走到新的節點就把舊的節點一個一個扣掉，看是否有等於 target 的點，但這種作法需要一直重複加減太不高笑。可以使用 prefix sum dictionary，去紀錄該 accumulated sum 出現的次數，到了新的節點只需要求出加上此節點後跟 target 的差距，再去這個 dict 找出此 sum 的出現次數再加上去即可
    3. 解法:
        - 前序遍歷 + prefix sum
4. LC124 Binary Tree Maximum Path Sum
    1. 題目:
        - Given a non-empty binary tree, find the maximum path sum. For this problem, a path is defined as any sequence of nodes from some starting node to any node in the tree along the parent-child connections. The path must contain at least one node and does not need to go through the root.
    2. 分析:
        - 此題要求的就不是是否等於某個 target，而是此 tree 所能產生的最大值
        - 因此前序已經不適用於此了，因為左右邊的值會影響我們的選擇
    3. 解法:
        - 後序遍歷 + global max update

## 在 array 中 count 符合條件的元素數量
- 共通點:
    1. 對於元素間的 index 關係有要求 (e.g. 後要比前的值小)
    2. 若我們已經處理完各個半部，我們就能夠直接加上剩餘的部分 (因為我們知道剩下的都會符合)，前提是我們要確定剩餘的一定能符合 (with the help of sorted array)

1. LC315
    - Classic Merge Sort
    - 後要比前小
2. LC493
    - 閹割版 Merge Sort (Divide and Conquer)
    - 前要比後的兩倍還大

## SlidingWindow 求符合條件的 Combination 數
- 均要用 atMost 去解, 至於為什麼, 詳見 992 的圖
    - 概念上就是: 如果求 exact 會漏, 那就全部取 atMost(n), 再去扣掉不合的 atMost(n-1)
1. LC930, LC992
    - 這兩題在 atMost中 window 的意義是**本此增加的 combination 個數**
2. 比較: Sliding Window 求極值的
    1. LC159, LC904
        1. 此題 window 的長度意義就是所求的長度

## Union Find and DFS
1. 找 Circle: LC261
2. 找 Connected Graph 數量: LC323

- Union Find:
    1. 找 Circle
        - 求 是否有共同 root
    2. 找 Connected Graph
        - 求 root 的數量
- DFS:
    1. 找 Circle
        - 遞迴求 是否重複 visited, (必須 exclude back_edge, 因此需要多傳一個 pre 來避免錯誤判斷)
    2. 找 Connected Graph
        - 遞迴去把所有連結的 mark 起來, 並遞增 cnt

## TopologicalSort
1. LC269. Alien Dictionary, LC210. Course Schedule II, LC332. Reconstruct Itinerary
2. 比較
    - 269 與 210 只有在建立 adjList 不一樣而已
    - 跟 332 的不同處是在 332 給定有限的拜訪路徑, 且次數可能 > 1, 換句話說可能出現有限的環
        - 因此我們在處理時，不用 visited 去追蹤, 而是直接把用過的路徑 pop 掉

## Two Sum Similar

### 1. Two Sum

- 描述: 給定一個未排序的數組, 找出隨便兩數的 index 加起來為 target
- 解法: HashTable

### 167. Two Sum II

- 描述: 給定一個排序好的數組, 找出隨便兩數的 index 加起來為 target
- 解法:
    1. Two Pointer
    2. Binary Search

### 15. 3Sum

- 描述: 給定一個未排序的數組, 找出所有數字組合, 加總起來為零, 且不能重複
- 解法大綱, 找出一個數, 並將其右的數組找出 2Sum

1. 處理未排序的組合:
    1. 使用排序
        - 可使用剪枝, 可在第一個數大於零後判斷後面不會再有解了
        - 並可使用 Two Sum II 的 two Pointer 解法
    2. 使用 set
        - 比較直覺, 且可以使用 Two Sum I 的解法
2. 處理 2Sum:
    1. 使用 Two Pointer, 此種方法只能搭配排序使用
    2. 使用 Set

### 259. 3Sum smaller

- 描述: 給定一個未排序的數組, 找出小於 target 的組合數量
- 比較: 這題不是找特定值, 因此 HashTable 法無法使用
- 解法:
    1. Two Pointer, 若是當前 l, r 組合是符合的, 那麼固定此 nums[i], nums[l] 去搭配 nums[l+1:r] 都是符合的
    2. BinarySeach, 解法類似於 16, 但這邊要注意要使用 bisect_left, 因為:
        - 我們的目標是尋找, 小於補數的, 因此要過濾等於, 所以要用 left

### 16. 3Sum Closest

- 描述: 給定一個未排序的數組, 找出最接近 target 的組合
- 比較: 這題不是找特定值, 因此 HashTable 法無法使用
- 解法:
    1. Two Pointer, 使用 cusSum 大於或小於 target 去移動 l, r
    2. BinarySearch, 固定兩個點, 去找第三個點, 這邊使用的是 biset_right, 因為要找出下個大於補數的位置

### 18. 4Sum (kSum)

- 描述: 3Sum 的延伸, 就是加個for
- 比較: 更高階的寫法應該要寫 kSum 的方法了
- 解法:
    - 用 recursive 的方法去避免不停地加上 for 迴圈上去
    - 維護變數 k, 逐層遞減, 直到 k == 2 時呼叫 twoSum 終止遞迴

## Line Sweep Similar
- 253 與 759
    1. 都需要 EventType、Balance、Prev
    2. Balance 紀錄目前讀到多少個 Open brackets
- 218
    1. 同樣需要將 Start, End 拆分成不同事件
    2. 多用一個 Heap 來去幫助我們做邏輯的處理(Get Heighest Building)
    3. 這時的 End 事件就是來幫我們去除掉 Heap 中已過期的事件

### 253. Meeting Rooms II
- 找出 Interval 間最大同時重合數
- 找出最大的 Open Brackets 數量

### 759. Employee Free Time
- 找出 Interval 間的空白處
- 當 Balance 為零時，表示找到新的 Free time 了 -> (Prev, CurrentTime)

### 218. The Skyline Problem
- 只用到事件的特性
- 後續的邏輯處理為 heap 的概念

## String Convert/Pattern
### LC205. Isomorphic Strings
- 此題求的是字串 pattern是否相同, 也就是去看相同字母其出現在兩個字串的位置是否相同
- 例子
    - s = "badc", t = "baba"
    - return False
- 解法: 要用雙向的 map

### LC1153. String Transforms Into Another String
- 而此題求的是字串A是否能 convert 成字串B, 彈性較大, 而且方向固定
- 例子
    - s = "badc", t = "baba"
    - return True
- 解法: 單向的 map, 但最後要加上檢查是否有橋可以去做 tmp char 的放置

## Duplicate Element in List
### LC136. Single Number
- 此題為 List 中只有一個重複的元素, 求出來
- 因此可以用 XOR 的方式去解

### LC217. Contains Duplicate
- 而此題是要求 List 中是否有包含重複的元素
- XOR 派不上用場
