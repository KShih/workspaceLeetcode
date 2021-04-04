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
